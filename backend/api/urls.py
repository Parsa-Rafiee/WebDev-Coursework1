"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    courses_api, course_api,
    students_api, student_api,
    enrollments_api, enrollment_api
)

urlpatterns = [
    
    path('courses/', courses_api, name='courses_api'),
    path('course/<int:course_id>/', course_api, name='course_api'),
    
    path('students/', students_api, name='students_api'),
    path('student/<int:student_id>/', student_api, name='student_api'),

    path('enrollments/', enrollments_api, name='enrollments_api'),
    path('enrollment/<int:enrollment_id>/', enrollment_api, name='enrollment_api'),
]
