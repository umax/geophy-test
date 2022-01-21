import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gpgh",
    version="0.0.1",
    author="Max Usachev",
    author_email="maxusachev@gmail.com",
    description="Command line tool to analyze GitHub repos in an organization",
    packages=['gpgh'],
    py_modules=['cli'],
    install_requires=[
        'click==8.0.3',
        'pygithub==1.55',
        'requests==2.27.1',
    ],
    entry_points={
        'console_scripts': ['gpgh=cli:get_metrics'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
