// Código real de cada componente (.tsx + .css co-locados con su contrato),
// leído crudo para mostrarlo en la página del componente — nunca reescrito
// ni resumido: es el mismo archivo que se importa en producción.
const modulosCodigo = import.meta.glob(
  [
    "../../../atomos/*/*.tsx",
    "../../../atomos/*/*.css",
    "../../../moleculas/*/*.tsx",
    "../../../moleculas/*/*.css",
    "../../../organismos/*/*.tsx",
    "../../../organismos/*/*.css",
    "../../../templates/*/*.tsx",
    "../../../templates/*/*.css",
    "../../../templates/*/*.html",
  ],
  { query: "?raw", import: "default", eager: true }
) as Record<string, string>;

export type ArchivoCodigo = { nombre: string; contenido: string; lenguaje: string };

const LENGUAJE_POR_EXTENSION: Record<string, string> = {
  tsx: "tsx",
  ts: "ts",
  css: "css",
  html: "html",
};

export function lenguajeDe(nombreArchivo: string): string {
  const extension = nombreArchivo.split(".").pop() ?? "";
  return LENGUAJE_POR_EXTENSION[extension] ?? "plaintext";
}

export function codigoFuenteDe(componentId: string): ArchivoCodigo[] {
  return Object.entries(modulosCodigo)
    .filter(([ruta]) => ruta.includes(`/${componentId}/`))
    .map(([ruta, contenido]) => {
      const nombre = ruta.split("/").pop()!;
      return { nombre, contenido, lenguaje: lenguajeDe(nombre) };
    })
    .sort((a) => (a.nombre.endsWith(".tsx") ? -1 : 1));
}
