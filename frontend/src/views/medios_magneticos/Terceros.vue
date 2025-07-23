<script setup>
import SubirArchivo from "@/components/SubirArchivo.vue";
import Toast from "primevue/toast";
</script>

<template>
  <div class="flex flex-col gap-4 w-full">
     <Toast />
     Seleccione o arrastre el modelo de terceros
     <SubirArchivo
        url="/medios_magneticos/terceros_nacionales/"
        url_delete="/medios_magneticos/terceros_nacionales_borrado/"
        accept="text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        :multiple="false"
        name="archivo"
     />
  </div>
</template>

<style scoped>

</style>