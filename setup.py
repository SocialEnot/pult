from setuptools import setup, find_packages

setup(name='Remote',
    version = '0.1',
    packages = find_packages(),
    options = {
        'app': {
            'formal_name': 'TV Remote',
            'bundle': 'org.tv.remote'
        },
        'ios': {
            'app_requires': [
               'toga-ios',
               'git+https://github.com/tonybaloney/pyviera-1.git@master#egg-info=pyviera'
            ]
        }
    }
)