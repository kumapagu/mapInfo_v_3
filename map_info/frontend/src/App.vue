<template>
  <v-app>
    <v-app-bar color="primary" dark app>
      <v-toolbar-title class="ml-6 text-h4"><v-btn class="text-h4" style="text-transform:none"  text href="/">MapInfo</v-btn></v-toolbar-title>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
    <v-footer color="primary" dark app class="justify-center">Vue_django_GoogleMapAPI</v-footer>
  </v-app>
</template>