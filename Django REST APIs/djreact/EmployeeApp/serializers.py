'''Serializers allow complex data such as querysets and model instances to be converted to native Python 
datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide 
deserialization, allowing parsed data to be converted back into complex types, after first validating the 
incoming data.

The serializers in REST framework work very similarly to Django's Form and ModelForm classes. We provide 
a Serializer class which gives you a powerful, generic way to control the output of your responses, as well 
as a ModelSerializer class which provides a useful shortcut for creating serializers that deal with model 
instances and querysets.'''

# in simple terms serializers package data when going to server and unpackage when coming form server

from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                  'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                  'EmployeeName',
                  'Department',
                  'DateOfJoining',
                  'PhotoFileName')
                  