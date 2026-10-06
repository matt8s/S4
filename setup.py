#!/usr/bin/env python3
"""Build configuration for the S4 Python extension."""

from pathlib import Path
import os
import shlex
import sys

import numpy as np
from setuptools import Extension, setup


def _split_paths(value):
    if not value:
        return []
    return [path for path in value.split(os.pathsep) if path]


def _split_flags(value):
    return shlex.split(value) if value else []


root = Path(__file__).resolve().parent
objdir = Path(os.environ.get("S4_OBJDIR", root / "build"))
libfile = Path(os.environ.get("S4_LIBFILE", objdir / "libS4.a"))

if not libfile.is_absolute():
    libfile = (root / libfile).resolve()

if not libfile.exists():
    raise RuntimeError(
        f"Native S4 library not found at {libfile}. "
        "Build it first with 'make S4_pyext' or the appropriate platform Makefile."
    )

cxx_runtime = os.environ.get(
    "S4_CXX_RUNTIME",
    "c++" if sys.platform == "darwin" else "stdc++",
)

extension = Extension(
    "S4",
    sources=["S4/main_python.c"],
    include_dirs=[np.get_include(), *_split_paths(os.environ.get("S4_INCLUDE_DIRS"))],
    libraries=[cxx_runtime] if cxx_runtime else [],
    library_dirs=_split_paths(os.environ.get("S4_LIBRARY_DIRS")),
    runtime_library_dirs=(
        []
        if os.name == "nt"
        else _split_paths(os.environ.get("S4_RUNTIME_LIBRARY_DIRS"))
    ),
    extra_objects=[str(libfile)],
    extra_link_args=_split_flags(os.environ.get("S4_LINK_FLAGS")),
    extra_compile_args=_split_flags(
        os.environ.get("S4_COMPILE_FLAGS", "-std=gnu99")
    ),
)

setup(ext_modules=[extension])
