from .models import course, teacher_form, intern_form
from rest_framework import serializers

class GradeSerializer(serializers.ModelSerializer):
	class Meta:
		model = course
		fields = ('id','name',)

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = course
		fields = "__all__" 

class TeacherFormSerializer(serializers.ModelSerializer):
	class Meta:
		model = teacher_form
		fields = "__all__"

class InternFormSerializer(serializers.ModelSerializer):
	class Meta:
		model = intern_form
		fields = "__all__"