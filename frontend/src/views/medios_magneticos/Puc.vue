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
          v-tooltip.bottom="'Descargar plantilla PUC'"
          severity="info"
          rounded
          aria-label="Descargar plantilla PUC"
        />
      </div>
    </div>
    <SubirArchivo
      url="/medios_magneticos/puc/"
      url_delete="/medios_magneticos/puc_borrado/"
      accept="text/csv"
      :multiple="false"
      name="archivo"
    />
  </div>
</template>

<style scoped>
</style>
