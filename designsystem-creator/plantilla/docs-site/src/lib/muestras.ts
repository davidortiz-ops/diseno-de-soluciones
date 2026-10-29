// Descubre los *.muestras.ts co-locados con cada contrato — component real +
// datos de muestra nombrados. Vite resuelve este glob en build time a
// imports estáticos reales.
const modulosMuestras = import.meta.glob(
  [
    "../../../atomos/*/*.muestras.ts",
    "../../../moleculas/*/*.muestras.ts",
    "../../../organismos/*/*.muestras.ts",
    "../../../templates/*/*.muestras.ts",
  ],
  { eager: true }
) as Record<string, any>;

export function moduloMuestrasDe(componentId: string): any | null {
  const ruta = Object.keys(modulosMuestras).find((p) => p.includes(`/${componentId}/`));
  return ruta ? modulosMuestras[ruta] : null;
}
