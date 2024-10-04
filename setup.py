from setuptools import setup, find_packages

setup(
    name='image_processing',
    version='0.1',
    description='Pacote para processamento de imagens e plotagem de gráficos',
    author='Kalew',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
