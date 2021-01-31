from setuptools import setup

setup(
    name='HumbleBrag-CLI',
    version='1.0',
    packages=['cli', 'cli.commands'],
    author='Ben',
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points="""
        [console_scripts]
        humble_brag=cli.cli:cli
    """,
)
