from setuptools import setup
setup(
    name = 'hypermd',
    version = '0.0.0',
    packages = ['hypermd'],
    entry_points = { 'console_scripts': [
        'hypermd = hypermd.__main__:main'
    ]},
    author="Henry Blanchette",
    description="A more versatile markdown format for the web.",
    url="https://github.com/Riib11/HyperMD"
)