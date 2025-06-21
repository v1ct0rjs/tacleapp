import reflex as rx
from dotenv import load_dotenv


load_dotenv()

config = rx.Config(
    app_name="tacleapp",
    plugins=[rx.plugins.TailwindV3Plugin()],
)

