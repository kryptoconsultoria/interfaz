<script setup>
import SubirArchivo from "@/components/SubirArchivo.vue";
</script>

<template>
  <div class="flex flex-col gap-4 w-full">
      Seleccione o arrastre las retenciones en la fuente
       <SubirArchivo
        url="/medios_magneticos/retenciones_fuente/"
        accept="application/pdf"
        :multiple="true"
        name="archivos[]"
       />
      Seleccione o arrastre los certificados de ingresos y retenciones
       <SubirArchivo
        url="/medios_magneticos/ingresos_retenciones/"
        accept="application/pdf"
        :multiple="true"
        name="archivos[]"
       />
      Seleccione o arrastre los certificados de participacion accionaria
      <SubirArchivo
        url="/medios_magneticos/participacion_accionaria/"
        accept="application/pdf"
        :multiple="true"
        name="archivos[]"
      />
  </div>
</template>

<style scoped>

</style>