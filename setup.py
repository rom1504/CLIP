import os

import pkg_resources
from setuptools import setup, find_packages
from pathlib import Path

if __name__ == "__main__":

    # Read description from README
    with Path(Path(__file__).parent, "README.md").open(encoding="utf-8") as file:
        long_description = file.read()

    setup(
        name="clip-anytorch",
        long_description=long_description,
        long_description_content_type="text/markdown",
        description=long_description.split("\n")[0],
        url="https://github.com/rom1504/CLIP",
        py_modules=["clip"],
        version="2.5.0",
        author="OpenAI",
        packages=find_packages(exclude=["tests*"]),
        install_requires=[
            str(r)
            for r in pkg_resources.parse_requirements(
                open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
            )
        ],
        include_package_data=True,
        extras_require={'dev': ['pytest']},
    )
