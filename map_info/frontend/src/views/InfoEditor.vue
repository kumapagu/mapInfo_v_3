<template>
  <form @submit.prevent="onSubmit">
    <v-container>
      <v-row  justify="center">
        <v-col cols="10">
          <v-text-field v-model="info.park_name" label="公園名" required></v-text-field>
        </v-col>
        
        <v-col cols="4">
          ブランコ:
          <!-- <v-radio-group v-model="info.playset_swing" row>
            <v-radio label="有り" value="有り"></v-radio>
            <v-radio label="無し" value="無し"></v-radio>
          </v-radio-group> -->
          <input type="radio" value="有り" v-model="info.playset_swing"> 有り
          <input type="radio" value="無し" v-model="info.playset_swing"> 無し
        </v-col>
        <v-col cols="4">
          すべり台:
          <input type="radio" value="有り" v-model="info.playset_slide"> 有り
          <input type="radio" value="無し" v-model="info.playset_slide"> 無し
        </v-col>
        <v-col cols="4">
          砂場:
          <input type="radio" value="有り" v-model="info.playset_sandbox"> 有り
          <input type="radio" value="無し" v-model="info.playset_sandbox"> 無し
        </v-col>
        <v-col cols="4">
          自動販売機:
          <input type="radio" value="有り" v-model="info.vending_machine"> 有り
          <input type="radio" value="無し" v-model="info.vending_machine"> 無し
        </v-col>
        <v-col cols="4">
          水道:
          <input type="radio" value="有り" v-model="info.water_services"> 有り
          <input type="radio" value="無し" v-model="info.water_services"> 無し
        </v-col>
        <v-col cols="4">
          駐輪場:
          <input type="radio" value="有り" v-model="info.bicycle_parking"> 有り
          <input type="radio" value="無し" v-model="info.bicycle_parking"> 無し
        </v-col>
        <v-col cols="4">
          駐車場:
          <input type="radio" value="有り" v-model="info.parking"> 有り
          <input type="radio" value="無し" v-model="info.parking"> 無し
        </v-col>
        <v-col cols="10">
          <v-textarea solo label="その他の情報" v-model="info.add_info"></v-textarea>
        </v-col>
        
      </v-row>
      <v-btn color="primary" type="submit">情報を登録</v-btn>
    </v-container>
  </form>

</template>

<script>
import { apiService } from "../common/api.service"

export default {
  name: 'info',
  props: {
      lat: Number,
      lng: Number,
  },
  data() {
    return {
      info: {
        park_name: '',
        playset_swing: '無し',
        playset_slide: '無し',
        playset_sandbox: '無し',
        vending_machine: '無し',
        water_services: '無し',
        bicycle_parking: '無し',
        parking: '無し',
        add_info: '',
      },
      
    }
  },
  methods: {
    onSubmit() {
      let endpoint = "/api/parks/"
      let method = "POST"
      apiService(endpoint, method, {
        park_name: this.info.park_name,
        playset_swing: this.info.playset_swing,
        playset_slide: this.info.playset_slide,
        playset_sandbox: this.info.playset_sandbox,
        vending_machine: this.info.vending_machine,
        water_services: this.info.water_services,
        bicycle_parking: this.info.bicycle_parking,
        parking: this.info.parking,
        add_info: this.info.add_info,
        lat: this.lat,
        lng: this.lng,
      }).then(park_data => {
        this.$router.push({
          name: 'maps'
        })
        console.log(park_data)
      })
    }
  }

    
}

</script>