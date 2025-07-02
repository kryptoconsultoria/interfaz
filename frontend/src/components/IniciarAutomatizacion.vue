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

      const MAX_RETRIES = 2;
      const TIMEOUT_MS = 8000;

      const fetchWithTimeout = async (url, options = {}) => {
        try {
          const controller = new AbortController();
          const timeoutId = setTimeout(() => controller.abort(), TIMEOUT_MS);
          const res = await fetch(url, {
            ...options,
            signal: controller.signal
          });
          clearTimeout(timeoutId);
          if (!res.ok) {
            throw new Error(`HTTP ${res.status}`);
          }
          return res;
        } catch (err) {
          if (err.name === "AbortError") {
            throw new Error("Request timed out");
          }
          throw err;
        }
      };

      const runWithRetries = async () => {
        for (let attempt = 0; attempt <= MAX_RETRIES; attempt++) {
          try {
            return await fetchWithTimeout("/medios_magneticos/iniciar_automatizacion/", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": this.obtenerTokenCSRF()
              }
            });
          } catch (err) {
            if (attempt === MAX_RETRIES) throw err;
            const delay = 2 ** attempt * 1000;
            await new Promise(r => setTimeout(r, delay));
          }
        }
      };

      try {
        const respuesta = await runWithRetries();
        const resp = await respuesta.json();

        if (resp.success) {
          const info = resp.data;
          this.robot = info.Tarea;
          this.estado = info.Estado;
          this.historiaUsuario = info.HistoriaUsuario || "";
          this.detalleError = info.ErrorDetalle || "";
          this.error = "";
        } else {
          this.error = resp.message || "Error al iniciar la automatización.";
        }

      } catch (err) {
        this.error = "Error de red/servidor: " + err.message;
      } finally {
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