from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Step 1: Create the Flask app and connect it with a SQLite database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Database file will be created in the same folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # Connecting SQLAlchemy with the app
api = Api(app)  # Initializing Flask-RESTful API

# Step 2: Create a Student model (like a table structure)
class StudentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)         # Student ID (unique)
    name = db.Column(db.String(100), nullable=False)     # Student Name (required)
    age = db.Column(db.Integer, nullable=False)          # Student Age (required)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "age": self.age}

# Step 3: Create the database and table if it doesn’t exist already
with app.app_context():
    db.create_all()

# Step 4: Input validation (to check if name and age are sent in request)
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help="Name is required and cannot be blank.")
parser.add_argument('age', type=int, required=True, help="Age is required and must be an integer.")

# Step 5: Handle GET and POST requests for /students
class StudentList(Resource):
    def get(self):
        # Return all student records in JSON
        students = StudentModel.query.all()
        return [student.to_dict() for student in students], 200

    def post(self):
        # Add a new student to the database
        args = parser.parse_args()
        name, age = args['name'], args['age']
        if not name.strip():  # Check if name is empty
            return {"error": "Name cannot be empty"}, 400
        try:
            new_student = StudentModel(name=name.strip(), age=age)
            db.session.add(new_student)
            db.session.commit()
            return new_student.to_dict(), 201  # Successfully created
        except IntegrityError:
            db.session.rollback()
            return {"error": "Database error"}, 500  # Some DB error occurred

# Step 6: Handle GET, PUT, DELETE requests for /students/<id>
class Student(Resource):
    def get(self, student_id):
        # Get a student by their ID
        student = StudentModel.query.get(student_id)
        if not student:
            abort(404, message="Student not found")  # Student not found
        return student.to_dict(), 200

    def put(self, student_id):
        # Update an existing student by ID
        args = parser.parse_args()
        student = StudentModel.query.get(student_id)
        if not student:
            abort(404, message="Student not found")
        student.name = args['name'].strip()
        student.age = args['age']
        db.session.commit()
        return student.to_dict(), 200

    def delete(self, student_id):
        # Delete a student by ID
        student = StudentModel.query.get(student_id)
        if not student:
            abort(404, message="Student not found")
        db.session.delete(student)
        db.session.commit()
        return {'message': 'Student deleted'}, 200

# Step 7: Link endpoints with their classes
api.add_resource(StudentList, '/students')                # /students handles GET and POST
api.add_resource(Student, '/students/<int:student_id>')  # /students/<id> handles GET, PUT, DELETE

# Step 8: Run the app
if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
