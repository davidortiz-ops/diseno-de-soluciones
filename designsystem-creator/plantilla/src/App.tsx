import { useState } from "react";
import "./App.css";

// Demo/playground del sistema de diseño. Cada componente que crees se monta
// aquí para verlo en ambos temas — no vive lógica de negocio. Reemplaza este
// contenido a medida que agregues átomos reales, por ejemplo:
//   import { Badge } from "@atomos/badge/Badge";
export function App() {
  const [tema, setTema] = useState<"oscuro" | "claro">("oscuro");

  return (
    <div className="playground" data-theme={tema === "claro" ? "claro" : undefined}>
      <button className="playground__boton" onClick={() => setTema((t) => (t === "oscuro" ? "claro" : "oscuro"))}>
        Tema: {tema}
      </button>

      <section className="playground__seccion">
        <h2>Playground vacío</h2>
        <p>
          Todavía no hay componentes. Crea tu primer átomo en <code>atomos/</code> (contrato + código) y móntalo
          aquí para verlo en ambos temas.
        </p>
      </section>
    </div>
  );
}
