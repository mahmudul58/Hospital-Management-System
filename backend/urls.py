from django.urls import path,include

from backend import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'doctor-list', views.DoctorViewSet)
router.register(r'department', views.DepartmentViewSet)
router.register(r'patient-list', views.PatientViewSet)
router.register(r'appointment', views.AppointmentViewSet)
router.register(r'medicine', views.MedicineListViewSet)
router.register(r'bill', views.BillListViewSet)
urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('doctor-available/',views.DoctorAvailabilityView.as_view(),name='doctor-available'),
    path('dr-reg/',views.DoctorRegisterView.as_view(),name='dr-reg'),
    path('patient-reg/',views.PatientRegisterView.as_view(),name='patient-reg'),
    path('receptionist-reg/',views.ReceptionistRegisterView.as_view(),name='receptionist-reg'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('prescription-create/',views.PrescriptionCreateView.as_view(),name='prescription-create'),
    path('prescription-list/',views.PrescriptionListView.as_view(),name='prescription-list'),
    path('prescription-medicine/',views.PrescriptionMedicineCreateView.as_view(),name='prescription-medicine'),
    path('prescription-medicine-list/',views.PrescriptionMedicineListView.as_view(),name='prescription-medicine-list'),

]