from setuptools import setup


setup(
    name='randword',
    description='A Python package for generation random English words',
    keywords=[
        'python', 'package', 'python-package', 'random',
        'word', 'words', 'generator', 'generation',
        'random-word', 'random-words', 'random-word-generator',
        'random-word-generation', 'english',
        'english-word', 'english-words'
    ],
    version='2.3.1',

    author='Artyom Bezmenov (8nhuman)',
    author_email='artem.bezmenov02@gmail.com',
    license='MIT',

    packages=['randword'],
    include_package_data=True,

    project_urls={ 
        'Bug Tracker': 'https://github.com/8nhuman8/randword/issues',
        'Source Code': 'https://github.com/8nhuman8/randword',
        'Download': 'https://github.com/8nhuman8/randword/archive/2.3.1.tar.gz',
        'Homepage': 'https://github.com/8nhuman8/randword'
    },

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ]
)
