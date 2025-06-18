import reflex as rx
from typing import Optional

# Patch Reflex port handling for compatibility with new psutil versions.
try:  # pragma: no cover - runtime patch only
    import psutil
    import reflex.utils.processes as processes

    def _patched_get_process_on_port(port: int) -> Optional[psutil.Process]:
        """Return the process listening on ``port`` if any."""
        for proc in psutil.process_iter(attrs=["pid", "name"]):
            try:
                conn_func = getattr(proc, "net_connections", proc.connections)
                for conn in conn_func(kind="inet"):
                    if conn.laddr and conn.laddr.port == port:
                        return proc
            except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
                continue
        return None

    processes.get_process_on_port = _patched_get_process_on_port
except Exception:
    # Ignore patch failures (psutil not installed or import error)
    pass

config = rx.Config(
    app_name="tacleapp",
    plugins=[rx.plugins.TailwindV3Plugin()],
    frontend_packages=["three", "@react-three/fiber", "@react-three/drei", "leva"],
)