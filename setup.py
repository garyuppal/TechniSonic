from distutils.core import setup

setup(
    name='TechniSound',
    author='Gary Uppal',
    version='0.1dev',
    packages=['technisound'],
#    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    install_requires=[
                    'numpy',
                    'scikit-learn',
                    'jupyterlab',
                    'ipykernel',
                    'matplotlib',
                    'seaborn',
                    'pandas',
                    'scipy',
                    'sounddevice'
                    ],
    entry_points={
        'console_scripts': [
            'tsound=technisound.cli:main'
        ]
    },
    python_requires=">=3.8",
)
