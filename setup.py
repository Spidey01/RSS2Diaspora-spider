import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RSS2Diaspora-Spider-spidey01",
    version="0.0.1",
    author="Terry M. Poulin",
    author_email="BigBoss1964@gmail.com",
    description="An RSS spider to Diaspora post bot.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Spidey01/RSS2Diaspora-spider",
    packages=setuptools.find_packages(),
    scripts=[
        'bin/rss2diaspora-spider'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
)
