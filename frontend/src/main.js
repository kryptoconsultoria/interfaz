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



const app = createApp(MediosMagneticos);


app.use(PrimeVue, {
    theme: {
        preset: Noir,
        options: {
            prefix: 'p',
            darkModeSelector: '.p-dark',
            cssLayer: false,
        }
    }
});

app.use(AppState);
app.use(ToastService);
app.use(ConfirmationService);
app.use(ToastService);
app.use(DialogService);

// Montar widgets django vite
app.mount("#medios-magneticos");
app.mount("#medios-distritales");
