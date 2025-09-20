from setuptools import setup, find_packages

setup(
    name="neurochip",
    version="0.1.0",
    description="A software for microchip programming and neurosciences development.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Jules",
    author_email="",
    url="https://github.com/example/neurochip",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Embedded Systems",
    ],
    python_requires=">=3.8",
)
