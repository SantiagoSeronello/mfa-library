import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MFA",
    version="1.0.0",
    author="Santiago",
    author_email="santiago.seronello@gmail.com",
    description="Commom MFA processes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={

    },
    classifiers=[

    ],
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)









