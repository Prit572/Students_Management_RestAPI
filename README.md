# Student Management REST API using Flask and SQLite

This is a basic project that demonstrates how to create a REST API using Flask. It supports storing, updating, viewing, and deleting student records, with the data persisted in a SQLite database.

## 🚀 Features

- ✅ Add new students  
- 👀 View all students  
- 🔍 View student by ID  
- ✏️ Update student information  
- ❌ Delete a student  
- ⚠️ Error messages for invalid operations  

---

## 📦 Requirements

Make sure you have Python installed. Then install the required libraries by running:

```
pip install Flask Flask-RESTful Flask-SQLAlchemy
```

---

## 🛠️ How to Run the Project

1. Clone or download the project files.
2. Save the main code in a file named `app.py`.
3. Open your terminal or command prompt in the same folder.
4. Start the Flask server using:

```
python app.py
```

5. Access the API at:  
   `http://127.0.0.1:5000/students`

---

## 📌 API Endpoints

### 1. Add a Student

- **Method**: `POST`  
- **URL**: `/students`  
- **Body (JSON)**:

```json
{
  "name": "Prit Chaniyara",
  "age": 20
}
```

---

### 2. Get All Students

- **Method**: `GET`  
- **URL**: `/students`

---

### 3. Get a Student by ID

- **Method**: `GET`  
- **URL**: `/students/<id>`

---

### 4. Update a Student by ID

- **Method**: `PUT`  
- **URL**: `/students/<id>`  
- **Body (JSON)**:

```json
{
  "name": "Prit Patel",
  "age": 21
}
```

---

### 5. Delete a Student by ID

- **Method**: `DELETE`  
- **URL**: `/students/<id>`

---

## 📝 Notes

- If the student ID is not found, a proper error message will be returned.
- The SQLite database file (`students.db`) will be created automatically in the same directory as `app.py`.

---

## 📚 Purpose

This project was created for learning and demonstration purposes. Feel free to modify and extend it.
