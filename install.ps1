# Instala o actualiza las skills de Diseño de Soluciones en la carpeta actual, sea cual sea su ruta.
# Pregunta cuáles instalar antes de copiar nada.
#
#   irm https://raw.githubusercontent.com/davidortiz-ops/diseno-de-soluciones/main/install.ps1 | iex
#
# $env:DDS_ORIGEN = '<carpeta>' instala desde una copia local (lo usan las pruebas).
# $env:DDS_SKILLS = '1,3' o 'todas' responde la pregunta sin preguntar.
& {
    $ErrorActionPreference = 'Stop'
    $ProgressPreference = 'SilentlyContinue'

    $repo = 'davidortiz-ops/diseno-de-soluciones'
    $rama = if ($env:DDS_RAMA) { $env:DDS_RAMA } else { 'main' }

    $catalogo = @(
        @{ carpeta = 'accesibilidad-wcag'; texto = 'Accesibilidad WCAG 2.2: audita sitios web contra los 87 criterios WCAG.' },
        @{ carpeta = 'auditoria-de-flujos'; texto = 'Auditoría de flujos: confronta un flujo diseñado con la investigación de usuario.' },
        @{ carpeta = 'consultor-madurez-design-systems'; texto = 'Consultor de madurez de Design Systems: diagnóstico y hoja de ruta.' },
        @{ carpeta = 'contratos-de-diseno'; texto = 'Contratos de diseño: piezas de UI como contratos YAML contra tus tokens.' },
        @{ carpeta = 'designsystem-creator'; texto = 'Designsystem-creator: arranca un sistema de diseño nuevo desde una plantilla.' },
        @{ carpeta = 'evaluacion-heuristica'; texto = 'Heuristy: evaluación heurística de Nielsen para banca y retail.' },
        @{ carpeta = 'proto-persona-banca-top-tier'; texto = 'Proto-persona banca Top Tier: evalúa como cliente de altos ingresos.' },
        @{ carpeta = 'tognazzini-revision-heuristica-creditos-vivienda'; texto = 'Tognazzini: experiencia de solicitud de crédito de vivienda.' }
    )

    function Falla($texto) {
        Write-Host "No se pudo instalar: $texto" -ForegroundColor Red
        throw 'instalacion-cancelada'
    }

    try {
        # La carpeta personal, la raíz de un disco o la de Windows no son una carpeta de trabajo
        # (PowerShell como administrador abre en C:\Windows\System32).
        function No-Sirve($ruta) {
            $r = $ruta.TrimEnd('\')
            return ($r -ieq $HOME.TrimEnd('\')) -or ($r -match '^[A-Za-z]:$') -or
                   ($env:SystemRoot -and $r.StartsWith($env:SystemRoot, [StringComparison]::OrdinalIgnoreCase))
        }

        $destinoRepo = (Get-Location).ProviderPath
        if (No-Sirve $destinoRepo) {
            if ($env:DDS_SKILLS) {
                Falla 'no estás en una carpeta de trabajo. Entra primero a la carpeta donde vas a trabajar y vuelve a ejecutar el comando.'
            }
            Write-Host "Estás en $destinoRepo, que no es una carpeta de trabajo."
            $ruta = Read-Host 'Escribe la ruta de la carpeta donde vas a trabajar (o arrástrala aquí desde el Explorador) y presiona Enter'
            $ruta = "$ruta".Trim()
            if ($ruta.StartsWith('& ')) { $ruta = $ruta.Substring(2).Trim() }
            $ruta = $ruta.Trim('"').Trim("'")
            if ($ruta -eq '~' -or $ruta.StartsWith('~\') -or $ruta.StartsWith('~/')) { $ruta = $HOME + $ruta.Substring(1) }
            if (-not $ruta) { Falla 'no se recibió ninguna carpeta.' }
            if (-not (Test-Path -LiteralPath $ruta -PathType Container)) {
                $r = Read-Host "La carpeta $ruta no existe. ¿La creo? [S/n]"
                if ($r -match '^(n|no)$') { Falla "la carpeta $ruta no existe." }
                New-Item -ItemType Directory -Force -Path $ruta | Out-Null
            }
            $destinoRepo = (Resolve-Path -LiteralPath $ruta).ProviderPath
            if (No-Sirve $destinoRepo) { Falla 'esa no es una carpeta de trabajo: elige o crea una carpeta para tu proyecto.' }
            Set-Location -LiteralPath $destinoRepo
        }

        # ---- Cuáles instalar
        Write-Host ''
        Write-Host 'Skills de Diseño de Soluciones disponibles:'
        for ($i = 0; $i -lt $catalogo.Count; $i++) {
            Write-Host ("  {0}. {1}" -f ($i + 1), $catalogo[$i].texto)
        }
        Write-Host ''
        $respuesta = if ($env:DDS_SKILLS) { $env:DDS_SKILLS } else {
            Read-Host 'Escribe los números de las que quieres instalar, separados por coma (ej: 1,3,5), o «todas»'
        }
        $respuesta = "$respuesta".Trim().ToLower()
        if (-not $respuesta) { Falla 'no elegiste ninguna skill.' }
        if ($respuesta -in @('todas', 'todo', 't', '*')) {
            $elegidas = $catalogo
        } else {
            $elegidas = @()
            foreach ($n in ($respuesta -split '[,;\s]+' | Where-Object { $_ })) {
                if ($n -notmatch '^\d+$' -or [int]$n -lt 1 -or [int]$n -gt $catalogo.Count) {
                    Falla "«$n» no es un número de la lista (del 1 al $($catalogo.Count))."
                }
                $s = $catalogo[[int]$n - 1]
                if ($elegidas -notcontains $s) { $elegidas += $s }
            }
        }

        $tmp = Join-Path ([IO.Path]::GetTempPath()) ('diseno-de-soluciones-' + [guid]::NewGuid().ToString('N'))
        New-Item -ItemType Directory -Path $tmp | Out-Null
        try {
            if ($env:DDS_ORIGEN) {
                $origen = $env:DDS_ORIGEN
            } else {
                Write-Host 'Descargando Diseño de Soluciones…'
                [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
                $zip = Join-Path $tmp 'repo.zip'
                try {
                    Invoke-WebRequest -UseBasicParsing -Uri "https://codeload.github.com/$repo/zip/refs/heads/$rama" -OutFile $zip
                } catch {
                    Falla 'no se pudo descargar de GitHub. Revisa tu conexión.'
                }
                Expand-Archive -Path $zip -DestinationPath (Join-Path $tmp 'zip')
                $carpeta = Get-ChildItem (Join-Path $tmp 'zip') -Directory | Select-Object -First 1
                if (-not $carpeta) { Falla 'la descarga llegó vacía.' }
                $origen = $carpeta.FullName
            }

            $skills = Join-Path $destinoRepo '.claude\skills'
            New-Item -ItemType Directory -Force -Path $skills | Out-Null
            Write-Host ''
            foreach ($s in $elegidas) {
                $desde = Join-Path $origen $s.carpeta
                if (-not (Test-Path (Join-Path $desde 'SKILL.md'))) { Falla "la descarga no trae $($s.carpeta)\SKILL.md." }
                $nueva = Join-Path $tmp $s.carpeta
                Copy-Item -Recurse $desde $nueva
                Get-ChildItem $nueva -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force
                Get-ChildItem $nueva -Recurse -File -Filter '*.skill' | Remove-Item -Force

                $destino = Join-Path $skills $s.carpeta
                if (Test-Path $destino) {
                    $accion = 'actualizada'
                    $anterior = "$destino.anterior"
                    if (Test-Path $anterior) { Remove-Item -Recurse -Force $anterior }
                    Move-Item $destino $anterior
                    Move-Item $nueva $destino
                    Remove-Item -Recurse -Force $anterior
                } else {
                    $accion = 'instalada'
                    Move-Item $nueva $destino
                }
                Write-Host "  OK  $($s.carpeta) $accion" -ForegroundColor Green
            }
        } finally {
            Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
        }

        Write-Host ''
        Write-Host "Listo: $($elegidas.Count) skill(s) en $skills" -ForegroundColor Green

        # ---- Los scripts de apoyo de algunas skills usan Python 3.8 o superior
        $hayPython = $false
        foreach ($c in @('python', 'python3', 'py')) {
            $cmd = Get-Command $c -ErrorAction SilentlyContinue
            if ($cmd -and $cmd.Source -notlike '*WindowsApps*') {
                & $c -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' 2>$null
                if ($LASTEXITCODE -eq 0) { $hayPython = $true; break }
            }
        }
        if (-not $hayPython) {
            Write-Host 'Ojo: no encontré Python 3.8 o superior. Las skills funcionan igual, pero sus scripts de cálculo y reportes lo necesitan: https://www.python.org/downloads/' -ForegroundColor Yellow
        }

        Write-Host ''
        Write-Host 'Siguiente paso: abre Claude Code en tu carpeta y pide lo que necesites (ej: «audita este flujo»):'
        Write-Host "  cd `"$destinoRepo`"; claude"
    } catch {
        if ($_.Exception.Message -ne 'instalacion-cancelada') {
            Write-Host "No se pudo instalar: $($_.Exception.Message)" -ForegroundColor Red
        }
    }
}
