try:
	from setuptools import setup
	
expect ImportError:
	from distutils.core import setup
	
config = {
	'description': 'Website for Rajesh Family Trust',
	'author': 'Rajesh Raghavakurup',
	'url': 'http://www.github.com',
	'download_url': 'http://www.github.com',
	'author_email': 'rajeshkurup@live.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['rajesh_family_trust'],
	'scripts': [],
	'name': 'rajesh_family_trust'
}

setup(**config)
