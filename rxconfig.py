import reflex as rx
from pathlib import Path

config = rx.Config(
    app_name="tacleapp",
    plugins=[rx.plugins.TailwindV3Plugin()],
    frontend_packages=[
        "three",
        "@react-three/fiber",
        "@react-three/drei",
        "leva"
    ],
)
