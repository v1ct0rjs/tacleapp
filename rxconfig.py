import reflex as rx
from dotenv import load_dotenv

load_dotenv()

config = rx.Config(
    app_name="tacleapp",
    plugins=[rx.plugins.TailwindV3Plugin()],
    # Agregar configuración para Docker
    frontend_port=3000,
    backend_port=8000,
    frontend_host="0.0.0.0",  # Escuchar en todas las interfaces
    backend_host="0.0.0.0",   # Escuchar en todas las interfaces
    env=rx.Env.PROD           # Configurar para producción
)
