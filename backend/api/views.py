import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Course, Student, Enrollment
from datetime import datetime


# Course API
def courses_api(request):
    """API endpoint for the collection of courses"""

    if request.method == 'POST':
        # Create a new course
        data = json.loads(request.body)
        course = Course.objects.create(
            name=data['name'],
            description=data['description'],
            credits=data['credits'],
            start_date=data['start_date']
        )
        return JsonResponse(course.as_dict())

    # GET all courses
    courses = [course.as_dict() for course in Course.objects.all()]
    return JsonResponse({'courses': courses})


def course_api(request, course_id):
    """API endpoint for a single course"""
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'PUT':
        # Update the course
        data = json.loads(request.body)
        course.name = data.get('name', course.name)
        course.description = data.get('description', course.description)
        course.credits = data.get('credits', course.credits)
        course.start_date = data.get('start_date', course.start_date)
        course.save()
        return JsonResponse(course.as_dict())

    if request.method == 'DELETE':
        # Delete the course
        course.delete()
        return JsonResponse({})

    # GET single course details
    return JsonResponse(course.as_dict())


# Student API
def students_api(request):
    """API for the collection of students"""

    if request.method == 'POST':
        # Create a new student
        data = json.loads(request.body)
        student = Student.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            age=data['age'],
            is_active=data.get('is_active', True)
        )
        return JsonResponse(student.as_dict())

    # GET all students
    students = [student.as_dict() for student in Student.objects.all()]
    return JsonResponse({'students': students})


def student_api(request, student_id):
    """API for a single student"""
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'PUT':
        # Update the student
        data = json.loads(request.body)
        student.first_name = data.get('first_name', student.first_name)
        student.last_name = data.get('last_name', student.last_name)
        student.age = data.get('age', student.age)
        student.is_active = data.get('is_active', student.is_active)
        student.save()
        return JsonResponse(student.as_dict())

    if request.method == 'DELETE':
        # Delete the student
        student.delete()
        return JsonResponse({})

    # get student details
    return JsonResponse(student.as_dict())


# Enrollment api
def enrollments_api(request):
    """API the collection of enrollments"""
    
    if request.method == 'POST':
        # Create enrollments
        data = json.loads(request.body)

        # Extract data from the request
        course_ids = data.get('course_ids', [])
        student_id = data.get('student_id')
        enrollment_date = data.get('enrollment_date', datetime.now())
        notes = data.get('notes', "")

        # Validate student
        student = get_object_or_404(Student, id=student_id)

        # List to hold all created enrollments
        enrollments_created = []

        # Loop through each course_id and create an enrollment for each
        for course_id in course_ids:
            course = get_object_or_404(Course, id=course_id)
            enrollment = Enrollment.objects.create(
                course=course,
                student=student,
                enrollment_date=enrollment_date,
                notes=notes
            )
            enrollments_created.append(enrollment.as_dict())

        # Return created enrollments
        return JsonResponse({"enrollments": enrollments_created}, status=201)

    elif request.method == 'GET':
        # Get student_id from query
        student_id = request.GET.get('student_id')

        if student_id:
            # If student_id is there, filter enrollments by student_id
            enrollments = [enrollment.as_dict() for enrollment in Enrollment.objects.filter(student__id=student_id)]
        else:
            # If no student_id is there, return all enrollments
            enrollments = [enrollment.as_dict() for enrollment in Enrollment.objects.all()]

        return JsonResponse({'enrollments': enrollments})

    # For unsupported methods, return a 405 Method Not Allowed
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def enrollment_api(request, enrollment_id):
    """API for a single enrollment"""
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)

    if request.method == 'PUT':
        # Update enrollment
        data = json.loads(request.body)
        enrollment.enrollment_date = data.get('enrollment_date', enrollment.enrollment_date)
        enrollment.notes = data.get('notes', enrollment.notes)
        enrollment.save()
        return JsonResponse(enrollment.as_dict())

    if request.method == 'DELETE':
        # Delete the enrollment
        enrollment.delete()
        return JsonResponse({})

    # get single enrollment details
    return JsonResponse(enrollment.as_dict())
