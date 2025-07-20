<template>
  <FileUpload
    :name="props.name"
    :url="props.url"
    customUpload
    @uploader="uploadHandler"
    :multiple="props.multiple"
    :accept="props.accept"
    @select="onSelectedFiles"
    class="p-4 border border-gray-300 rounded w-full"
  >
    <template #header="{ chooseCallback, uploadCallback, clearCallback, files: headerFiles }">
      <div class="flex flex-wrap justify-between items-center flex-1 gap-4">
        <div class="flex gap-2">
          <Button @click="chooseCallback()" icon="pi pi-file" rounded outlined severity="secondary" />
          <Button @click="uploadCallback()" icon="pi pi-cloud-upload" rounded outlined severity="success"
            :disabled="!headerFiles || headerFiles.length === 0" />
          <Button @click="onClearTemplatingUpload(clearCallback)" icon="pi pi-times" rounded outlined severity="danger"
            :disabled="!headerFiles || headerFiles.length === 0" />
          <Button
            icon="pi pi-trash"
            rounded
            severity="danger"
            v-tooltip.bottom="'Eliminar archivos del servidor'"
            aria-label="Eliminar archivos"
            @click="deleteFile"
          />
        </div>
      </div>
    </template>

    <template #content="{ files: slotFiles, uploadedFiles, removeUploadedFileCallback, removeFileCallback, messages }">
      <div class="flex flex-col gap-4 pt-4">
        <Message
          v-for="message in messages"
          :key="message"
          :class="{ 'mb-8': !slotFiles.length && !uploadedFiles.length }"
          severity="error"
        >
          {{ message }}
        </Message>

        <div v-if="slotFiles.length > 0">
          <ul class="flex flex-col gap-2">
            <li
              v-for="(file, index) in slotFiles"
              :key="file.__uid"
              class="flex items-center justify-between border border-surface p-3 rounded"
            >
              <div class="flex flex-col">
                <span class="font-medium">{{ file.name }}</span>
                <small class="text-gray-500">{{ formatSize(file.size) }}</small>
                <small v-if="file.errorMessage" class="text-red-500">{{ file.errorMessage }}</small>
              </div>
              <div class="flex items-center gap-2">
                <Badge :value="statusLabel(file)" :severity="statusSeverity(file)" />
                <Button icon="pi pi-times" @click="onRemoveTemplatingFile(file, removeFileCallback, index)"
                  outlined rounded severity="danger" />
              </div>
            </li>
          </ul>
        </div>

        <div v-if="uploadedFiles.length > 0">
          <h5 class="font-bold mt-6 mb-2">Archivos subidos</h5>
          <ul class="flex flex-col gap-2">
            <li
              v-for="(file, index) in uploadedFiles"
              :key="file.__uid"
              class="flex items-center justify-between border border-surface p-3 rounded"
            >
              <div class="flex flex-col">
                <span class="font-medium">{{ file.name }}</span>
                <small class="text-gray-500">{{ formatSize(file.size) }}</small>
              </div>
              <div class="flex items-center gap-2">
                <Badge value="Completado" severity="success" />
                <Button icon="pi pi-times" @click="removeUploadedFileCallback(index)" outlined rounded severity="danger" />
              </div>
            </li>
          </ul>
        </div>
      </div>
    </template>

    <template #empty>
      <div class="flex items-center justify-center flex-col">
        <i class="pi pi-cloud-upload !border-2 !rounded-full !p-8 !text-4xl !text-muted-color" />
        <p class="mt-6 mb-0">Arrastre los archivos para subir al servidor.</p>
      </div>
    </template>
  </FileUpload>
</template>
<script setup>
import { ref, reactive, getCurrentInstance } from 'vue';
import FileUpload from 'primevue/fileupload';
import Button from 'primevue/button';
import Badge from 'primevue/badge';
import Message from 'primevue/message';
import { useToast } from 'primevue/usetoast';
import { usePrimeVue } from 'primevue/config';

const props = defineProps({
  url: { type: String, required: true },
  url_delete: { type: String, required: true },
  multiple: { type: Boolean, default: true },
  accept: { type: String, default: null },
  name: { type: String, default: null }
});

const toast = useToast();
const primevue = usePrimeVue();
const totalSize = ref(0);

// Funciones de utilidad
const formatSize = bytes => {
  const sizes = primevue.config.locale?.fileSizeTypes || ['B','KB','MB','GB','TB'];
  if (!bytes || isNaN(bytes)) return '0 B';
  const i = Math.floor(Math.log(bytes)/Math.log(1024));
  return `${(bytes/Math.pow(1024, i)).toFixed(2)} ${sizes[i]}`;
};

const statusLabel = file => {
  return file.status === 'uploading' ? 'Subiendo'
    : file.status === 'success' ? 'Subido'
    : file.status === 'error' ? 'Error'
    : 'Pendiente';
};

const statusSeverity = file => {
  return file.status === 'uploading' ? 'info'
    : file.status === 'success' ? 'success'
    : file.status === 'error' ? 'danger'
    : 'warn';
};

// Handlers de FileUpload
const onSelectedFiles = event => {
  const enhanced = event.files.map(f => reactive({
    __uid: Symbol(),
    name: f.name,
    size: f.size ?? 0,
    type: f.type,
    status: 'pending',
    errorMessage: null,
    raw: f
  }));
  event.files.splice(0, event.files.length, ...enhanced);
  totalSize.value = enhanced.reduce((sum, f) => sum + f.size, 0);
};

const onClearTemplatingUpload = clear => {
  clear();
  totalSize.value = 0;
};

const onRemoveTemplatingFile = (file, removeFile, idx) => {
  removeFile(idx);
};

const uploadHandler = event => {
  const files = Array.isArray(event.files) ? event.files : [event.files];
  for (const file of files) {
    file.status = 'uploading';
    file.errorMessage = null;
    const formData = new FormData();
    formData.append(props.name || 'file', file.raw);
    const xhr = new XMLHttpRequest();
    xhr.open('POST', props.url, true);
    xhr.onload = () => {
      let resp;
      try { resp = JSON.parse(xhr.responseText); }
      catch {
        file.status = 'error';
        file.errorMessage = 'Respuesta inválida del servidor';
        toast.add({ severity:'error', summary:'Error', detail:file.errorMessage, life:5000 });
        return;
      }
      if (xhr.status >= 200 && xhr.status < 300 && resp.success) {
        file.status = 'success';
        event.upload?.(file);
        toast.add({ severity:'success', summary:'¡Éxito!', detail:file.name, life:3000 });
      } else {
        file.status = 'error';
        file.errorMessage = resp.message || 'Error al subir';
        toast.add({ severity:'error', summary:'Error', detail:file.errorMessage, life:5000 });
      }
    };
    xhr.onerror = () => {
      file.status = 'error';
      file.errorMessage = 'Fallo de red';
      toast.add({ severity:'error', summary:'Error', detail:file.errorMessage, life:5000 });
    };
    xhr.send(formData);
  }
};

// CSRF y delete handler
const cargando = ref(false);

const obtenerTokenCSRF = () => {
  const match = document.cookie.match(/csrftoken=([^;]+)/);
  return match ? match[1] : '';
};

const deleteFile = async (event) => {
  cargando.value = true;

  let resp = null;
  let ok = false;

  try {
    const response = await fetch(props.url_delete, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': obtenerTokenCSRF()
      },
      credentials: 'same-origin'
    });
    resp = await response.json().catch(() => null);

    if (!resp) throw new Error('Respuesta inválida del servidor');

    if (response.ok && resp.success) {
      ok = true;
      toast.add({ severity:'success', summary:'¡Éxito!', detail:'Eliminación exitosa', life:3000 });
    } else {
      const msg = resp.message || 'Error al eliminar';
      toast.add({ severity:'error', summary:'Error', detail:msg, life:5000 });
    }
  } catch (err) {
    toast.add({ severity:'error', summary:'Error', detail: err.message || 'Error de red', life:5000 });
  } finally {
    cargando.value = false;
    event.upload?.({
      status: ok ? 'success' : 'error',
      errorMessage: resp?.message || null
    });
  }
};
</script>

