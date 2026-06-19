# Hospital Management System (HMS)

A simple Django-based Hospital Management System backend.

**Overview**

- Minimal REST API for managing patients, doctors, appointments and related hospital data.

**Setup (local)**

- Prerequisites: Python 3.8+, pip, virtualenv (Postgres optional).
- Clone the repo and enter the project root:

```bash
git clone <repo-url>
cd "Hospital Management System"
```

- Create and activate a virtual environment, then install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# If there is no requirements.txt, at minimum install:
# pip install django djangorestframework
```

- Configure environment variables (optional):
  - `SECRET_KEY` (Django secret)
  - `DATABASE_URL` (if using external DB)

- Run migrations, create a superuser, and start the dev server:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Run tests:

```bash
python manage.py test
```

**Authentication**

- Uses Django authentication (session or token depending on your configuration).
- All API endpoints require authentication unless explicitly marked public.

**Roles & Permissions (typical mapping)**

- Admin / Superuser:
  - Access: All API endpoints
  - Actions: Create / Read / Update / Delete everything

- Staff (Hospital staff with elevated rights):
  - Access: Most management endpoints
  - Actions: Create / Read / Update / Delete for non-admin tasks (users, schedules, basic records)

- Doctor:
  - Access: Patient records, appointments, medical notes related to their patients
  - Actions: Create medical notes/diagnoses, Update patient treatment data, Read patient records; limited Delete (usually not allowed)

- Nurse:
  - Access: Patient vitals, ward/bed assignments, appointments
  - Actions: Create / Update vitals and nursing notes, Read patient records; limited Delete

- Receptionist:
  - Access: Appointments, patient basic info, scheduling
  - Actions: Create / Read / Update appointments and patient administrative info; no clinical record delete rights

- Patient (end-user):
  - Access: Own profile and own medical/appointment data
  - Actions: Read own records, Update personal profile, Create appointment requests; no delete access to clinical records

Note: The project file `backend/permission.py` is the canonical place to implement or adjust permission logic.

**Common API endpoints (examples)**

- `/api/patients/` — patient list & detail
- `/api/doctors/` — doctors list & detail
- `/api/appointments/` — appointment CRUD
- `/api/auth/` — login / token endpoints

Adjust endpoint paths to match the code in `backend/urls.py` and `HMS/urls.py`.

**Extending or changing permissions**

- Edit or extend `backend/permission.py` and corresponding view permissions in `backend/views.py`.
- Use Django REST Framework permission classes for fine-grained control.

If you want, I can: add actual endpoint docs (list every route), generate a `requirements.txt`, or implement role-based permission classes in `backend/permission.py`. Which would you like next?
