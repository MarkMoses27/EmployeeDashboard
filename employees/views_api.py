# employees/views_api.py
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeDetailView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
