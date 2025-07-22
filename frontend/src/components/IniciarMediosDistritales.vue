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
      mostrarCard: false, // Nuevo control para mostrar la tarjeta
      mostrarDescargas: false  // Nuevo control para mostrar descargas
    };
  },
  methods: {
    async iniciarAutomatizacion() {
      this.cargando = true;
      this.error = "";
      this.mostrarCard = false; // Oculta la tarjeta antes de iniciar
      this.mostrarDescargas = false; // mostrar descargas igual a false antes de iniciar

      const TIMEOUT_MS  = 1200000;

      try {
        const respuesta = await fetch("/medios_distritales/iniciar_automatizacion/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": this.obtenerTokenCSRF()
          },
          signal: AbortSignal.timeout(TIMEOUT_MS),
        });
        const resp = await respuesta.json();
        if (resp.success == true){
            const info = resp.data;
            this.cargando = false;
            this.mostrarCard = true;
            this.robot = info.Tarea;
            this.estado = info.Estado;
            this.historiaUsuario = info.HistoriaUsuario || "";
            this.detalleError = info.ErrorDetalle || "";
            this.error = "";

            if (this.estado == "Finalizado" && this.robot == "subir_archivos") {
              console.log("verdadero")
              this.mostrarDescargas = true;
            }

        } else {
          this.mostrarCard = true;
          this.error = resp.message || "Error al iniciar la automatización.";
        }

      } catch (err) {
        this.error = "Error de red o servidor: " + err;
      } finally {
        this.cargando = false;
        this.mostrarCard = true;
      }
    },
    async DownloadFile (endpoint){
      let resp = null;
      let ok = false;
      try {
        const response = await fetch(endpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.obtenerTokenCSRF()
          },
          credentials: 'same-origin'
        });

        if (!response.ok) {
          throw new Error(`Error del servidor: ${response.status}`);
        }

        console.log(response.headers)
        const cd = response.headers.get('Content-Disposition') || '';
        const match = cd.match(/filename\*?=(?:UTF-8''|")?([^;"']+)/i);
        const filename = match ? decodeURIComponent(match[1]) : 'archivo.bin';

        const blob = await response.blob(); // lee como blob
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        link.remove();
        URL.revokeObjectURL(url);

        ok = true;
        this.$toast.add({ severity:'success', summary:'¡Éxito!', detail:'Descarga exitosa', life:3000 });
      } catch (err) {
        const msg = err.message || 'Error de red';
        this.$toast.add({ severity:'error', summary:'Error', detail: msg, life:50000 });
      } finally {
        resp = resp || {};
        event.upload?.({
          status: ok ? 'success' : 'error',
          errorMessage: resp.message || null
        });
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

        <!-- Este div usa mt-auto para empujar los botones al fondo -->
        <div v-if="mostrarDescargas" class="mt-auto flex justify-end gap-x-2 pt-4"  >
          <Button
            rounded
            v-tooltip.bottom="'Descargar medios nacionales desglosados'"
            severity="info"
            icon="pi pi-download"
            size="large"
            :disabled="cargando"
            @click="DownloadFile('/medios_magneticos/descargar_medios_desglosados/')"
          />
          <Button
            rounded
            v-tooltip.bottom="'Descargar medios nacionales'"
            severity="success"
            icon="pi pi-download"
            size="large"
            :disabled="cargando"
            @click="DownloadFile('/medios_magneticos/descargar_medios/')"a tarjeta
          />
        </div>
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