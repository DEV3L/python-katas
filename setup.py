from setuptools import setup, find_packages

setup(
    name='python_katas',
    packages=find_packages(),
    version='0.1',
    description='A Python GitHub repository for practicing katas.',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    url='https://github.com/DEV3L/python_katas',
    download_url='https://github.com/DEV3L/python_katas/tarball/0.1',
    keywords=['dev3l', 'python', 'kata',],
    install_requires=[
        'pytest',
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
