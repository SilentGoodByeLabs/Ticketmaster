import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.ticketmaster.app',
  appName: 'Ticketmaster',
  webDir: 'www',
  server: {
    androidScheme: 'https'
  }
};

export default config;
