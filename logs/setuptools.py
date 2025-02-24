from setuptools import setup, find_packages

setup(
    name='RLPMixer',
    version='0.1.0',
    author='dondre stewart',
    author_email='dondrestewart111@gmail.com',
    description='A reinforcement learning-powered pixel generation model.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tusjsrrrftt/RLPMixer.git',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'torch',
        'numpy',
        'matplotlib',
        'tqdm',
        'PyYAML',
        'tensorboard',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
