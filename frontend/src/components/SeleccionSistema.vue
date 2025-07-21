<script setup>
import { ref, computed, onMounted, watch } from 'vue';

const emit = defineEmits(['update-seleccion']);  // Evento personalizado

const selectedSistema = ref(null);
const selectedCliente = ref(null);
const sistemas = ref([]);
const clientes = ref([]);

// Computar clientes según sistema seleccionado
const clientesFiltrados = computed(() => {
  if (!selectedSistema.value) return [];
  return clientes.value.filter(cliente => cliente.idsistema === selectedSistema.value.idsistema);
});

// Cargar datos del backend
onMounted(() => {
  const data = window.__INITIAL_DATA__ || {};
  sistemas.value = data.sistemas || [];
  clientes.value = data.clientes || [];
});

// Emitir sistema + cliente cada vez que ambos estén seleccionados
watch([selectedSistema, selectedCliente], ([sistema, cliente]) => {
  if (sistema && cliente) {
    emit('update-seleccion', { sistema, cliente });
  }
});
</script>

<template>
    <div class="flex flex-col gap-4 w-full">
    <!-- Combo de Sistemas -->
    <Select
      v-model="selectedSistema"
      :options="sistemas"
      optionLabel="nombre"
      placeholder="Seleccione un Sistema Contable"
      class="w-full"
    />
    <!-- Combo de Clientes filtrados -->
    <Select
      v-model="selectedCliente"
      :options="clientesFiltrados"
      optionLabel="nombre"
      placeholder="Seleccione un Cliente"
      class="w-full"
      :disabled="!selectedSistema"
    />
  </div>
</template>

<style scoped>
</style>
