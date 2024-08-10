# 📎[Web de links](https://web-links-hazel.vercel.app/)

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.4.5+-5646ED?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)](https://reflex.dev)

## Proyecto desarrollado con [Python](https://www.python.org/) y [Reflex](https://reflex.dev/) que representa un sitio web personal estilo "[link in bio](https://web-links-hazel.vercel.app/)"

Seguí el tutorial del repositorio [python-web](https://github.com/mouredev/python-web) de [mouredev](https://mouredev.com/) para aprender sobre está tecnología para construir páginas web con código python puro.

## Requisitos

#### Instala y crea un entorno virtual [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) en la raíz del proyecto
Mac/Linux: `python3 -m pip install virtualenv`

Windows: `py -m pip install --user virtualenv`

`python3 -m venv .venv`

#### Activa el entorno virtual 
Mac/Linux: `source .venv/bin/activate`

Windows: `.\.venv\Scripts\activate`

Para desactivar el entorno virtual: `deactivate`

## Dependencias
*(Con el entorno virtual activo)*

`pip install reflex`

También las tienes en `requirements.txt`

`python -m pip install -r requirements.txt`

## Ejecución
`reflex run`

`reflex run --loglevel debug` *(modo debug)*

Acceder a [http://localhost:3000](http://localhost:3000) (frontend) y a [http://localhost:8000](http://localhost:8000) (backend)

## Despliegue

### Frontend

build.ps1 contiene las instrucciones necesarias para empaquetar el frontend del proyecto de manera local (Windows en mi caso).

`build.ps1`

```powershell
venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
Remove-Item public
reflex init
reflex export --frontend-only
Expand-Archive frontend.zip public
Remove-Item frontend.zip
deactivate
```

*Prepera el entorno, instala dependencias, inicializa el proyecto, crea la construcción de producción, y la descomprime.*

> El proyecto se puede desplegar en cualquier proveedor o servidor que soporte recursos estáticos.
> 
> [Éste proyecto](https://webb-links-hazel.vercel.apps/) se encuentra desplegado en [Vercel](https://vercel.com).

Configuración en Vercel:

* Se ha asociado el repositorio de GitHub al proyecto (para que cada `push` en la rama `main` desencadene un nuevo despliegue)
* Build & Development Settings: Other
* Root Directory: `public` (que contiene el empaquetado estático para producción)

### Backend

En proceso ...

<img src="https://media.giphy.com/media/lrtNcS63iXYMgEodrf/giphy.gif" width="70">
