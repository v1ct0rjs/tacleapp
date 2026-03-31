import reflex as rx
from dotenv import load_dotenv

load_dotenv()

config = rx.Config(
    app_name="tacleapp",
    plugins=[rx.plugins.TailwindV3Plugin()],
    # Configuracion local para que el frontend conecte al backend sin ambiguedades.
    frontend_port=3000,
    backend_port=8000,
    frontend_host="127.0.0.1",
    backend_host="127.0.0.1",
    env=rx.Env.DEV,
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)
