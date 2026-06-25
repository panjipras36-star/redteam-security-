from setuptools import setup

setup(
    name="recon11",
    version="1.1",
    py_modules=["recon11"],
    entry_points={
        'console_scripts': [
            'recon11=recon11:display_banner', 
        ],
    },
)
