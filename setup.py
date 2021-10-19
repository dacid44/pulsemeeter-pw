import os
import sys
from setuptools import setup

data_files = [
    ('share/licenses/pulsemeeter/', ['LICENSE']),
]

for directory, _, filenames in os.walk(u'share'):
    dest = directory[6:]
    if filenames:
        files = [os.path.join(directory, filename) for filename in filenames]
        data_files.append((os.path.join('share', dest), files))

setup(
    name='pulsemeeter',
    version='1.1',
    description='A pulseaudio audio routing application',
    author='Gabriel Carneiro',
    author_email='therealcarneiro@gmail.com',
    license="MIT",
    license_files='LICENSE',
    url='https://github.com/theRealCarneiro/pulsemeeter',
    packages=['pulsemeeter'],
    install_requires=['gobject'],
    data_files=data_files,
    entry_points={
        "console_scripts": [
            "pulsemeeter = pulsemeeter.__main__:main",
        ],
    },
    scripts=[
        'scripts/pmctl',
    ],
    include_package_data=True
)
