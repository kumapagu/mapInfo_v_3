<template>
    <div>
        <v-container>
            <h1>Park Info</h1>
            <div v-for="park in parks" :key="park.pk">
                <p>{{ park.park_name }}</p>
                <p><img src="park.image"></p>
            </div>
        </v-container>
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