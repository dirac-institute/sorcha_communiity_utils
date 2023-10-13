from sorcha_addons import activity
from sorcha_addons import lightcurve

__all__ = [
    "activity",
    "lightcurve",
]

# Version information (autogenerated by setuptools-scm)
try:
    from ._version import version as __version__
    from ._version import version_tuple
except ImportError:
    __version__ = "unknown version"
    version_tuple = (0, 0, "unknown version")
