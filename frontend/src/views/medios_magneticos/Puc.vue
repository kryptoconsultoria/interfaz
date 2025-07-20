<script setup>
import SubirArchivo from '../../components/SubirArchivo.vue';
import { useToast } from 'primevue/usetoast';
const toast = useToast();

const DownloadFile = async (event) => {
  let resp = null;
  let ok = false;
  try {
    const response = await fetch('/medios_magneticos/descargar_puc/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': obtenerTokenCSRF()
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
    toast.add({ severity:'success', summary:'¡Éxito!', detail:'Descarga exitosa', life:3000 });
  } catch (err) {
    const msg = err.message || 'Error de red';
    toast.add({ severity:'error', summary:'Error', detail: msg, life:50000 });
  } finally {
    resp = resp || {};
    event.upload?.({
      status: ok ? 'success' : 'error',
      errorMessage: resp.message || null
    });
  }
};

const obtenerTokenCSRF = () => {
  const match = document.cookie.match(/csrftoken=([^;]+)/);
  return match ? match[1] : '';
};

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
          @click="DownloadFile"
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
