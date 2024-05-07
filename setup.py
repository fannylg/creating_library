# setup.py
from setuptools import setup

setup(
    name='practica2_plots',
    version='0.1',
    py_modules=['plot_functions'],
    install_requires=[
        'matplotlib',
        'seaborn',
        'pandas',
    ],
    author='equipo6',
    description='Librería para crear visualizacion de datos continuos y discretos para el DCD',
    keywords='plotting, matplotlib, histogram, bar chart, box plot, heatmap',
)