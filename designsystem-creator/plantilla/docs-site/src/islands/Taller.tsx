import { useMemo, useState } from "react";
import { moduloMuestrasDe } from "../lib/muestras";
import "./Taller.css";

type VarianteEje = { eje: string; opciones: string[]; por_defecto?: string };
type Dato = { nombre: string; tipo?: string; obligatorio?: boolean };
type Accion = { nombre: string; dispara?: string };

type Control =
  | { tipo: "seleccion"; prop: string; etiqueta: string; opciones: string[]; porDefecto: string }
  | { tipo: "booleano"; prop: string; etiqueta: string }
  | { tipo: "texto"; prop: string; etiqueta: string; obligatorio: boolean };

// Snake_case del contrato -> camelCase del prop real en el .tsx (ej:
// posicion_etiqueta -> posicionEtiqueta). Misma convención en todo el repo.
function aCamelCase(snake: string): string {
  return snake.replace(/_([a-z0-9])/g, (_, c) => c.toUpperCase());
}

function etiquetaDesde(nombre: string): string {
  const limpio = nombre.replace(/_/g, " ");
  return limpio.charAt(0).toUpperCase() + limpio.slice(1);
}

// Una acción se trata como "interruptor de estado" solo si dispara un
// evento genérico de cambio Y el componente tiene exactamente un dato
// booleano al que aplicarlo — evita que una acción sin relación (ej.
// "alEditar"/onEdit) termine volteando el booleano de otra.
const EVENTO_INTERRUPTOR = /^on(change|click|input|toggle)$/;

export function Taller({
  componentId,
  variantes,
  datos,
  estados,
  acciones,
}: {
  componentId: string;
  variantes: VarianteEje[];
  datos: Dato[];
  estados: string[];
  acciones: Accion[];
}) {
  const entrada = useMemo(() => moduloMuestrasDe(componentId), [componentId]);

  const { controles, propBooleanoUnico } = useMemo(() => {
    const propsUsados = new Set<string>();
    const lista: Control[] = [];
    const booleanos: string[] = [];

    for (const v of variantes) {
      const prop = aCamelCase(v.eje);
      propsUsados.add(prop);
      lista.push({
        tipo: "seleccion",
        prop,
        etiqueta: etiquetaDesde(v.eje),
        opciones: v.opciones ?? [],
        porDefecto: v.por_defecto ?? v.opciones?.[0] ?? "",
      });
    }

    for (const d of datos) {
      const prop = aCamelCase(d.nombre);
      if (propsUsados.has(prop)) continue;
      const esTexto = d.tipo === undefined || d.tipo === "texto";
      const esBooleano = d.tipo === "booleano";
      // Cualquier otro tipo (lista, "datos de <otro-componente>", objeto
      // compuesto…) no tiene un control de texto/booleano que le sirva —
      // queda solo de lectura desde la muestra en vez de mostrar
      // "[object Object]" en un input.
      if (!esTexto && !esBooleano) continue;
      propsUsados.add(prop);
      if (esBooleano) {
        booleanos.push(prop);
        lista.push({ tipo: "booleano", prop, etiqueta: etiquetaDesde(d.nombre) });
      } else {
        lista.push({ tipo: "texto", prop, etiqueta: etiquetaDesde(d.nombre), obligatorio: !!d.obligatorio });
      }
    }

    if (estados.includes("deshabilitado") && !propsUsados.has("deshabilitado")) {
      lista.push({ tipo: "booleano", prop: "deshabilitado", etiqueta: "Deshabilitado" });
    }

    return { controles: lista, propBooleanoUnico: booleanos.length === 1 ? booleanos[0] : null };
  }, [variantes, datos, estados]);

  const datosSoloMuestra = useMemo(
    () => datos.filter((d) => d.tipo !== undefined && d.tipo !== "texto" && d.tipo !== "booleano").map((d) => d.nombre),
    [datos]
  );

  const [valores, setValores] = useState<Record<string, any>>(() => {
    const primeraMuestra = entrada ? Object.values(entrada.muestras)[0] : null;
    const base: Record<string, any> = { ...((primeraMuestra as any) ?? {}) };
    for (const c of controles) {
      if (base[c.prop] !== undefined) continue;
      base[c.prop] = c.tipo === "booleano" ? false : c.tipo === "seleccion" ? c.porDefecto : "";
    }
    return base;
  });

  if (!entrada) {
    return (
      <p className="taller__vacio">
        Todavía no hay *.muestras.ts co-locado para este componente — el Taller necesita al menos una muestra de
        referencia para tomar datos base.
      </p>
    );
  }

  const Componente = entrada.componente;

  function actualizar(prop: string, valor: any) {
    setValores((v) => ({ ...v, [prop]: valor }));
  }

  function manejadorAccion(accion: Accion) {
    const evento = String(accion.dispara ?? "").toLowerCase();
    if (propBooleanoUnico && EVENTO_INTERRUPTOR.test(evento)) {
      return (arg?: any) =>
        setValores((v) => ({
          ...v,
          [propBooleanoUnico]: typeof arg === "boolean" ? arg : !v[propBooleanoUnico],
        }));
    }
    return () => {};
  }

  const propsAcciones: Record<string, (...args: any[]) => void> = {};
  for (const a of acciones) {
    const manejador = manejadorAccion(a);
    if (a.nombre) propsAcciones[a.nombre] = manejador;
    if (a.dispara) propsAcciones[a.dispara] = manejador;
  }

  const propsFinales: Record<string, any> = { ...valores };
  for (const c of controles) {
    if (c.tipo === "texto" && !c.obligatorio && propsFinales[c.prop] === "") {
      propsFinales[c.prop] = undefined;
    }
  }

  return (
    <div className="taller">
      <div className="taller__controles">
        {controles.length === 0 && <p className="taller__vacio">Este componente no tiene ejes ni datos configurables.</p>}
        {controles.map((c) => (
          <label className={`taller__control ${c.tipo === "booleano" ? "taller__control--booleano" : ""}`} key={c.prop}>
            <span className="taller__etiqueta">{c.etiqueta}</span>
            {c.tipo === "seleccion" && (
              <select
                className="taller__select"
                value={valores[c.prop] ?? ""}
                onChange={(e) => actualizar(c.prop, e.target.value)}
              >
                {c.opciones.map((o) => (
                  <option value={o} key={o}>
                    {o}
                  </option>
                ))}
              </select>
            )}
            {c.tipo === "booleano" && (
              <input
                type="checkbox"
                className="taller__checkbox"
                checked={!!valores[c.prop]}
                onChange={(e) => actualizar(c.prop, e.target.checked)}
              />
            )}
            {c.tipo === "texto" && (
              <input
                type="text"
                className="taller__texto"
                value={valores[c.prop] ?? ""}
                onChange={(e) => actualizar(c.prop, e.target.value)}
              />
            )}
          </label>
        ))}
        {datosSoloMuestra.length > 0 && (
          <p className="taller__nota">
            Usa los datos de muestra de <code>{componentId}.muestras.ts</code> para: {datosSoloMuestra.join(", ")}.
          </p>
        )}
      </div>
      <div className="taller__lienzo">
        <Componente {...propsFinales} {...propsAcciones} />
      </div>
    </div>
  );
}
