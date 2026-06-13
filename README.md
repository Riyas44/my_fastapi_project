# my_fastapi_project
📘 Project Description This project is a beginner-friendly FastAPI CRUD application that demonstrates how to manage user records in memory using Python. It uses Pydantic models for data validation and provides RESTful API endpoints for creating, reading, updating, and deleting users.

🚀 Features
Create User: Add a new user with user_id and name.

Get All Users: Retrieve a list of all users.

Get User by ID: Fetch details of a specific user.

Update User: Modify an existing user’s information.

Delete User: Remove a user by ID.

📂 Project Structure
main.py → Contains FastAPI app and endpoints.

Item model → Defines user schema with user_id and name.

users list → Acts as an in-memory database.

▶️ How to Run

Install dependencies:
pip install fastapi uvicorn

Start the server:
uvicorn main:app --reload
