import setuptools

with open("README.md","r") as f:
    long_description = f.read()

setuptools.setup(
    name="zyutil",
    version="0.0.1",
    author="zhaoyi",
    author_email="zhaoyi.hb@gmail.com",
    description="util",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        ""
    ]

)