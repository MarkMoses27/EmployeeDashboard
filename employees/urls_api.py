# employees/urls_api.py
from django.urls import path
from .views_api import EmployeeDetailView

urlpatterns = [
    path('api/employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-api-detail'),
    # Add more API URL patterns as needed
]
