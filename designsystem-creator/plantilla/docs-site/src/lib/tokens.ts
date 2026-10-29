import tokensJson from "../../../tokens/tokens.json";

export type Token = {
  nombre: string;
  valor: string | number;
  claro?: string | number;
  tipo?: string;
};

function recorrer(d: any, ruta: string[], out: Token[]) {
  if (!d || typeof d !== "object") return;
  if ("$value" in d) {
    out.push({
      nombre: ruta.join("-"),
      valor: d.$value,
      claro: d.$extensions?.["theme-light"],
      tipo: d.$type,
    });
    return;
  }
  for (const [k, v] of Object.entries(d)) {
    if (!k.startsWith("_") && !k.startsWith("$")) recorrer(v, [...ruta, k], out);
  }
}

// Mismo aplanado que scripts/validar_contratos.py y generar_tokens_css.py:
// el nombre de token es la ruta sin el grupo de primer nivel.
export function todosLosTokens(): Token[] {
  const out: Token[] = [];
  for (const [grupo, contenido] of Object.entries(tokensJson as Record<string, any>)) {
    if (!grupo.startsWith("_")) recorrer(contenido, [], out);
  }
  return out;
}

let cache: Map<string, Token> | null = null;
export function tokenPorNombre(nombre: string): Token | undefined {
  if (!cache) {
    cache = new Map(todosLosTokens().map((t) => [t.nombre, t]));
  }
  return cache.get(nombre);
}

export function coloresPrimitivos(): Token[] {
  const out: Token[] = [];
  recorrer((tokensJson as any).primitivos_color, [], out);
  return out;
}

export function coloresSemanticos(): Token[] {
  const out: Token[] = [];
  recorrer((tokensJson as any).semanticos, [], out);
  return out.filter((t) => t.tipo === "color");
}

export function escala(grupo: string): Token[] {
  const out: Token[] = [];
  recorrer((tokensJson as any).primitivos_escala?.[grupo], [grupo], out);
  return out;
}
