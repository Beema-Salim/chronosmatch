from setuptools import Extension, setup
from Cython.Build import cythonize


extensions = [
    Extension(
        "chronosmatch.engine.matching_engine",
        ["src/chronosmatch/engine/matching_engine.pyx"],
    ),
    Extension(
        "chronosmatch.engine.cython_order_book",
        ["src/chronosmatch/engine/cython_order_book.pyx"],
    ),
]


setup(
    name="chronosmatch-engine",
    ext_modules=cythonize(
        extensions,
        language_level=3,
    ),
    package_dir={"": "src"},
)