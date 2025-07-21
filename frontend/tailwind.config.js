// tailwind.config.js
module.exports = {
  important: '#medios-magneticos',
  prefix: "tw-",
  corePlugins: {
    preflight: false,
  },
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
    './node_modules/primevue/**/*.{js,ts,vue}', // IMPORTANTE: para que Tailwind escanee los componentes de PrimeVue
  ],
  theme: {
    extend: {},
  },
  plugins: [],
  darkMode: 'class', // o 'media' si prefieres modo automático
}