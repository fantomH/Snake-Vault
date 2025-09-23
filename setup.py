# :: --------------------------------------------------------------------- INFO
# :: [Snake-Vault/setup.py]
# :: author        : Pascal Malouin @ github.com/fantomH
# :: created       : 2024-05-19 13:50:18 UTC
# :: updated       : 2025-09-23 17:34:28 UTC
# :: description   : "Setup script for Snake-Vault"

from setuptools import (
    setup,
    find_packages
)

setup(
    name='Snake-Vault',
    version='1.0.0',
    author="Pascal Malouin",
    author_email="pascal.malouin@gmail.com",
    description="Miscellaneous Python utils.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fantomH/Snake-Vault/",
    
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'lxml',
        'python-magic',
    ],
    entry_points={
        "console_scripts": [
            "snake-sqlite=snake_vault.snake_sqlite.cli:main"
        ]
    },
)
