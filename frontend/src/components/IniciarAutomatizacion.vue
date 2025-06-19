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
      this.mostrarCard = false; // Oculta la tarjeta antes de iniciar

      try {
        const respuesta = await fetch("/medios_magneticos/iniciar_automatizacion/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": this.obtenerTokenCSRF()
          }
        });
        const data = await respuesta.json();
        console.log(data);

        if (data.estado === "exitoso") {
          this.mostrarCard = true;
          this.iniciarPolling(); // Solo inicia polling si la automatización fue exitosa
        } else {
          this.error = data.message || "Error al iniciar la automatización.";
          this.mostrarCard = true;
          this.detenerPolling();
        }
      } catch (err) {
        this.error = "Error de red o servidor: " + err;
        this.mostrarCard = true;
        this.detenerPolling();
      } finally {
        this.cargando = false;
      }
    },
    conectarWebSocket() {
      this.socket = new WebSocket("ws://localhost:8000/ws/estado/");

      this.socket.onopen = () => {
        this.conectado = true;
        console.log("Conectado al WebSocket");
      };

      this.socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        this.robot = data.robot;
        this.estado = data.estado;
        this.detalle = data.detalle;

        // Detener conexión si el estado es "finalizado"
        if (
          this.robot === "subir_insumos.robot" &&
          this.estado.toLowerCase() === "finalizado"
        ) {
          this.socket.close();
        }
      };

        this.socket.onclose = () => {
          this.conectado = false;
          console.log("WebSocket cerrado");
        };
      }
    },
    obtenerTokenCSRF() {
      const match = document.cookie.match(/csrftoken=([^;]+)/);
      return match ? match[1] : "";
    },
    mounted() {
      this.conectarWebSocket();
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
      v-if="conectado"
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