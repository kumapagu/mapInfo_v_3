<template>
  <div>
    <div id="map" class="map" ref="googleMap" />
    <v-btn @click="createInfo">情報を登録する</v-btn>
  </div>
</template>

<script>
import GoogleMapsApiLoader from 'google-maps-api-loader';
import { apiService } from "../common/api.service"
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
      parks: [],
      park: null
    }
  },
  async mounted() {
    this.google = await GoogleMapsApiLoader({
      apiKey: process.env.VUE_APP_GOOGLE_API 
    });
    // this.$nextTick(()=>{
    //   this.initializeMap()
    // })
    this.initializeMap();
  },
  methods: {
    initializeMap() {
      const map = new this.google.maps.Map(this.$refs.googleMap, this.mapConfig);
      this.setMarker(map)
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
    
    getParks() {
      let endpoint = "api/parks/"
      apiService(endpoint).then(data => {
          this.parks.push(...data.results)
      })  
    },
    setMarker(map) {
      for(this.park of this.parks){
        let latLng = new this.google.maps.LatLng(this.park.lat,this.park.lng)
        let marker = new this.google.maps.Marker({
        position: latLng,
        // map: map,
        });
        marker.setMap(map)
        // console.log(this.park.park_name)
      }
    },

    createInfo(){
      this.$router.push({
        name: 'info',
        params: {
          lat: this.lat,
          lng: this.lng,
        }
      })
    }    
  },
  created() {
        this.getParks()
        // console.log(this.parks)
  }
}
</script>

<style lang="scss" scoped>
.map {
  width: 80vw;
  height: 80vh;
}
</style>