// @ts-check
import { defineConfig } from "astro/config";
import react from "@astrojs/react";
import path from "node:path";
import { fileURLToPath } from "node:url";

const dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(dirname, "..");

// docs-site/ es un sitio APARTE dentro del repo, pero lee del repo padre en
// build time: tokens/tokens.json, *.contract.yaml co-locados, REGLAS-GLOBALES.md,
// CLAUDE.md y los componentes React reales (atomos/organismos) para embeberlos
// vivos en la pestaña "Estados". Nada de eso se copia a mano.
export default defineConfig({
  integrations: [react()],
  vite: {
    resolve: {
      alias: {
        "@atomos": path.resolve(repoRoot, "atomos"),
        "@moleculas": path.resolve(repoRoot, "moleculas"),
        "@organismos": path.resolve(repoRoot, "organismos"),
        "@templates": path.resolve(repoRoot, "templates"),
        "@repo-tokens-css": path.resolve(repoRoot, "src/estilos/tokens.css"),
      },
      // Los componentes reales viven fuera de docs-site/node_modules (en
      // atomos/organismos, hermanos de docs-site/). Sin este dedupe, Node
      // resolvería su `import "react"` hacia el node_modules del repo raíz
      // en vez del de docs-site, cargando DOS copias de React a la vez.
      // (Un alias directo a la carpeta rompe el interop CJS/ESM de Vite en
      // modo dev — dedupe usa la resolución normal de Vite, solo la fuerza
      // a colapsar en una sola copia.)
      dedupe: ["react", "react-dom"],
    },
    server: {
      fs: {
        allow: [repoRoot],
      },
    },
  },
});
