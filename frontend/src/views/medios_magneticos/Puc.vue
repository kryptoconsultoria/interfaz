<script setup>
import SubirArchivo from '../../components/SubirArchivo.vue';
</script>

<template>
  <div class="flex flex-col gap-4 w-full">
    <div class="flex justify-between items-center w-full">
      <span>Seleccione o arrastre el plan único de cuentas</span>
      <div class="flex gap-x-2">
        <Button
          icon="pi pi-download"
          severity="info"
          rounded
          aria-label="Descargar excel auxiliar 1"
        />
      </div>
    </div>
    <SubirArchivo
      url="/medios_magneticos/puc/"
      accept="text/csv"
      :multiple="false"
      name="archivo"
    />
  </div>
</template>

<style scoped>
</style>
