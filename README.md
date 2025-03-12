# Web-Based Library Management System

## 📌 Project Description

The **Web-Based Library Management System** is a Django-based web application that helps libraries efficiently manage books, users, and borrowing transactions. It provides an easy-to-use interface for administrators and users to interact with the library system.

## 🚀 Features

- 📚 **Book Management** – Add, update, delete, and search for books.
- 👥 **User Management** – Register users and manage their accounts.
- 📊 **Dashboard & Reports** – View statistics on book availability and user activity.

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS
- **Dependencies**: See `requirements.txt`

## 📥 Installation & Setup

### Prerequisites

- Python 3.x installed
- Django installed (`pip install django`)

### Steps to Run the Project

1. Clone the repository:
   ```sh
   git clone https://github.com/RahulK847/Web_Based_Library_Managment_System.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Web_Based_Library_Managment_System
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser (for admin access):
   ```sh
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```
7. Open `http://127.0.0.1:8000/` in your browser.

## 🎯 Usage Guide

- **Admin Panel**: Accessible at `/admin/` for managing books and users.
- **User Dashboard**: Users can browse books and track their borrow history.

