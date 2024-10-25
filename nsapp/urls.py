from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import *

# router=DefaultRouter()
# router.register('instructor', InstructorListView, basename='instructorList')

urlpatterns = [
    # path('', include(router.urls)),
    path('instructor/', InstructorListView.as_view(), name='instructorList'),
    path('instructor/<int:pk>', InstructorDetailView.as_view(), name='instructor-detail'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
]
