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
from rest_framework.validators import UniqueValidator

from rest_framework import serializers


def validate_unique_username(value):

    if User.objects.filter(username=value).exists():
        raise serializers.ValidationError("Username is not available. Try another one.")
    return value


def validate_unique_email(value):

    if User.objects.filter(email=value).exists():
        raise serializers.ValidationError(
            "This Email is already taken. Try another one."
        )
    return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]
        extra_kwargs = {
            "password": {"write_only": True},
            "role": {"read_only": True},
            "date_joined": {"read_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class DoctorRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        source="user.username",
        validators=[validate_unique_username],
    )
    email = serializers.EmailField(
        required=True, source="user.email", validators=[validate_unique_email]
    )
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True, source="user.first_name")
    last_name = serializers.CharField(required=True, source="user.last_name")
    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), required=True
    )
    specialization = serializers.CharField(required=True)
    phone = serializers.CharField(max_length=20, required=True, write_only=True)
    experience = serializers.IntegerField(required=True)
    is_available = serializers.BooleanField(default=True)

    class Meta:
        model = Doctor
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "department",
            "specialization",
            "phone",
            "experience",
            "is_available",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        phone = validated_data.pop("phone")
        department = validated_data.pop("department")
        specialization = validated_data.pop("specialization")
        experience = validated_data.pop("experience")
        is_available = validated_data.pop("is_available")

        user_data = validated_data.pop("user")
        password = validated_data.pop("password")

        user = User.objects.create_user(
            username=user_data["username"],
            email=user_data["email"],
            password=password,
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            role="doctor",
        )

        doctor = Doctor.objects.create(
            user=user,
            phone=phone,
            department=department,
            specialization=specialization,
            experience=experience,
            is_available=is_available,
        )
        return doctor


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class PatientRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        source="user.username",
        validators=[validate_unique_username],
    )
    email = serializers.EmailField(
        required=True,
        source="user.email",
        validators=[validate_unique_email],
    )
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True, source="user.first_name")
    last_name = serializers.CharField(required=True, source="user.last_name")

    age = serializers.IntegerField(required=True)
    gender = serializers.CharField(required=True)
    blood_group = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    phone = serializers.CharField(max_length=20, required=True, write_only=True)

    class Meta:
        model = Patient
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "age",
            "gender",
            "blood_group",
            "address",
            "phone",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        age = validated_data.pop("age")
        gender = validated_data.pop("gender")
        blood_group = validated_data.pop("blood_group")
        address = validated_data.pop("address")
        phone = validated_data.pop("phone")

        user_data = validated_data.pop("user")
        password = validated_data.pop("password")

        user = User.objects.create_user(
            username=user_data["username"],
            email=user_data["email"],
            password=password,
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            role="patient",
        )

        patient = Patient.objects.create(
            user=user,
            age=age,
            gender=gender,
            blood_group=blood_group,
            address=address,
            phone=phone,
        )
        return patient


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.filter(is_available=True)
    )
    class Meta:
        model = Appointment
        fields = "__all__"


class PrescriptionMedicineSerializer(serializers.ModelSerializer):
    dosage = serializers.CharField(required=True)
    duration = serializers.CharField(required=True)
    medicine_name = serializers.ReadOnlyField(source="medicine.name")

    class Meta:
        model = PrescriptionMedicine
        fields = "__all__"


class PrescriptionSerializer(serializers.ModelSerializer):

    appointment = serializers.PrimaryKeyRelatedField(
        queryset=Appointment.objects.filter(status='confirmed')
    )

    class Meta:
        model = Prescription
        fields = "__all__"


class MedicineSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    unit = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Medicine
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):
    patient_name = serializers.ReadOnlyField(source="patient.user.username")

    class Meta:
        model = Bill
        fields = "__all__"
