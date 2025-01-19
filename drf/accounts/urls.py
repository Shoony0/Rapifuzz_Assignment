from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('forgot/password/<int:pk>/', views.ForgotPasswordView.as_view(), name='forgot_password'),
    path('register/incident/', views.RegisterIncidentView.as_view(), name='register_incident'),
    path('view/incident/', views.IncidentView.as_view(), name='register_incident'),
    path('get/incident/<str:pk>/', views.GetIncidentView.as_view(), name='get_incident'),
    path('update/incident/status/<str:pk>/', views.UpdateIncidentStatusView.as_view(), name='update_incident_status'),
    path('get/pincode/details/<str:pincode>/', views.PincodeDetailsView.as_view(), name='pincode_details'),
]
