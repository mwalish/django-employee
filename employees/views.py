from django.shortcuts import render
from rest_framework import viewsets, generics

from employees.models import Department, Employee
from employees.serializer import Departmentseializer, EmployeeSeriallizer



# DEPARTMENT VIEWSET

class DepartmentViewSets(viewsets.ModelViewSet):
    """
    A complete ModelViewSet that automatically handles all CRUD operations
    for the Department model. This includes:
    - GET /departments/         -> List all departments
    - POST /departments/        -> Create a new department
    - GET /departments/{id}/    -> Retrieve a specific department
    - PUT /departments/{id}/    -> Update a specific department
    - DELETE /departments/{id}/ -> Delete a specific department
    """
    # Tell DRF which database records to pull
    queryset = Department.objects.all()
    
    # Connect this view to the department serializer for data formatting
    serializer_class = Departmentseializer


# EMPLOYEE GENERIC VIEWS


class EmployeelistCreateViews(generics.ListCreateAPIView):
    """
    A concrete generic view that handles collection-level operations.
    - GET /employees/  -> Fetches a list of all existing employees.
    - POST /employees/ -> Validates and adds a brand new employee.
    """
    # Define the database records targeted by this endpoint
    queryset = Employee.objects.all()
    
    # Use the Employee serializer to validate and structure the data
    serializer_class = EmployeeSeriallizer


class EmployeListeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    A concrete generic view that handles instance-level operations.
    Expects an ID (lookup field) passed via the URL path.
    - GET /employees/{id}/    -> Fetches details for a single employee.
    - PUT/PATCH /employees/{id}/ -> Modifies data for a single employee.
    - DELETE /employees/{id}/ -> Removes a single employee from the database.
    """
    # Define the database records targeted by this endpoint
    queryset = Employee.objects.all()
    
    # Use the Employee serializer to validate and structure the data
    serializer_class = EmployeeSeriallizer