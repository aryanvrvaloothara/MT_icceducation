const app = new Vue({
    el: "#app",
    data: {
      jobs: [],
    },
    methods: {
        applyJob(id) {
            fetch("http://localhost:8000/apply/" + id, {
                method: "POST"
            })
            .then(response => response.json())
            .then(() => {
                console.log("APPLIED!!!")
            })
        }
    },
    mounted(){
        fetch("http://localhost:8000/jobs/")
        .then(response => response.json())
        .then((data) => {
            this.jobs = data;
        })
    },
    template: `
      <div>
        <ul>
          <li v-for="job in jobs">
            <h2>{{job.title}}</h2>
            <h6>Experience :</h6> <p>{{job.experience}}</p>
            <h6>Description</h6>
            <p>{{job.description}}</p>
            <h6>No. of Vacencies: </h6>{{job.no_of_vacancies}}
            <button v-on:click="applyJob(job.id)">Apply</button>
          </li>
        </ul>
      </div>
    `,
  })





const crud = new Vue({
    el: "#crud",
    data: {
      editJob: null,
      jobs: [],
    },
    methods: {
        deleteJob(id, i) {
            fetch("http://localhost:8000/jobs/" + id, {
                method: "DELETE"
            })
            .then(() => {
                this.jobs.splice(i, 1);
            })
        },
        updateJob(job){
            fetch("http://localhost:8000/jobs/" + job.id, {
                body: JSON.stringify(job),
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
            })
            .then(() => {
                this.editJob = null;
            })
        }
    },
    mounted(){
        fetch("http://localhost:8000/jobs/")
        .then(response => response.json())
        .then((data) => {
            this.jobs = data;
        })
    },
    template: `
      <div>
        <ul>
          <li v-for="job, i in jobs">
            <div v-if="editJob === job.id ">
                <input v-model="job.title">
                <input v-model="job.experience">
                <input v-model="job.description">
                <input v-model="job.no_of_vacancies">
                <button v-on:click="updateJob(job)">save</button>
            </div>

            <div v-else>

               <h2>{{job.title}}</h2>
               <h6>Experience :</h6> <p>{{job.experience}}</p>
               <h6>Description</h6>
               <p>{{job.description}}</p>
               <h6>No. of Vacencies: </h6>{{job.no_of_vacancies}}
               <button v-on:click="editJob = job.id">Edit</button>
               <button v-on:click="deleteJob(job.id, i)">Delete</button>
            </div>

          </li>
        </ul>
      </div>
    `,
  })
