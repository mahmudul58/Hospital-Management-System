# 🏥 Hospital Management System (HMS)

A RESTful API backend for managing hospital operations — built with **Django**, **Django REST Framework**, and **JWT authentication**. Supports role-based access control for Admins, Doctors, Patients and Receptionist.

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.14 or higher
- MySQL Server running locally
- `pip` package manager
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/mahmudul58/Hospital-Management-System.git
cd Hospital-Management-System
```

### 2. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄 Database Configuration

### Step 1 — Create the MySQL Database

Open your MySQL client (Workbench, CLI, or phpMyAdmin) and run:

```sql
CREATE DATABASE hms_db;
```

### Step 2 — Configure `HMS/settings.py`

Find the `DATABASES` section and update it with your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hms_db',          # your database name
        'USER': 'root',            # your MySQL username
        'PASSWORD': 'yourpassword',# your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

> **Note:** This project uses `PyMySQL` as the MySQL driver. Make sure the following is present at the top of `HMS/__init__.py`:
>
> ```python
> import pymysql
> pymysql.install_as_MySQLdb()
> ```

### Step 3 — Apply Migrations (Create Tables)

```bash
python manage.py makemigrations
python manage.py migrate
```

This will automatically create all required tables in your `hms_db` database.

### Step 4 — Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

---

## 🚀 Running the Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Django Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
