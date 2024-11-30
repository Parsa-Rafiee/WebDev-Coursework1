<template>
    <div class="enrollment">
      <h3>Enrollments</h3>
  
      <!-- select a Student -->
      <div class="mb-3">
        <label for="studentSelect" class="form-label">Select Student</label>
        <select v-model="selectedStudent" @change="fetchEnrollments" class="form-select">
          <option v-for="student in students" :key="student.id" :value="student">
            {{ student.first_name }} {{ student.last_name }}
          </option>
        </select>
      </div>
  
        <!-- display Enrolled Courses -->
        <div v-if="enrollments.length">
        <h5>Enrolled courses</h5>
        <ul class="list-group mb-3">
            <li v-for="enrollment in enrollments" :key="enrollment.id" class="list-group-item">
                {{ enrollment.course }} 
            <button @click="removeEnrollment(enrollment)" class="btn btn-sm btn-danger float-end">
                Remove
            </button>
            </li>
        </ul>
        </div>
  
      <!-- Select Courses to Enroll -->
      <div class="mb-3">
        <label for="courseSelect" class="form-label">Select Courses to Enroll</label>
        <select v-model="selectedCourses" multiple class="form-select">
          <option v-for="course in courses" :key="course.id" :value="course">
            {{ course.name }}
          </option>
        </select>
      </div>
  
      <!-- Date Picker for Enrollment Date -->
      <div class="mb-3">
        <label for="enrollmentDate" class="form-label">Select Enrollment Date</label>
        <input type="date" v-model="enrollmentDate" class="form-control" />
      </div>
  
      <button @click="addEnrollments" class="btn btn-primary">Enroll in Selected Courses</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      students: Array,    
      courses: Array      
    },
    data() {
      return {
        selectedStudent: null,
        enrollments: [],
        selectedCourses: [],
        enrollmentDate: "" 
      };
    },
    methods: {
        async fetchEnrollments() {
    if (!this.selectedStudent) {
        console.error("No student selected.");
        return;
    }

    console.log("Fetching enrollments for student:", this.selectedStudent);

    try {
        const response = await fetch(`http://localhost:8000/api/enrollments/?student_id=${this.selectedStudent.id}`);

        const data = await response.json();
        console.log("Fetched enrollments:", data);

        if (data.enrollments) {
            this.enrollments = data.enrollments;
        } else {
            console.error("No enrollments");
        }
    } catch (error) {
        console.error("error fetching:", error);
    }
},
    async addEnrollments() {
        if (!this.selectedStudent || !this.selectedCourses.length || !this.enrollmentDate) return;
  
        // enrollment date is formatted correctly
        const formattedDate = this.enrollmentDate;
  
        const response = await fetch('http://localhost:8000/api/enrollments/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            student_id: this.selectedStudent.id,
            course_ids: this.selectedCourses.map(course => course.id),
            enrollment_date: formattedDate, 
            notes: ''
          })
        });
  
        if (response.ok) {
          this.fetchEnrollments(); 
          this.selectedCourses = [];
          this.enrollmentDate = "";  
        }
      },
      async removeEnrollment(enrollment) {
        const response = await fetch(`http://localhost:8000/api/enrollment/${enrollment.id}/`, {
          method: 'DELETE',
        });
        if (response.ok) {
          this.enrollments = this.enrollments.filter(e => e.id !== enrollment.id);
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .enrollment {
    margin-top: 20px;
  }
  </style>
  