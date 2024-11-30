<template>
    <div>
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>Course Name</th>
                    <th>Description</th>
                    <th>Credits</th>
                    <th>Start Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="course in courses" :key="course.id">
                    <td>
                        <!-- Show input if in edit mode, otherwise show text -->
                        <div v-if="course.showEditForm">
                            <input v-model="course.name" class="form-control" />
                        </div>
                        <div v-else>
                            {{ course.name }}
                        </div>
                    </td>
                    <td>
                        <div v-if="course.showEditForm">
                            <textarea v-model="course.description" class="form-control"></textarea>
                        </div>
                        <div v-else>
                            {{ course.description }}
                        </div>
                    </td>
                    <td>
                        <div v-if="course.showEditForm">
                            <input v-model="course.credits" type="number" class="form-control" />
                        </div>
                        <div v-else>
                            {{ course.credits }}
                        </div>
                    </td>
                    <td>
                        <div v-if="course.showEditForm">
                            <input v-model="course.start_date" type="date" class="form-control" />
                        </div>
                        <div v-else>
                            {{ course.start_date }}
                        </div>
                    </td>
                    <td>
                        <button 
                            class="btn btn-sm" 
                            @click="editCourse(course)" 
                            v-if="!course.showEditForm">
                            Edit
                        </button>
                        <button 
                            class="btn btn-success btn-sm" 
                            @click="saveCourse(course)" 
                            v-if="course.showEditForm">
                            Save
                        </button>
                        <button 
                            class="btn btn-danger btn-sm" 
                            @click="deleteCourse(course)">
                            Delete
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    props: {
        courses: {
            type: Array,
            required: true
        }
    },
    methods: {
        // toggle the edit form
        editCourse(course) {
            course.showEditForm = true;
        },

        // save the edited data
        async saveCourse(course) {
            const updatedCourse = {
                name: course.name,
                description: course.description,
                credits: course.credits,
                start_date: course.start_date
            };

            const response = await fetch(`http://localhost:8000/api/course/${course.id}/`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(updatedCourse)
            });

            if (response.ok) {
                const updatedData = await response.json();
                // Find and update the course in the list
                const index = this.courses.findIndex(c => c.id === updatedData.id);
                this.courses[index] = updatedData;
                course.showEditForm = false;  // Hide the edit form after save
                alert('Course updated successfully!');
            } else {
                alert('Failed to update the course.');
            }
        },

        // Delete course
        async deleteCourse(course) {
            if (confirm(`Are you sure you want to delete course '${course.name}'?`)) {
                const response = await fetch(`http://localhost:8000/api/course/${course.id}/`, { method: 'DELETE' });
                if (response.ok) {
                    this.courses = this.courses.filter(c => c.id !== course.id);
                    alert('Course deleted successfully!');
                } else {
                    alert('Failed to delete course.');
                }
            }
        }
    }
}
</script>

<style scoped>

</style>
