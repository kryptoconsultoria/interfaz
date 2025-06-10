<script setup>
import { ref } from 'vue';
import { usePrimeVue } from 'primevue/config';
import { useToast } from "primevue/usetoast";

const $primevue = usePrimeVue();
const toast = useToast();

const totalSize = ref(0);
const totalSizePercent = ref(0);
const files = ref([]);

// Sobreescribir parametros de entrada
const props = defineProps({
  // URL a la que subir archivos
  url: {
    type: String,
    required: true
  },
  // ¿Permitir varias selecciones?
  multiple: {
    type: Boolean,
    default: true
  },
  // Tipo de archivos aceptados
  accept: {
    type: String,
    default: null
  },
  // Tipo de archivos aceptados
  name: {
    type: String,
    default: null
  }
})

const onRemoveTemplatingFile = (file, removeFileCallback, index) => {
    removeFileCallback(index);
    totalSize.value -= file.size;
    totalSizePercent.value = totalSize.value / 10;
};

const onClearTemplatingUpload = (clear) => {
    clear();
    totalSize.value = 0;
    totalSizePercent.value = 0;
};

const onSelectedFiles = (event) => {
    files.value = event.files;
    files.value.forEach((file) => {
        totalSize.value += parseInt(formatSize(file.size));
    });
};

const uploadEvent = (callback) => {
    totalSizePercent.value = totalSize.value / 10;
    callback();
};

const onTemplatedUpload = () => {
    toast.add({ severity: "info", summary: "Success", detail: "File Uploaded", life: 3000 });
};

const formatSize = (bytes) => {
    const k = 1024;
    const dm = 3;
    const sizes = $primevue.config.locale.fileSizeTypes;

    if (bytes === 0) {
        return `0 ${sizes[0]}`;
    }

    const i = Math.floor(Math.log(bytes) / Math.log(k));
    const formattedSize = parseFloat((bytes / Math.pow(k, i)).toFixed(dm));

    return `${formattedSize} ${sizes[i]}`;
};
</script>

<template>
  <FileUpload
    :name="props.name"
    :url="props.url"
    @upload="onTemplatedUpload($event)"
    :multiple="props.multiple"
    :accept="props.accept"
    @select="onSelectedFiles"
    class="p-4 border border-gray-300 rounded w-full"
  >
    <template #header="{ chooseCallback, uploadCallback, clearCallback, files }">
      <div class="flex flex-wrap justify-between items-center flex-1 gap-4">
        <div class="flex gap-2">
          <Button @click="chooseCallback()" icon="pi pi-file" rounded outlined severity="secondary"></Button>
          <Button @click="uploadEvent(uploadCallback)" icon="pi pi-cloud-upload" rounded outlined severity="success" :disabled="!files || files.length === 0"></Button>
          <Button @click="onClearTemplatingUpload(clearCallback)" icon="pi pi-times" rounded outlined severity="danger" :disabled="!files || files.length === 0"></Button>
        </div>
      </div>
    </template>

    <template #content="{ files, uploadedFiles, removeUploadedFileCallback, removeFileCallback, messages }">
      <div class="flex flex-col gap-4 pt-4">
        <Message
          v-for="message of messages"
          :key="message"
          :class="{ 'mb-8': !files.length && !uploadedFiles.length }"
          severity="error"
        >
          {{ message }}
        </Message>

        <div v-if="files.length > 0">
          <h5 class="font-bold text-sm">Archivos pendientes</h5>
          <ul class="flex flex-col gap-2">
            <li
              v-for="(file, index) of files"
              :key="file.name + file.type + file.size"
              class="flex items-center justify-between border border-surface p-3 rounded"
            >
              <div class="flex flex-col">
                <span class="font-medium">{{ file.name }}</span>
                <small class="text-gray-500">{{ formatSize(file.size) }}</small>
              </div>
              <div class="flex items-center gap-2">
                <Badge value="Pendiente" severity="warn" />
                <Button icon="pi pi-times" @click="onRemoveTemplatingFile(file, removeFileCallback, index)" outlined rounded severity="danger" />
              </div>
            </li>
          </ul>
        </div>

        <div v-if="uploadedFiles.length > 0">
          <h5 class="font-bold mt-6 mb-2">Archivos subidos</h5>
          <ul class="flex flex-col gap-2">
            <li
              v-for="(file, index) of uploadedFiles"
              :key="file.name + file.type + file.size"
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
<style scoped>
</style>