<script setup>
import SubirArchivo from "@/components/SubirArchivo.vue";
import Toast from 'primevue/toast'; // ✅ Componente visual
</script>

<template>
    <!-- Este componente es necesario para que useToast() funcione -->
  <div class="flex flex-col gap-4 w-full">
      <Toast />
      Seleccione o arrastre las retenciones en la fuente
       <SubirArchivo
        url="/medios_magneticos/retenciones_fuente/"
        url_delete="/medios_magneticos/retenciones_fuente_borrado/"
        accept="application/pdf"
        :multiple="true"
        name="archivo"
       />
      Seleccione o arrastre los certificados de ingresos y retenciones
       <SubirArchivo
        url="/medios_magneticos/ingresos_retenciones/"
        url_delete="/medios_magneticos/ingresos_retenciones_borrado/"
        accept="application/pdf"
        :multiple="true"
        name="archivo"
       />
      Seleccione o arrastre los certificados de participacion accionaria
      <SubirArchivo
        url="/medios_magneticos/participacion_accionaria/"
        url_delete="/medios_magneticos/participacion_accionaria_borrado/"
        accept="application/pdf"
        :multiple="true"
        name="archivo"
      />
  </div>
</template>

<style scoped>

</style>