<template>
  <v-app>
    <v-app-bar color="primary" dark app>
      <v-toolbar-title color="white">InfoMap</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
    <v-footer color="primary" dark app class="justify-center">Vue_django_GoogleMapAPI</v-footer>
  </v-app>
</template>