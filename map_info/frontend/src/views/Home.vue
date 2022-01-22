<template>
    <div>
        <v-container>
            <h1>Park Info</h1>
            <div v-for="park in parks" :key="park.pk">
                <p>{{ park.park_name }}</p>
                <p><img src="park.image"></p>
            </div>
        </v-container>
        <router-link
        :to="{name: 'info'}"
        class="job-link"
        >情報
        </router-link>
        <a href="http://127.0.0.1:8000/maps">aタグ</a>
        <v-btn to="maps">map</v-btn>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js"
export default {
    name: "home",
    data() {
        return {
            parks: []
        }
    },
    methods: {
        getParks() {
            let endpoint = "api/parks/"
            apiService(endpoint).then(data => {
                this.parks.push(...data.results)
            })  
        }
    },
    created() {
        this.getParks()
        console.log(this.parks)
    }
}
</script>