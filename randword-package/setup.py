from setuptools import setup


setup(
    name='randword',
    description='A Python package for generation random English words',
    keywords=['generation', 'word', 'random', 'english'],
    version='2.0',

    author='Artyom Bezmenov (8nhuman)',
    author_email='artem.bezmenov02@gmail.com',
    license='MIT',

    url='https://github.com/8nhuman8/randword',
    download_url='https://github.com/8nhuman8/randword/archive/2.0.tar.gz',

    packages=['randword'],

    include_package_data=True,

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ]
)
