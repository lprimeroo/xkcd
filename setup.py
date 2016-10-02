from setuptools import setup, find_packages

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

setup(
    name="xkcd-wallpaper",
    version="1.0",
    author="saru95",
    install_requires=open(os.path.join(BASE_DIR, "requirements.txt")).readlines(),
    license="MIT",
    description="Script that sets the latest XKCD comic as your wallpaper",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'xkcd-wallpaper=xkcdwall.cmd:set_wallpaper'
        ]
    }
)
