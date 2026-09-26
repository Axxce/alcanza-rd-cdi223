# Alcanza RD

Sitio web del proyecto académico CDI-223 de UNICARIBE sobre economía familiar y costo de vida. La candidata Laura Méndez es ficticia.

## Publicación

Vercel sirve los archivos de `dist/` mediante la configuración de `vercel.json`. La carpeta `dist/` se incluye en el repositorio para que Vercel publique el sitio sin dependencias ni pasos de compilación.

Para ponerlo en línea desde una sesión de Vercel:

1. En **Add New → Project**, importa el repositorio `Axxce/alcanza-rd-cdi223` desde GitHub.
2. Conserva el directorio raíz del repositorio y selecciona **Other** si Vercel pide un framework. `vercel.json` define `dist` como directorio de salida; no hace falta configurar un comando de compilación.
3. Pulsa **Deploy**. Vercel generará la dirección pública y publicará las actualizaciones posteriores de la rama `main`.

## Actualizar contenido

Las páginas se generan desde `build.py`, con estilos en `theme.css` y el menú en `menu.js`. Para regenerarlas:

```bash
python3 build.py
```

Confirma los cambios de los archivos fuente y de `dist/` en GitHub. La próxima implementación en Vercel tomará la versión actualizada del repositorio.

El proyecto conserva los campos de sustentantes y matrículas pendientes de completar antes de la entrega académica.
