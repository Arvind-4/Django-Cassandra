try:
    print("Production settings loaded.")
    from .production import *
except ImportError:
    print("Local settings loaded.")
    from .local import *
