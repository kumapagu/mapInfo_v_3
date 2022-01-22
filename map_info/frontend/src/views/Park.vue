<template>
    <div>
        <v-container>
            <h2 class="mb-5">{{ park.park_name }}</h2>
            <p>職種：{{ park.playset_slide }}</p>
            <p>内容：{{ park.playset_swing }}</p>
            <p>給料：{{ park.playset_sandbox }}円</p>
            <p>都道府県：{{ park.id }}</p>
            <p>市町村：{{ park.parking }}</p>
            <v-btn color="success" class="mr-2" :to="{ name: 'info', params: { id: park.id } }">編集</v-btn>
            <!-- <v-btn color="error" @click="deleteJobData">削除</v-btn> -->
        </v-container>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js"

export default {
    name: 'park',
    props: {
        id: {
            type: [ String, Number ]
        }
    },
    data() {
        return {
            park: {}
        }
    },
    methods: {
        setPageTitle(title) {
            document.title = title;
        },
        getParkData() {
            let endpoint = `/api/parks/${this.id}/`;
            apiService(endpoint).then(data => {
                this.park = data;
                this.setPageTitle(data.park_name);
            });
        },
        // deleteJobData() {
        //     let endpoint = `/api/jobs/${this.id}/`;
        //     apiService(endpoint, "DELETE").then(() => {
        //         this.$router.push({
        //             name: 'home'
        //         });
        //     });
        // }
    },
    created() {
        this.getParkData()
    }
}
</script>

<style>
    
</style>