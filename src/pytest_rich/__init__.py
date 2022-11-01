import contextlib

try:
    from importlib import metadata
except ImportError:  # Python < 3.8
    import importlib_metadata as metadata  # type: ignore

with contextlib.suppress(metadata.PackageNotFoundError):
    __version__ = metadata.version(__name__)
