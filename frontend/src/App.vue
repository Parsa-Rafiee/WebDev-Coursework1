<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded bg-light p-2 mb-3">
            {{ title }}
        </div>

        <!-- tabs for Courses, Students, and Enrollments -->
        <ul class="nav nav-tabs mb-3" id="courseStudentTabs" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link active" id="courses-tab" data-bs-toggle="tab" data-bs-target="#courses" type="button" role="tab">
                    Courses
                </button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="students-tab" data-bs-toggle="tab" data-bs-target="#students" type="button" role="tab">
                    Students
                </button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="enrollments-tab" data-bs-toggle="tab" data-bs-target="#enrollments" type="button" role="tab">
                    Enrollments
                </button>
            </li>
        </ul>

        <div class="tab-content">
            <!-- Courses tab -->
            <div class="tab-pane fade show active" id="courses" role="tabpanel">
                <button class="btn btn-sm btn-success mb-3" data-bs-toggle="modal" data-bs-target="#addCourseModal">
                    <i class="bi bi-plus"></i> Add Course
                </button>

                <!-- courses Modal -->
                <div class="modal fade" id="addCourseModal" tabindex="-1" aria-labelledby="addCourseModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="addCourseModalLabel">Add Course</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="mb-3">
                                    <label for="courseName" class="form-label">Name</label>
                                    <input v-model="newCourse.name" type="text" class="form-control" id="courseName">
                                </div>
                                <div class="mb-3">
                                    <label for="courseDescription" class="form-label">Description</label>
                                    <textarea v-model="newCourse.description" class="form-control" id="courseDescription" rows="3"></textarea>
                                </div>
                                <div class="mb-3">
                                    <label for="courseCredits" class="form-label">Credits</label>
                                    <input v-model="newCourse.credits" type="number" class="form-control" id="courseCredits">
                                </div>
                                <div class="mb-3">
                                    <label for="courseStartDate" class="form-label">Start Date</label>
                                    <input v-model="newCourse.start_date" type="date" class="form-control" id="courseStartDate">
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button type="button" class="btn btn-primary" @click="createCourse" data-bs-dismiss="modal">Save</button>
                            </div>
                        </div>
                    </div>
                </div>

                <!--  List Component -->
                <CourseTable 
                    :courses="courses"
                    @delete-course="deleteCourse"
                    @update-course="updateCourse"
                />
            </div>

            <!-- students Tab -->
            <div class="tab-pane fade" id="students" role="tabpanel">
                <button class="btn btn-sm btn-success mb-3" data-bs-toggle="modal" data-bs-target="#addStudentModal">
                    <i class="bi bi-plus"></i> Add Student
                </button>

                <!-- Students Modal -->
                <div class="modal fade" id="addStudentModal" tabindex="-1" aria-labelledby="addStudentModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="addStudentModalLabel">Add Student</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="mb-3">
                                    <label for="studentFirstName" class="form-label">First Name</label>
                                    <input v-model="newStudent.first_name" type="text" class="form-control" id="studentFirstName">
                                </div>
                                <div class="mb-3">
                                    <label for="studentLastName" class="form-label">Last Name</label>
                                    <input v-model="newStudent.last_name" type="text" class="form-control" id="studentLastName">
                                </div>
                                <div class="mb-3">
                                    <label for="studentAge" class="form-label">Age</label>
                                    <input v-model="newStudent.age" type="number" class="form-control" id="studentAge">
                                </div>
                                <div class="mb-3">
                                    <label for="studentActive" class="form-check-label">Is Active</label>
                                    <input v-model="newStudent.is_active" type="checkbox" class="form-check-input" id="studentActive">
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button type="button" class="btn btn-primary" @click="createStudent" data-bs-dismiss="modal">Save</button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- List Component -->
                <StudentTable 
                    :students="students"
                    @delete-student="deleteStudent"
                />

            </div>
            <!-- enrollment Tab -->
            <div class="tab-pane fade" id="enrollments" role="tabpanel">
                <Enrollment 
                    :students="students" 
                    :courses="courses"
                />
            </div>
        </div>
    </div>
</template>

<script>
import CourseTable from './components/CourseTable.vue'
import StudentTable from './components/StudentTable.vue'
import Enrollment from './components/Enrollment.vue'

const baseUrl = 'http://localhost:8000'

export default {
    components: {
        CourseTable,
        StudentTable,
        Enrollment
    },
    data() {
        return {
            title: 'Course and Student Management',
            courses: [],
            students: [],
            selectedCourses: [],
            enrollments: [],
            newCourse: {
                name: '',
                description: '',
                credits: 0,
                start_date: ''
            },
            newStudent: {
                first_name: '',
                last_name: '',
                age: 0,
                is_active: true
            },
            newEnrollment: {
                selectedCourseIds: [],
                enrollmentDate: '',  
                enrollmentNotes: '',
                selectedStudent: null,
            }
        }
    },
    async mounted() {
        await Promise.all([
            this.fetchCourses(),
            this.fetchStudents()
        ])
    },
    methods: {
        async fetchCourses() {
            const response = await fetch(`${baseUrl}/api/courses/`);
            const data = await response.json();
            this.courses = data.courses;
        },
        async fetchStudents() {
            const response = await fetch(`${baseUrl}/api/students/`);
            const data = await response.json();
            this.students = data.students;
        },
        async fetchEnrollments() {
            if (!this.selectedStudent) return;
            const response = await fetch(`${baseUrl}/api/enrollments/?student_id=${this.selectedStudent.id}`);
            const data = await response.json();
            this.enrollments = data.enrollments;
        },
    
        async createCourse() {
            const response = await fetch(`${baseUrl}/api/courses/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.newCourse)
            });
            const newCourse = await response.json();
            this.courses.push(newCourse);
        },
        async deleteCourse(course) {
            if (confirm(`Are you sure you want to delete course '${course.name}'?`)) {
                const response = await fetch(`${baseUrl}${course.api}`, { method: 'DELETE' });
                if (response.ok) this.courses = this.courses.filter(c => c.id !== course.id);
            }
        },
        async createStudent() {
            const response = await fetch(`${baseUrl}/api/students/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.newStudent)
            });
            const newStudent = await response.json();
            this.students.push(newStudent);
        },
        async deleteStudent(student) {
            if (confirm(`Are you sure you want to delete student '${student.first_name} ${student.last_name}'?`)) {
                const response = await fetch(`${baseUrl}${student.api}`, { method: 'DELETE' });
                if (response.ok) this.students = this.students.filter(s => s.id !== student.id);
            }
        },
        async updateCourse() {
            if (!this.selectedCourse) return;

            const updatedData = {
            name: this.courseName,
            description: this.courseDescription,
            credits: this.courseCredits,
            start_date: this.courseStartDate,
            };

            try {
            const response = await fetch(`http://localhost:8000/api/courses/${this.selectedCourse.id}/`, {
                method: 'PUT',
                headers: {
                'Content-Type': 'application/json',
                },
                body: JSON.stringify(updatedData),
            });

            if (response.ok) {
                const data = await response.json();
                console.log('Course updated:', data);
                alert('Course updated successfully!');
                this.fetchCourses(); // Reload courses after update
            } else {
                const errorData = await response.json();
                alert(errorData.error || 'Failed to update the course');
            }
            } catch (error) {
            console.error('Error updating course:', error);
            alert('Error updating course');
            }
        },
        async updateStudent() {
            if (!this.selectedStudent) return;

            const updatedData = {
            first_name: this.studentFirstName,
            last_name: this.studentLastName,
            age: this.studentAge,
            is_active: this.studentIsActive,
            };

            try {
            const response = await fetch(`http://localhost:8000/api/students/${this.selectedStudent.id}/`, {
                method: 'PUT',
                headers: {
                'Content-Type': 'application/json',
                },
                body: JSON.stringify(updatedData),
            });

            if (response.ok) {
                const data = await response.json();
                console.log('Student updated:', data);
                alert('Student updated successfully!');
                this.fetchStudents(); // Reload students after update
            } else {
                const errorData = await response.json();
                alert(errorData.error || 'Failed to update the student');
            }
            } catch (error) {
            console.error('Error updating student:', error);
            alert('Error updating student');
            }
        }
    }
}
</script>

<style scoped>
</style>
