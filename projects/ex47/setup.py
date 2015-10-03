try:
	from setuptools import setup
	
expect ImportError:
	from distutils.core import setup
	
config = {
	'description': 'ex47',
	'author': 'Rajesh',
	'url': 'github',
	'download_url': 'github repository',
	'author_email': 'rtr@rtr.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'ex47_project'
}

setup(**config)
