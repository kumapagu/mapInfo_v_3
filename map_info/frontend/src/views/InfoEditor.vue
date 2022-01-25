<template>
  <form @submit.prevent="onSubmit">
    <v-btn text class="ml-5 mt-3" color="primary" href="/">マップへ戻る</v-btn>
    <v-container>
      <v-row  class="mx-auto">
        <v-col cols="10">
          <v-text-field v-model="park_name" label="公園名" required></v-text-field>
        </v-col>
        
        <v-col cols="4">
          ブランコ:
          <!-- <v-radio-group v-model="info.playset_swing" row>
            <v-radio label="有り" value="有り"></v-radio>
            <v-radio label="無し" value="無し"></v-radio>
          </v-radio-group> -->
          <input type="radio" value="有り" v-model="playset_swing"> 有り
          <input type="radio" value="無し" v-model="playset_swing"> 無し
        </v-col>
        <v-col cols="4">
          すべり台:
          <input type="radio" value="有り" v-model="playset_slide"> 有り
          <input type="radio" value="無し" v-model="playset_slide"> 無し
        </v-col>
        <v-col cols="4">
          砂場:
          <input type="radio" value="有り" v-model="playset_sandbox"> 有り
          <input type="radio" value="無し" v-model="playset_sandbox"> 無し
        </v-col>
        <v-col cols="4">
          自動販売機:
          <input type="radio" value="有り" v-model="vending_machine"> 有り
          <input type="radio" value="無し" v-model="vending_machine"> 無し
        </v-col>
        <v-col cols="4">
          水道:
          <input type="radio" value="有り" v-model="water_services"> 有り
          <input type="radio" value="無し" v-model="water_services"> 無し
        </v-col>
        <v-col cols="4">
          駐輪場:
          <input type="radio" value="有り" v-model="bicycle_parking"> 有り
          <input type="radio" value="無し" v-model="bicycle_parking"> 無し
        </v-col>
        <v-col cols="4">
          駐車場:
          <input type="radio" value="有り" v-model="parking"> 有り
          <input type="radio" value="無し" v-model="parking"> 無し
        </v-col>
        <v-col cols="10">
          <v-textarea solo label="その他の情報" v-model="add_info"></v-textarea>
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
    id: {Number, required: false},
    lat: Number,
    lng: Number,
  },
  data() {
    return {
      park_name: '',
      playset_swing: '無し',
      playset_slide: '無し',
      playset_sandbox: '無し',
      vending_machine: '無し',
      water_services: '無し',
      bicycle_parking: '無し',
      parking: '無し',
      add_info: '',
      d_lat: this.lat,
      d_lng: this.lng,
      isDisplay: true
      
    }
  },
  async beforeRouteEnter (to, from, next) {
    console.log('test')
      if (to.params.id !== undefined) {
        let endpoint = `/api/parks/${ to.params.id }/`;
        let data = await apiService(endpoint);
        return next(vm => {
            (vm.park_name = data.park_name),
            (vm.playset_swing = data.playset_swing),
            (vm.playset_slide = data.playset_slide),
            (vm.playset_sandbox = data.playset_sandbox),
            (vm.vending_machine = data.vending_machine),
            (vm.water_services = data.water_services),
            (vm.bicycle_parking = data.bicycle_parking),
            (vm.parking = data.parking),
            (vm.add_info = data.add_info),
            (vm.d_lat = data.lat),
            (vm.d_lng = data.lng)
        });
      } else {
          return next();
      }
    },
  methods: {
    onSubmit() {
      let endpoint = "/api/parks/"
      let method = "POST"
      if (this.id !== undefined) {
          endpoint += `${this.id}/`;
          method = "PUT";
      }
      apiService(endpoint, method, {
        park_name: this.park_name,
        playset_swing: this.playset_swing,
        playset_slide: this.playset_slide,
        playset_sandbox: this.playset_sandbox,
        vending_machine: this.vending_machine,
        water_services: this.water_services,
        bicycle_parking: this.bicycle_parking,
        parking: this.parking,
        add_info: this.add_info,
        lat: this.d_lat,
        lng: this.d_lng,
      }).then(park_data => {
        this.$router.go({
          path: this.$router.currentRoute.path,
          force: true
        })
        console.log(park_data)
      })
    },
    created() {
      document.title = "Editor - park";
    }
  }

    
}

</script>