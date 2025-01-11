from setuptools import setup


long_description: str = ""

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pystatx',
    version='0.1-1',
    description='statx(2) wrapper',
    url='https://github.com/ckarageorgkaneen/pystatx',
    packages=['statx'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    project_urls={
        'Tracker': 'https://github.com/ckarageorgkaneen/pystatx/issues',
        'Source': 'https://github.com/ckarageorgkaneen/pystatx',
    },
    license='GPLv3',
    python_requires='>=3.9',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development :: Libraries",
    ]
)
