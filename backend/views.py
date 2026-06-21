from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from backend.serializers import (
    UserSerializer,
    DoctorRegisterSerializer,
    DepartmentSerializer,
    DoctorSerializer,
    PatientSerializer,
    PatientRegisterSerializer,
    LoginSerializer,
    AppointmentSerializer,
    PrescriptionSerializer,
    PrescriptionMedicineSerializer,
    MedicineSerializer,
    BillSerializer,
)
from backend.models import (
    Doctor,
    Department,
    Patient,
    User,
    Appointment,
    Prescription,
    PrescriptionMedicine,
    Medicine,
    Bill,
)

from . permission import IsAdminUser, IsAdminOrReceptionist, IsDoctorUser




class DoctorRegisterView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorRegisterSerializer
    permission_classes=[IsAdminOrReceptionist]

class DoctorAvailabilityView(generics.ListAPIView):
    queryset=Doctor.objects.filter(is_available=True)
    serializer_class = DoctorRegisterSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class PatientRegisterView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientRegisterSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    

def get_tokens_for_user(user):

    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "Invalid email or password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not user.check_password(password):
            return Response(
                {"error": "Invalid email or password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        tokens = get_tokens_for_user(user)
        return Response(
            {
                "message": "Login successful",
                "user_id": user.id,
                "email": user.email,
                "role": user.role,
                "username": user.username,
                "tokens": tokens,
            }
        )


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes=[IsAdminOrReceptionist]


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAdminOrReceptionist]

    #filtering
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['doctor', 'patient', 'status']
    search_fields = [
        'doctor__user__first_name', 
        'doctor__user__last_name',
        'doctor__user__username',
        'patient__user__first_name', 
        'patient__user__last_name',
        'patient__user__username'
    ]


class PrescriptionCreateView(generics.CreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsDoctorUser]

class PrescriptionListView(generics.ListAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]

class MedicineListViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAdminOrReceptionist]

    # searching
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']

class BillListViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAdminOrReceptionist]

class ReceptionistRegisterView(generics.CreateAPIView):
    
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser] 

    def perform_create(self, serializer):
        serializer.save(role="receptionist")