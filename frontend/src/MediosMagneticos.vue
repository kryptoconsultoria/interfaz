<script setup>
import { ref, computed } from 'vue';
import Puc from './views/medios_magneticos/Puc.vue';
import DocumentosPDF from './views/medios_magneticos/DocumentosPDF.vue';
import Terceros from './views/medios_magneticos/Terceros.vue';
import Balances from './views/medios_magneticos/Balances.vue';
import AnexosRenta from './views/medios_magneticos/AnexosRenta.vue';
import Planillas from './views/medios_magneticos/Planillas.vue';
import Iniciar from './views/medios_magneticos/Iniciar.vue';
import SeleccionSistema from "@/views/medios_magneticos/SeleccionSistema.vue";

const seleccion = ref(null);

function manejarSeleccion(data) {
  seleccion.value = data;
  fetch("/medios_magneticos/guardar_seleccion/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
}

function validarSeleccion(activateCallback, pasoDestino) {
  if (seleccionCompleta.value) {
    activateCallback(pasoDestino);
  }
}

const seleccionCompleta = computed(() =>
  seleccion.value &&
  seleccion.value.sistema &&
  seleccion.value.cliente
);

const pasos = [
  { valor: "1", nombre: "Seleccionar Sistema" },
  { valor: "2", nombre: "PUC" },
  { valor: "3", nombre: "Documentos PDF" },
  { valor: "4", nombre: "Terceros" },
  { valor: "5", nombre: "Balances" },
  { valor: "6", nombre: "Anexos de Renta" },
  { valor: "7", nombre: "Planillas" },
  { valor: "8", nombre: "Iniciar" },
];
</script>

<template>
  <Stepper value="1">
    <StepList>
      <Step :value="pasos[0].valor">{{ pasos[0].nombre }}</Step>
      <Step
        v-for="step in pasos.slice(1)"
        :key="step.valor"
        :value="step.valor"
        :disabled="!seleccionCompleta"
      >
        {{ step.nombre }}
      </Step>
    </StepList>

    <StepPanels>
      <StepPanel v-slot="{ activateCallback }" value="1">
        <div class="flex flex-col h-full">
          <div class="border border-gray-300 rounded-md p-4 bg-white shadow-md">
            <SeleccionSistema @update-seleccion="manejarSeleccion" />
          </div>
        </div>
        <div class="flex pt-6 justify-end">
          <Button
            label="Siguiente"
            icon="pi pi-arrow-right"
            iconPos="right"
            :disabled="!seleccionCompleta"
            @click="() => validarSeleccion(activateCallback, '2')"
          />
        </div>
      </StepPanel>

      <StepPanel v-slot="{ activateCallback }" value="2">
        <div class="flex flex-col h-full">
          <div class="border border-gray-300 rounded-md p-4 bg-white shadow-md">
            <Puc />
          </div>
        </div>
        <div class="flex pt-6 justify-between">
          <Button label="Atrás" severity="secondary" icon="pi pi-arrow-left" @click="activateCallback('1')" />
          <Button label="Siguiente" icon="pi pi-arrow-right" iconPos="right" @click="() => validarSeleccion(activateCallback, '3')" />
        </div>
      </StepPanel>

      <StepPanel v-slot="{ activateCallback }" value="3">
        <div class="flex flex-col h-full">
          <div class="border border-gray-300 rounded-md p-4 bg-white shadow-md">
            <DocumentosPDF />
          </div>
        </div>
        <div class="flex pt-6 justify-between">
          <Button label="Atrás" severity="secondary" icon="pi pi-arrow-left" @click="activateCallback('2')" />
          <Button label="Siguiente" icon="pi pi-arrow-right" iconPos="right" @click="() => validarSeleccion(activateCallback, '4')" />
        </div>
      </StepPanel>

      <StepPanel v-slot="{ activateCallback }" value="4">
        <div class="flex flex-col h-full">
          <div class="border border-gray-300 rounded-md p-4 bg-white shadow-md">
            <Terceros />
          </div>
        </div>
        <div class="flex pt-6 justify-between">
          <Button label="Atrás" severity="secondary" icon="pi pi-arrow-left" @click="activateCallback('3')" />
          <Button label="Siguiente" icon="pi pi-arrow-right" iconPos="right" @click="() => validarSeleccion(activateCallback, '5')" />
        </div>
      </StepPanel>

      <StepPanel v-slot="{ activateCallback }" value="5">
        <div class="flex flex-col h-full">
          <div class="border border-gray-300 rounded-md p-4 bg-white shadow-md">
            <Balances />
          </div>
        </div>
        <div class="flex pt-6 justify-between">
          <Button label="Atrás" severity="secondary" icon="pi pi-arrow-left" @click="activateCallback('4')" />
          <Button label="Siguiente" icon="pi pi-arrow-right" iconPos="right" @click="() => validarSeleccion(activateCallback, '6')" />
        </div>
      </StepPanel>

      <StepPanel v-slot="{ activateCallback }" value="6">
        <div class="flex flex-col h-full">
          <div class="border border-gray-300 rounded-md p-4 bg-white shadow-md">
            <AnexosRenta />
          </div>
        </div>
        <div class="flex pt-6 justify-between">
          <Button label="Atrás" severity="secondary" icon="pi pi-arrow-left" @click="activateCallback('5')" />
          <Button label="Siguiente" icon="pi pi-arrow-right" iconPos="right" @click="() => validarSeleccion(activateCallback, '7')" />
        </div>
      </StepPanel>

      <StepPanel v-slot="{ activateCallback }" value="7">
        <div class="flex flex-col h-full">
          <div class="border border-gray-300 rounded-md p-4 bg-white shadow-md">
            <Planillas />
          </div>
        </div>
        <div class="flex pt-6 justify-between">
          <Button label="Atrás" severity="secondary" icon="pi pi-arrow-left" @click="activateCallback('6')" />
          <Button label="Siguiente" icon="pi pi-arrow-right" iconPos="right" @click="() => validarSeleccion(activateCallback, '8')" />
        </div>
      </StepPanel>

      <StepPanel v-slot="{ activateCallback }" value="8">
        <div class="flex flex-col h-full">
          <div class="border border-gray-300 rounded-md p-4 bg-white shadow-md">
            <Iniciar />
          </div>
        </div>
        <div class="pt-6">
          <Button label="Atrás" severity="secondary" icon="pi pi-arrow-left" @click="activateCallback('7')" />
        </div>
      </StepPanel>
    </StepPanels>
  </Stepper>
</template>

<style scoped>
/* Puedes agregar estilos adicionales aquí si lo deseas */
</style>
