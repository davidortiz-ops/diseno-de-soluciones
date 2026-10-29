import { load } from "js-yaml";

// Descubre TODOS los *.contract.yaml del repo en build time — nada
// hardcodeado. Si mañana se agrega un contrato nuevo, aparece solo.
const modulosCrudos = import.meta.glob(
  [
    "../../../atomos/*/*.contract.yaml",
    "../../../moleculas/*/*.contract.yaml",
    "../../../organismos/*/*.contract.yaml",
    "../../../templates/*/*.contract.yaml",
  ],
  { query: "?raw", import: "default", eager: true }
) as Record<string, string>;

export type Contrato = Record<string, any> & {
  component_id: string;
  intencion: string;
  tipo: string;
};

export type ContratoConFuente = {
  id: string;
  contrato: Contrato;
  yaml: string;
  rutaArchivo: string;
  carpeta: "atomos" | "moleculas" | "organismos" | "templates";
};

const TIPO_A_CARPETA: Record<string, ContratoConFuente["carpeta"]> = {
  atomo: "atomos",
  molecula: "moleculas",
  organismo: "organismos",
  plantilla: "templates",
  template: "templates",
};

let cache: ContratoConFuente[] | null = null;

export function todosLosContratos(): ContratoConFuente[] {
  if (cache) return cache;
  cache = Object.entries(modulosCrudos).map(([ruta, yaml]) => {
    const contrato = load(yaml) as Contrato;
    return {
      id: contrato.component_id,
      contrato,
      yaml,
      rutaArchivo: ruta,
      carpeta: TIPO_A_CARPETA[contrato.tipo] ?? "atomos",
    };
  });
  return cache;
}

export function contratoPorId(id: string): ContratoConFuente | undefined {
  return todosLosContratos().find((c) => c.id === id);
}

// Extrae comentarios # HALLAZGO / # OJO del YAML crudo (js-yaml los descarta
// al parsear) — cada uno se muestra como "No hacer" en la pestaña Guías.
export function extraerHallazgos(yaml: string): string[] {
  const lineas = yaml.split("\n");
  const hallazgos: string[] = [];
  let actual: string[] | null = null;

  for (const linea of lineas) {
    const inicio = linea.match(/^\s*#\s*(HALLAZGO|OJO)\b[:\s]*(.*)/i);
    if (inicio) {
      if (actual) hallazgos.push(actual.join(" ").trim());
      actual = [inicio[2].trim()].filter(Boolean);
      continue;
    }
    const continuacion = linea.match(/^\s*#\s?(.*)/);
    if (actual && continuacion) {
      actual.push(continuacion[1].trim());
      continue;
    }
    if (actual) {
      hallazgos.push(actual.join(" ").trim());
      actual = null;
    }
  }
  if (actual) hallazgos.push(actual.join(" ").trim());
  return hallazgos.filter(Boolean);
}

export function tienePendiente(yaml: string): boolean {
  return /PENDIENTE/.test(yaml);
}

export function extraerNotasPendiente(yaml: string): string[] {
  const lineas = yaml.split("\n");
  const notas: string[] = [];
  for (const linea of lineas) {
    if (/PENDIENTE/.test(linea)) {
      const limpio = linea.replace(/^\s*#\s?/, "").trim();
      notas.push(limpio);
    }
  }
  return notas;
}

// Nivel (atomo|molecula|organismo) -> carpeta, para enlazar `usa:` a su página.
export function hrefComponente(nivel: string, id: string): string | undefined {
  if (!(nivel in TIPO_A_CARPETA)) return undefined;
  return `/componentes/${id}`;
}
