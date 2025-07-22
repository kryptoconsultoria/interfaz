// import $ from 'jquery';
// window.$ = $;
// window.jQuery = $;

// estilos plantilla bootstrap 5
//import './assets/css/bootstrap.min.css'
//import './assets/css/plugins.min.css'
//import './assets/css/kaiadmin.css'

// librerias plantilla bootstrap 5
//import '@popperjs/core'
//import 'bootstrap'                       // busca bootstrap.bundle.js
//import WebFont from 'webfontloader'
//import './assets/js/kaiadmin.js'
//import 'jquery.scrollbar';


// css styles prime vue
import './style.css';
import './flags.css';
import 'primeicons/primeicons.css';


// Prime vue librerias componentes drag and drop y select sistema
import { createApp } from 'vue'
import MediosMagneticos from './MediosMagneticos.vue';
import MediosDistritales from './MediosDistritales.vue';
import PrimeVue from 'primevue/config';
import ConfirmationService from 'primevue/confirmationservice';
import DialogService from 'primevue/dialogservice';
import ToastService from 'primevue/toastservice';
import Toast from 'primevue/toast';

import AppState from './plugins/appState.js';
import Noir from './presets/Noir.js';



//Subir y probar componentes de primevue
//WebFont.load({
//  google: {
//    families: ['Public Sans:300,400,500,600,700']
//  },
//  custom: {
//    families: [
//      'Font Awesome 5 Solid',
//      'Font Awesome 5 Regular',
//      'Font Awesome 5 Brands',
//      'simple-line-icons'
//    ],
//    urls: [`http://localhost:5173/static/src/assets/css/fonts.min.css`]
//  },
//  active() {
//    sessionStorage.fonts = true;
//  }
//});

// Medios nacionales
const app1 = createApp(MediosMagneticos);
app1.use(PrimeVue, {
    theme: {
        preset: Noir,
        options: {
            prefix: 'p',
            darkModeSelector: '.p-dark',
            cssLayer: false,
        }
    }
});

app1.use(AppState);
app1.use(ToastService);
app1.use(ConfirmationService);
app1.use(ToastService);
app1.use(DialogService);

// Montar widgets django vite
app1.mount("#medios-magneticos");



// Medios distritales
const app2 = createApp(MediosDistritales);
app2.use(PrimeVue, {
    theme: {
        preset: Noir,
        options: {
            prefix: 'p',
            darkModeSelector: '.p-dark',
            cssLayer: false,
        }
    }
});

app2.use(AppState);
app2.use(ToastService);
app2.use(ConfirmationService);
app2.use(ToastService);
app2.use(DialogService);

// Montar widgets django vite
app2.mount("#medios-distritales");