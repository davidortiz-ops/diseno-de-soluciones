import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "node:path";

// Alias hacia las carpetas atómicas del sistema de diseño — los componentes
// se importan desde ahí (ej: import { Badge } from "@atomos/badge/Badge"),
// nunca se mueven a src/. src/ es solo el demo/playground.
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@atomos": path.resolve(__dirname, "atomos"),
      "@moleculas": path.resolve(__dirname, "moleculas"),
      "@organismos": path.resolve(__dirname, "organismos"),
      "@templates": path.resolve(__dirname, "templates"),
    },
  },
});
