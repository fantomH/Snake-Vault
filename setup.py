# :----------------------------------------------------------------------- INFO
# :[Snake-Vault/setup.py]
# /author        : fantomH
# /created       : 2024-05-19 13:50:18 UTC
# /updated       : 2024-05-20 16:23:28 UTC
# /description   : "Setup script for Snake-Vault"

from setuptools import (
    setup,
    find_packages
)

setup(
    name='Snake-Vault',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'python-magic',
    ]
)
