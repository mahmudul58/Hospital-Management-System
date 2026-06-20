from django.db import models
from django.contrib.auth.models import User,AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin','Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
        ('receptionist', 'Receptionist'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')

    def save(self, *args, **kwargs):
        if self.is_superuser: 
            self.role = 'admin' 
        super().save(*args, **kwargs)



class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='doctor_profile')
    department=models.ForeignKey('Department',on_delete=models.CASCADE)
    specialization=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    experience=models.PositiveIntegerField()
    is_available=models.BooleanField(default=True)
    def __str__(self):
        return self.user.username

class Department(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.name
    
class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='patient_profile')
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=10)
    blood_group=models.CharField(max_length=10)
    address=models.TextField()
    phone=models.CharField(max_length=15)
    def __str__(self):
        return self.user.username
    
class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Appointment_date=models.DateTimeField()
    status=models.CharField(max_length=20,choices=[('Pending','Pending'),('Confirmed','Confirmed'),('Cancelled','Cancelled')],default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.patient.user.username} - {self.doctor.user.username} - {self.Appointment_date}"

class Prescription(models.Model):
    appointment=models.OneToOneField(Appointment,on_delete=models.CASCADE)
    diagnosis=models.TextField()
    notes=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Prescription for {self.appointment.patient.user.username} - {self.appointment.doctor.user.username}"
    
class PrescriptionMedicine(models.Model):
    prescription=models.ForeignKey(Prescription,on_delete=models.CASCADE)
    medicine=models.ForeignKey('Medicine',on_delete=models.CASCADE)
    dosage=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.medicine.name} for {self.prescription.appointment.patient.user.username}"

class Medicine(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    unit=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.name

class Bill(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    paid=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Bill for {self.patient.user.username} - {self.amount}"