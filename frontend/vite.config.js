import { fileURLToPath, URL } from 'node:url';
import { defineConfig } from 'vite'
import { resolve } from 'path'
//import inject from '@rollup/plugin-inject';
import vue from '@vitejs/plugin-vue';
import Components from 'unplugin-vue-components/vite';
import {PrimeVueResolver} from '@primevue/auto-import-resolver';
import { viteStaticCopy } from 'vite-plugin-static-copy';

//inject({
// include: '**/*.js',
//    $: 'jquery',
//    jQuery: 'jquery',
//})

export default defineConfig({
  root: resolve(__dirname),
  base: '/static/',
  css: {
    devSourcemap: false
  },
  plugins: [
    vue(),
    Components({
      resolvers: [
        PrimeVueResolver()
      ]
    }),
    viteStaticCopy({
      targets: [
        {
          src: 'node_modules/primeicons/fonts/*',
          dest: 'assets/fonts'
        }
      ]
    })
  ],
  /*optimizeDeps: {
    include: ['jquery']
  },*/
  build: {
    manifest: 'manifest.json',
    outDir: resolve(__dirname, '../static'),
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'src/main.js')
      },
    },
  },
  resolve: {
    alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  server: {
    port: 5173,
    host:true,
    origin: 'http://localhost:5173',
    headers: {
      'Access-Control-Allow-Origin': '*'
    }
  },
  publicDir: 'public', // directorio de acceso publico
  assetsInclude: ['**/*.woff', '**/*.woff2','**/*.ttf','**/*.eot','**/*.svg']
})
