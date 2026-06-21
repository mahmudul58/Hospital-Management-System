# 🏥 Hospital Management System (HMS)

A RESTful API backend for managing hospital operations — built with **Django**, **Django REST Framework**, and **JWT authentication**. Supports role-based access control for Admins, Doctors, Patients and Receptionist.

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.14 or higher
- PostgreSQL Server running locally
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

---

## 🔗 API Endpoint Reference (Quick Links)

Here is a quick overview of all the available API routes and the specific user roles required to access them.

### 🔐 Authentication & Registration
| Endpoint | Method | Required Role / Permission | Description |
|---|---|---|---|
| `/login/` | `POST` | **Any** | Login to receive JWT Tokens |
| `/patient-reg/` | `POST` | **Any** | Register a new Patient profile |
| `/doctor-reg/` | `POST` | **Admin, Receptionist** | Register a new Doctor profile |
| `/receptionist-reg/` | `POST` | **Admin** | Register a new Receptionist profile |

### 👨‍⚕️ Doctors & Patients
| Endpoint | Method | Required Role / Permission | Description |
|---|---|---|---|
| `/doctor-available/` | `GET` | **Any** | View a list of available doctors |
| `/doctor-list/` | `GET, POST, PUT, DELETE` | **Authenticated Users** | Manage and view doctors |
| `/patient-list/` | `GET, POST, PUT, DELETE` | **Authenticated Users** | Manage and view patients |

### 🏥 Departments & Appointments
| Endpoint | Method | Required Role / Permission | Description |
|---|---|---|---|
| `/department/` | `GET, POST, PUT, DELETE` | **Admin, Receptionist** | Manage hospital departments |
| `/appointment/` | `GET, POST, PUT, DELETE` | **Admin, Receptionist** | Manage appointments (Supports `?search=` and filters) |

### 💊 Prescriptions & Medicines
| Endpoint | Method | Required Role / Permission | Description |
|---|---|---|---|
| `/prescription-create/` | `POST` | **Doctor** | Create a prescription with nested medicines |
| `/prescription-list/` | `GET` | **Authenticated Users** | View a list of all prescriptions |
| `/medicine/` | `GET, POST, PUT, DELETE` | **Admin, Receptionist** | Manage the medicine inventory (Supports `?search=`) |

### 🧾 Billing
| Endpoint | Method | Required Role / Permission | Description |
|---|---|---|---|
| `/bill/` | `GET, POST, PUT, DELETE` | **Admin, Receptionist** | Generate and manage patient bills |
