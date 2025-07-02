<script>
export default {
  name: "IniciarAutomatizacion",
  data() {
    return {
      cargando: false,
      robot: "",
      historiaUsuario: "",
      estado: "",
      detalleError: "",
      error: "",
      intervalo: null,
      mostrarCard: false // Nuevo control para mostrar la tarjeta
    };
  },
  methods: {
    async iniciarAutomatizacion() {
      this.cargando = true;
      this.error = "";
      this.mostrarCard = false;

      try {
        // Inicia la tarea y recibe jobId
        const resp0 = await fetch("/medios_magneticos/iniciar_automatizacion/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": this.obtenerTokenCSRF()
          }
        });
        if (!resp0.ok) throw new Error(`HTTP ${resp0.status}`);
        const { jobId } = await resp0.json();

        // Función de polling con setTimeout
        const pollStatus = async () => {
          const resp1 = await fetch(`/medios_magneticos/estado/${jobId}/`);
          if (!resp1.ok) throw new Error(`HTTP ${resp1.status}`);
          const r = await resp1.json();

          if (r.status === "pending") {
            // Tarea no lista, esperamos unos segundos
            setTimeout(pollStatus, 5000);
          } else {
            // Tarea completada: procesamos resultado
            if (r.success) {
              const info = r.data;
              this.robot = info.Tarea;
              this.estado = info.Estado;
              this.historiaUsuario = info.HistoriaUsuario || "";
              this.detalleError = info.ErrorDetalle || "";
              this.error = "";
            } else {
              this.error = r.message || "Error en la automatización.";
            }
            this.cargando = false;
            this.mostrarCard = true;
          }
        };

        // Inicia el polling
        pollStatus();

      } catch (err) {
        this.error = "Error de red o servidor: " + err.message;
        this.cargando = false;
        this.mostrarCard = true;
      }
    },
    obtenerTokenCSRF() {
      const match = document.cookie.match(/csrftoken=([^;]+)/);
      return match ? match[1] : "";
    }
   },
  };
</script>

<template>
  <div class="flex flex-col gap-4 w-full">
    <!-- Botón centrado -->
    <div class="flex justify-center">
      <Button
        label="Iniciar automatización"
        icon="pi pi-check"
        size="large"
        :disabled="cargando"
        @click="iniciarAutomatizacion"
      />
    </div>

    <!-- Barra de progreso a todo lo ancho -->
    <ProgressBar
      v-if="cargando"
      mode="indeterminate"
      style="height: 6px;"
      class="w-full"
    />

    <!-- Tarjeta con información, solo visible después de iniciar automatización -->
    <Card
      v-if="mostrarCard"
      class="border-2 border-dashed border-surface-200 dark:border-surface-700 rounded bg-surface-50 dark:bg-surface-950 flex-auto flex justify-center font-medium"
    >
      <template #title>
        <span class="font-bold text-lg">Estado de la automatización</span>
      </template>
      <template #content>
        <ul class="list-disc list-inside text-sm text-gray-700" v-if="!error">
          <li><strong>Robot:</strong> {{ robot }}</li>
          <li><strong>Historia de usuario:</strong> {{ historiaUsuario }}</li>
          <li><strong>Estado:</strong> {{ estado }}</li>
          <li><strong>Detalle del error:</strong> {{ detalleError }}</li>
        </ul>
        <p class="text-red-500 text-sm" v-else>{{ error }}</p>
      </template>
    </Card>
  </div>
</template>

<style scoped>
.barra-carga {
  margin-top: 10px;
}
.error {
  color: red;
}
</style>