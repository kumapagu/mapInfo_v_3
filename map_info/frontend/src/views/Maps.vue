<template>
  <div class="parent">
    <div id="map" class="map" ref="googleMap" />
    <v-btn class="btn" x-large @click="createInfo">情報を登録する</v-btn>
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
        zoom: 17,
        mapTypeControl: false
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
        let infoContent = 
          `<h3>${this.park.park_name}</h3>` + 
          '<ul>' +
          `<li>ブランコ：${this.park.playset_swing}</li>` +
          `<li>すべり台：${this.park.playset_slide}</li>` +
          `<li>砂場：${this.park.playset_sandbox}</li>` +
          `<li>水道：${this.park.water_services}</li>` +
          `<li>自転車置場：${this.park.bicycle_parking}</li>` +
          `<li>駐車場：${this.park.parking}</li>` +
          `<li>自動販売機：${this.park.vending_machine}</li>` +
          '</ul>' +
          `<p>その他の情報：<br>${this.park.add_info}</p>` +
          `<a href='/park/${ this.park.id }'>編集</a>` +
          '<style>' +
          'h3 { text-align:center; }' +
          'ul { list-style:none; }' +
          '</style>'

        let infoWindow = new this.google.maps.InfoWindow({content: infoContent, maxWidth: 200})
        let latLng = new this.google.maps.LatLng(this.park.lat,this.park.lng)
        let marker = new this.google.maps.Marker({
        position: latLng,

        // map: map,
        });
        marker.setMap(map)

        marker.addListener("click", ()=>{
          infoWindow.open({
            anchor: marker,
            map,
            shouldFocus: false
          })
        })
        
      }
    },
    // setWindow() {
    //   let link = document.getElementById('link')
    //     console.log(link)
    //     link.addEventListener("click", ()=>{
    //       this.$router.push({
    //         name: 'info',
    //       })
    //     })
    // },

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
  },
  beforeRouteEnter(to, from, next) {
  next(vm => { vm.getParks(), vm.setMarker(); });
}
}
</script>

<style scoped>
.parent {
  position: relative;
}

.map {
  width: 100vw;
  height: 90vh;
  position: absolute;
  z-index: 1;
}

.btn {
  position: absolute;
  top: 20px;
  left: 25px;
  z-index: 5;
}
</style>