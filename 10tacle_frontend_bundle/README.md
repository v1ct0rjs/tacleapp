# 10tacle.org — Frontend estático detrás de Traefik (sin cambiar Traefik)

Este bundle sirve el `frontend.zip` exportado por Reflex con **Nginx** escuchando en `:3000` y
**alias de red `10tacle_app`**, de forma que Traefik puede seguir usando tu configuración actual:

- **Router**: `10tacle` (file provider)
- **Rule**: `Host("10tacle.org","www.10tacle.org")`
- **EntryPoints**: `websecure`
- **Service URL**: `http://10tacle_app:3000/`
- **Red Docker**: `proxy` (externa, la misma que usa Traefik)

## Pasos
1. Copia este directorio al servidor (por ejemplo `/opt/10tacle-frontend/`).
2. Copia tu `frontend.zip` al mismo directorio.
3. **Para minimizar downtime**:
   - Para el contenedor antiguo que ejecuta `reflex run` (el que resolvía como `10tacle_app`).
   - Ejecuta: `./deploy/deploy_frontend.sh ./frontend.zip`
4. Listo: Traefik seguirá resolviendo el backend `http://10tacle_app:3000/`, que ahora será el Nginx estático.

## Alternativa (casi cero downtime)
- Arranca este Nginx sin alias y escuchando en `:3000` con otro alias (p.ej. `10tacle_web`) y
  cambia **solo** la URL del servicio en `dynamic/dynamic_conf.yml` a `http://10tacle_web:3000/`.
  Traefik recargará automáticamente (`providers.file.watch: true`). Luego paras el antiguo.

## Rollback
- Para `10tacle_web`: `docker compose down`
- Vuelve a levantar tu contenedor anterior `reflex run` (o restaura la URL original en `dynamic_conf.yml` si la cambiaste).

## Estructura
- `docker-compose.yml`: Servicio Nginx con alias `10tacle_app` en la red `proxy`.
- `deploy/nginx.conf`: Nginx con fallback SPA y cache prudente.
- `deploy/deploy_frontend.sh`: Script que descomprime `frontend.zip` y levanta el servicio.
- `deploy/reflex-frontend/`: Carpeta donde se descomprime el build.
