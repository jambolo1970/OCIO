from setuptools import setup, find_packages

setup(
    name="OCIO",
    version="1.0.0",
    description="Promemoria per sbattere le palpebre e ridurre secchezza oculare",
    author="TuoNome",
    packages=find_packages(),
    py_modules=["OCIO"],
    install_requires=[
        "Pillow>=11.0"
    ],
    entry_points={
        "console_scripts": [
            "OCIO=OCIO:OcioApp"
        ]
    },
    include_package_data=True,
)
