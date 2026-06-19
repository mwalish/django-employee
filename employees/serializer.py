from rest_framework import serializers
from employees.models import Department, Employee


# =====================================================================
# DEPARTMENT SERIALIZER
# =====================================================================
class Departmentseializer(serializers.ModelSerializer):
    """
    Converts Department model data into JSON format for API responses,
    and validates incoming JSON data to convert it back into Django objects.
    Acts as the bridge between the Django database and the API client.
    """

    class Meta:
        # Link this serializer directly to the Department database model
        model = Department
        
        # Automatically include every single field from the Department model
        fields = '__all__'


# =====================================================================
# EMPLOYEE SERIALIZER
# =====================================================================
class EmployeeSeriallizer(serializers.ModelSerializer):
    """
    Handles serialization for the Employee model.
    Uses a dual-field approach for the Department relationship:
    - Displays full details on GET requests.
    - Accepts a simple integer ID on POST/PUT requests.
    """

    # READ-ONLY FIELD: 
    # When fetching data (GET), this nests the complete Department object 
    # details (ID, name, etc.) instead of just showing a raw ID number.
    department = Departmentseializer(read_only=True)
    
    # WRITE-ONLY FIELD:
    # When creating/updating data (POST/PUT), this expects a simple primary key (integer ID).
    # 'source=department' ensures DRF maps this ID directly to the model's 'department' relationship.
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department',
        write_only=True
    )
   
    class Meta:
        # Link this serializer directly to the Employee database model
        model = Employee
        
        # Automatically include all fields from the Employee model, 
        # including the custom 'department' and 'department_id' fields defined above.
        fields = "__all__"