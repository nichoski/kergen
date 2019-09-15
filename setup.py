from distutils.core import setup

setup(
    name = 'kergen',
    scripts = ['kergen/kergen', 'kergen/kergen-map', 'kergen/depgen'],
    data_files=[('/usr/share/kergen', ['kergen/modules.alias'])],
    version = '0.1.5',
    description = 'Linux kernel config generator',
    author = 'Pavel Nichoski',
    author_email = 'nichoski@gmail.com',
    url = 'https://github.com/nichoski/kergen',
    license = 'Apache License Version 2.0',
    classifiers = [
        'License :: OSI Approved :: Apache License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Operating System :: Linux',
        'Development Status :: 1 - Open Beta',
        'Intended Audience :: System Administrators',
    ],
)
