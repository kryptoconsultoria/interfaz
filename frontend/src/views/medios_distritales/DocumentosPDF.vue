<script setup>
import SubirArchivo from "@/components/SubirArchivo.vue";
import Toast from 'primevue/toast'; // ✅ Componente visual
</script>

<template>
    <!-- Este componente es necesario para que useToast() funcione -->
  <div class="flex flex-col gap-4 w-full">
      <Toast />
      Seleccione o arrastre los archivos rete ica
       <SubirArchivo
        url="/medios_distritales/rete_ica/"
        url_delete="/medios_distritales/rete_ica_borrado/"
        accept="application/pdf"
        :multiple="true"
        name="archivo"
       />
      Seleccione o arrastre los archivos rete ica por tercero
       <SubirArchivo
        url="/medios_distritales/rete_ica_terceros/"
        url_delete="/medios_distritales/rete_ica_terceros_borrado/"
        accept="application/pdf"
        :multiple="true"
        name="archivo"
       />
  </div>
</template>

<style scoped>

</style>