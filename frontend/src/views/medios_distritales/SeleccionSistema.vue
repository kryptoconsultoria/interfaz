<script setup>
import { ref } from 'vue';
import SeleccionSistema from "@/components/SeleccionSistema.vue";

const seleccion = ref(null);

function manejarSeleccion(data) {
  seleccion.value = data;
  // Enviar selección al backend
  fetch("/medios_magneticos/guardar_seleccion/", {
      method: "POST",
      headers: {
          "Content-Type": "application/json"
      },
      body: JSON.stringify({
          sistema: data.sistema,
          cliente: data.cliente
      })
  })
  .then(async res => {
      const contentType = res.headers.get("content-type");
      if (!res.ok) {
          throw new Error(`HTTP ${res.status}`);
      }
      if (!contentType || !contentType.includes("application/json")) {
          const text = await res.text();
          throw new Error(`Respuesta no JSON: ${text.slice(0, 100)}`);
      }
      return res.json();
  })
  .then(res => {
      if (!res.success) {
          console.error("Error al guardar en sesión:", res.message);
      }
  })
  .catch(err => {
      console.error("Fallo de red o formato:", err);
  });
}
</script>
<template>
      <SeleccionSistema @update-seleccion="manejarSeleccion"/>
</template>

<style scoped>

</style>