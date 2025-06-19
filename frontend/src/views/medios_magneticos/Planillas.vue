<script setup>

import SubirArchivo from "@/components/SubirArchivo.vue";
import Toast from "primevue/toast";
</script>

<template>
  <div class="flex flex-col gap-4 w-full">
    <Toast />
     Seleccione o arrastre las planillas de seguridad social
    <SubirArchivo
        url="/medios_magneticos/planillas/"
        accept="application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        :multiple="true"
        name="archivo"
    />
  </div>
</template>

<style scoped>

</style>