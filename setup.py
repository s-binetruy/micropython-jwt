import sys
from setuptools import setup

# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
sys.path.append(".")
import sdist_upip


setup(
    name="micropython-jwt",
    version="0.1.0",
    description="JWT generator",
    author="Stephane Binetruy",
    author_email="jwt@binetruy.fr",
    url="https://github.com/s-binetruy/micropython-jwt",
    packages=["ujwt"],
    package_dir = {'': 'src'},
    install_requires=['micropython-hmac', 'micropython-base64'],
    cmdclass={"sdist": sdist_upip.sdist},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT license (MIT)",
        "Operating System :: Other OS",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
