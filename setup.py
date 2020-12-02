import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'semantic-release-pypi-example',
    packages = ['semantic_release_pypi_example'],
    license='MIT',
    description = '',
    author = 'abichinger',
    author_email = 'andreas.bichinger@gmail.com',
    url = 'https://github.com/abichinger/semantic-release-pypi',
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.3',
)