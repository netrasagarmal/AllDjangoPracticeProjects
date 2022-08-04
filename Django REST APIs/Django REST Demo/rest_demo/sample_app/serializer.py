# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import StudentModel

# Create a model serializer
class StudentSerializer(serializers.ModelSerializer):
	# specify model and fields
	class Meta:
		model = StudentModel
		fields = ('sId', 'studentName', 'studentClass')
