from django.contrib import admin

from backend.models import (
    Department,
    Doctor,
    User,
    Patient,
    Appointment,
    Prescription,
    PrescriptionMedicine,
    Medicine,
    Bill,
)

# Register your models here.
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Department)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(PrescriptionMedicine)
admin.site.register(Medicine)
admin.site.register(Bill)
