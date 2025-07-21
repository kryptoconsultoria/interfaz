import { definePreset } from '@primeuix/themes';
import Aura from '@primeuix/themes/aura';

const AzulKrypto = definePreset(Aura, {
  semantic: {
    primary: {
      50: '#e1e5eb',
      100: '#b3bdce',
      200: '#8293af',
      300: '#50698f',
      400: '#2e4c77',
      500: '#0D1B2A',  // Color principal
      600: '#0a1623',
      700: '#08111c',
      800: '#060d16',
      900: '#040911',
      950: '#02050b'
    },
    colorScheme: {
      light: {
        primary: {
          color: '{primary.500}',
          contrastColor: '#ffffff',
          hoverColor: '{primary.400}',
          activeColor: '{primary.300}'
        },
        highlight: {
          background: '{primary.500}',
          focusBackground: '{primary.400}',
          color: '#ffffff',
          focusColor: '#ffffff'
        }
      },
      dark: {
        primary: {
          color: '{primary.100}',
          contrastColor: '{primary.900}',
          hoverColor: '{primary.200}',
          activeColor: '{primary.300}'
        },
        highlight: {
          background: '{primary.100}',
          focusBackground: '{primary.200}',
          color: '{primary.900}',
          focusColor: '{primary.900}'
        }
      }
    }
  }
});

export default AzulKrypto;
