import os
from setuptools import setup

setup(
    name="ambassadors.openclips",
    version=open("VERSION").readline().strip() if os.path.exists("VERSION") else "0.0.0",

    packages=[
        "ambassadors",
        "ambassadors.openclips",
    ],

    namespace_packages=["ambassadors", ],

    test_suite="tests"
)
