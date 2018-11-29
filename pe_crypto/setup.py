from setuptools import setup, find_packages


setup(
    name = 'pe_crypto',
    version = '1.0',
    py_modules = ['pe_crypto'],
    install_requires = [
        'click',
        'cryptography'
    ],
    entry_points = '''
        [console_scripts]
        pe_crypto = pe_crypto:_cli
    '''
)
