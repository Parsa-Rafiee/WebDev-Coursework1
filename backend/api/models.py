from django.db import models
from django.urls import reverse


class Course(models.Model):
    """Course model"""

    name = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.IntegerField()
    start_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.credits} credits)"

    def as_dict(self):
        return {
            'id': self.id,
            'api': reverse('course_api', args=[self.id]),
            'name': self.name,
            'description': self.description,
            'credits': self.credits,
            'start_date': self.start_date,
        }


class Student(models.Model):
    """Student model"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def as_dict(self):
        return {
            'id': self.id,
            'api': reverse('student_api', args=[self.id]),
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'is_active': self.is_active,
        }


class Enrollment(models.Model):
    """Enrollment model"""

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} enrolled in {self.course} on {self.enrollment_date}"

    def as_dict(self):
        return {
            'id': self.id,
            'course': self.course.name,
            'student': self.student.as_dict(),
            'enrollment_date': self.enrollment_date,
            'notes': self.notes,
        }
