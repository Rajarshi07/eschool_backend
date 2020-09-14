from .models import course, teacher_form, intern_form
from .serializers import CourseSerializer, TeacherFormSerializer, InternFormSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

class grade_view(APIView):

	def get(self, request, grade, format = None):
		class_courses = course.objects.filter(grade = grade)
		serialized = CourseSerializer(class_courses, many=True)
		return Response(serialized.data)

class teacher_form(APIView):

	def post(self, request, format = None):	
		new_teacherform = TeacherFormSerializer(data = request.data)
		if new_teacherform.is_valid():
			new_teacherform.save()

class intern_form(APIView):

	def post(self, request, format = None):
		new_internform = InternFormSerializer(data = request.data)
		if new_teacherform.is_valid():
			new_internform.save()
"""class search(APIView):

	def get(self, request, val, format = None):
		val = list(val.split(" "))
		q_search = (Q(subject__icontains = val[0]) |Q(grade__icontains = val[0]) | Q(name__icontains = val[0]))
		if len(val) > 1:
			for i in range(1,len(val)):
				q_search.connector = Q.OR
				q_search = q_search.add((Q(subject__icontains = val[i]) |Q(grade__icontains = val[i]) | Q(name__icontains = val[i])), q_search.connector)
		q_search = (Q(name__icontains = val[0]))
		if len(val) > 1:
			for i in range(1,len(val)):
				q_search.connector = Q.AND
				q_search = q_search.add((Q(name__icontains = val[i])), q_search.connector)
		print(q_search)
		s = course.objects.filter(q_search)
		if len(s)>5:
			s = s[:5]
		course_serializer = SearchSerializer(s, many = True)
		return Response(course_serializer.data)"""

