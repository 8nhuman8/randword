from setuptools import setup


setup(
    name='randword',
    description='A Python package for generation random English words',
    keywords=['generation', 'word', 'random', 'english'],
    version='2.0.2',

    author='Artyom Bezmenov (8nhuman)',
    author_email='artem.bezmenov02@gmail.com',
    license='MIT',

    packages=['randword'],
    include_package_data=True,

    project_urls= {
        'Homepage': 'https://github.com/8nhuman8/randword',
        'Download': 'https://github.com/8nhuman8/randword/archive/2.0.2.tar.gz',
        'Source Code': 'https://github.com/8nhuman8/randword',
        'Bug Tracker': 'https://github.com/8nhuman8/randword/issues'
    },

    #url='https://github.com/8nhuman8/randword',
    #download_url='https://github.com/8nhuman8/randword/archive/2.0.1.tar.gz',

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ]
)
