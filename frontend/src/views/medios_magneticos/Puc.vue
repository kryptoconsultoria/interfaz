<script setup>
import SubirArchivo from '../../components/SubirArchivo.vue';
</script>

<template>
  <div class="flex flex-col gap-4 w-full">
      Seleccione o arrastre el plan unico de cuentas
      <SubirArchivo
          url="/medios_magneticos/puc/"
          accept="text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
          :multiple="false"
          name="archivo"
      />
  </div>
</template>

<style scoped>

</style>