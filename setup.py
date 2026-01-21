from setuptools import setup, find_packages

setup(
    name="ocio",
    version="1.0.0",
    description="Promemoria per sbattere le palpebre e ridurre secchezza oculare",
    author="TuoNome",
    packages=find_packages(),
    py_modules=["ocio"],
    install_requires=[
        "Pillow>=11.0"
    ],
    entry_points={
        "console_scripts": [
            "ocio=ocio:OcioApp"
        ]
    },
    include_package_data=True,
)
