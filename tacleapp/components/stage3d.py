# tacleapp/components/stage3d.py
import reflex as rx

class Stage3d(rx.Component):
    library = "stage3d"   # ⇠ el mismo nombre que pusiste en pcconfig.json
    tag = "Stage3d"       # ⇠ igual que la función exportada
    is_default = True     # ⇠ porque exportas default


stage3d = Stage3d.create
