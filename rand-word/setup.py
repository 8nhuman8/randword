from setuptools import setup


setup(
    name='rand-word',
    description='A Python package for generation random English words',
    keywords=['generation', 'word', 'random', 'english', 'python', 'package'],
    version='0.1',

    author='Artyom Bezmenov (8nhuman)',
    author_email='artem.bezmenov02@gmail.com',

    url='https://github.com/8nhuman8/rand-word',
    license='MIT',

    package_data={'': ['*.txt']},

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 1 - Planning'
    ]
)
