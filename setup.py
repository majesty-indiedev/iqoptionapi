"""The python wrapper for IQ Option API package setup."""
from setuptools import (setup, find_packages)
from iqoptionapi.version_control import api_version

setup(
    name="yhaps-iqoptionapi",
    version=api_version,
    packages=find_packages(),
    install_requires=["pylint", "requests", "websocket-client==0.56"],
    include_package_data=True,
    description="IQ Option API Fork By Yhaps",
    long_description="Most updated IQ Option wrapper for Python",
    url="https://github.com/majesty-indiedev/iqoptionapi",
    author="M.H",
    zip_safe=False
)
