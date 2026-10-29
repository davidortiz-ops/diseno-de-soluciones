import { useMemo } from "react";
import { moduloMuestrasDe } from "../lib/muestras";
import "./EstadosVivos.css";

export function EstadosVivos({ componentId }: { componentId: string }) {
  const entrada = useMemo(() => moduloMuestrasDe(componentId), [componentId]);

  if (!entrada) {
    return <p className="estados-vivos__vacio">Todavía no hay *.muestras.ts co-locado para este componente.</p>;
  }

  const Componente = entrada.componente;
  const variantes = Object.entries(entrada.muestras);

  return (
    <div className="estados-vivos">
      {variantes.map(([nombre, props]: [string, any]) => (
        <div className="estados-vivos__item" key={nombre}>
          <span className="estados-vivos__etiqueta">{nombre}</span>
          <div className="estados-vivos__lienzo">
            <Componente {...props} />
          </div>
        </div>
      ))}
      <p className="estados-vivos__nota">
        Galería tomada de <code>{componentId}.muestras.ts</code>. Los estados que dependen de una interacción real
        (foco, confirmaciones) se exploran en la pestaña Taller.
      </p>
    </div>
  );
}
