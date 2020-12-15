from setuptools import setup, find_packages

setup(
    name='Head First: vsearch4web',
    packages=find_packages(),
    version='0.1',
    description='A simple web app that searches for items within a string.',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    url='https://github.com/DEV3L/python_katas',
    keywords=['dev3l', 'python', 'head first', 'hf', 'flask', ],
    install_requires=[
        'flask==1.0',
    ],
    classifiers=[
        'Environment :: Web',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Beer-Ware License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Flask :: Hello World'],
)
