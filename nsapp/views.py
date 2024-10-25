from django.shortcuts import render
from rest_framework import generics
from .serializer import InstructorSerializer, CourseSerializer
from .models import Instructor, Course
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import BasicAuthentication
# from rest_framework.viewsets import ModelViewSet


class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        if request.method=='GET':
            return True
        
        if request.method == 'POST' or request.method=='PUT' or request.method=='DELETE':
            if user.is_superuser:
                return True
        return False

# Create your views here.

class InstructorListView(generics.ListCreateAPIView):
    queryset=Instructor.objects.all()
    serializer_class=InstructorSerializer


class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Instructor.objects.all()
    serializer_class=InstructorSerializer

class CourseListView(generics.ListCreateAPIView):
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    permission_classes=[IsAuthenticated, WriteByAdminOnlyPermission]
    queryset=Course.objects.all()
    serializer_class=CourseSerializer


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

# class InstructorListView(ModelViewSet):
#     queryset=Instructor.objects.all()
#     serializer_class=InstructorSerializer

# class CourseListView(ModelViewSet):
#     queryset=Course.objects.all()
#     serializer_class=CourseSerializer
