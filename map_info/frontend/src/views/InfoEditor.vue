<template>
<div>
  <h1>{{lat}}{{name}}</h1>
  
</div>
</template>

<script>
export default {
  name: 'info',
  props: {
      lat: Number,
      lng: Number,
      name: String
  },
  data() {
    return {
      
    }
  }

    
}

</script>