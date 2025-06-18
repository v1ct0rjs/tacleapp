
from reflex.components.component import NoSSRComponent

class Stage3d(NoSSRComponent):
    library = "stage3d"
    tag = "Stage3d"
    is_default = True

stage3d = Stage3d.create

