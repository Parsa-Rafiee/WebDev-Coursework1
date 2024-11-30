<template>
  <div>
      <table class="table table-bordered">
          <thead>
              <tr>
                  <th>First Name</th>
                  <th>Last Name</th>
                  <th>Age</th>
                  <th>Is Active</th>
                  <th>Actions</th>
              </tr>
          </thead>
          <tbody>
              <tr v-for="student in students" :key="student.id">
                  <td>{{ student.first_name }}</td>
                  <td>{{ student.last_name }}</td>
                  <td>{{ student.age }}</td>
                  <td>
                      <span v-if="student.is_active">Yes</span>
                      <span v-else>No</span>
                  </td>
                  <td>
                      <button class="btn btn-danger btn-sm" @click="$emit('delete-student', student)">
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
      students: {
          type: Array,
          required: true
      }
  }
}
</script>

<style scoped>
.table {
  margin-top: 1em;
}
</style>
