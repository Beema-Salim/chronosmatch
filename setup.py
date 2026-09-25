from setuptools import setup
from Cython.Build import cythonize


setup(
    name="chronosmatch-engine",
    ext_modules=cythonize(
        "src/chronosmatch/engine/matching_engine.pyx",
        language_level=3,
    ),
)