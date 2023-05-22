from setuptools import find_packages, setup

with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

with open("requirements.txt") as f:
    INSTALL_LIBRARIES = f.read().splitlines()


setup(
    name="blazekit",
    version="0.0.2",
    author="Rishabh Jain",
    author_email="rishabhking05@gmail.com",
    description="UI to interact with Kubernetes Clusters",
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=INSTALL_LIBRARIES,
    keywords=[
        "python",
        "kubernetes",
        "aws cli",
    ],
    project_urls={
        "Source Code": "https://github.com/rishabhjain05/BlazeKit",
    },
    classifiers=[],
)