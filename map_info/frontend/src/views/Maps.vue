<template>
  <div>
    <div id="map" class="map" ref="googleMap" />
    <v-btn @click="createInfo">情報を登録する</v-btn>
  </div>
</template>

<script>
import GoogleMapsApiLoader from 'google-maps-api-loader';
export default {
  name: 'Maps',
  props: {

  },
  data() {
    return {
      google: null,
      mapConfig: {
        center: {
          lat: 35.68944,
          lng: 139.69167
        },
        zoom: 17
      },
      marker: null,
      lat: null,
      lng: null,
    }
  },
  async mounted() {
    this.google = await GoogleMapsApiLoader({
      apiKey: process.env.VUE_APP_GOOGLE_API 
    });
    this.initializeMap();
  },
  methods: {
    initializeMap() {
      const map = new this.google.maps.Map(this.$refs.googleMap, this.mapConfig);
      map.addListener("click", (e) => {
        
        this.deleteMarker()
        this.placeMarkerAndPanTo(e.latLng, map);
        this.lat = e.latLng.lat()
        this.lng = e.latLng.lng()
        // console.log(this.lat)
        // console.log(this.lng)
      });
      
    },
    placeMarkerAndPanTo(latLng, map) {
      let marker = new this.google.maps.Marker({
        position: latLng,
        map: map,
      });
      this.marker = marker
    },
    deleteMarker() {
      if (this.marker){
        this.marker.setMap(null)
        this.maker = null
        this.lat = null
        this.lng = null
      }
    },
    createInfo(){
      this.$router.push({
        name: 'info',
        params: {
          lat: this.lat,
          lng: this.lng,
          name: 'Taro'
        }
      })
    }
    
    
  }
}
</script>

<style lang="scss" scoped>
.map {
  width: 100vw;
  height: 100vh;
}
</style>