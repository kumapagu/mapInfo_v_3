<template>
  <v-container>
    <div class="container">
      <div class="park-info">
        <h2 class="mb-5">{{ park.park_name }}</h2>
        <p>ブランコ：{{ park.playset_swing }}</p>
        <p>すべり台：{{ park.playset_slide }}</p>
        <p>砂場：{{ park.playset_sandbox }}</p>
        <p>水道：{{ park.water_services }}</p>
        <p>自転車置き場：{{ park.bicycle_parking }}</p>
        <p>駐車場：{{ park.parking }}</p>
        <p>自動販売機：{{ park.vending_machine }}</p>
        <p>その他の情報：{{ park.add_info }}</p>
      </div>
      <div class="spacer"></div>
      <div class="park-image">
        <img :src="park.image">
      </div>
    </div>
    <v-btn color="primary" class="mr-2" :to="{ name: 'info', params: { id: park.id } }">編集</v-btn>
    <v-btn color="primary" class="mr-2" href="/">マップへ戻る</v-btn>
    <v-btn color="error" @click="deleteParkData" href="/">削除</v-btn>
  </v-container>
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
    park: {},
    lat: null,
    lng: null
    }
  },
  methods: {
    setPageTitle(title) {
      document.title = title
    },
    getParkData() {
      let endpoint = `/api/parks/${this.id}/`
      apiService(endpoint).then(data => {
      this.park = data
      this.setPageTitle(data.park_name)
      this.lat = data.lat
      this.lng = data.lng
      this.setSession()
      })
    },
    setSession(){
      sessionStorage.setItem('lat', this.lat)
      sessionStorage.setItem('lng', this.lng)
    },
    deleteParkData() {
      let endpoint = `/api/parks/${this.id}/`
      apiService(endpoint, "DELETE")
    },
  },
  created() {
    this.getParkData()
  },

}
</script>

<style scoped>
  .container {
      display: flex;
      flex-wrap: wrap;
  }

  img {
      width: 80vh;
  }
</style>