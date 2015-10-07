try:
	from setuptools import setup
	
expect ImportError:
	from distutils.core import setup
	
config = {
	'description': 'Gothonweb',
	'author': 'My Name',
	'url': 'http://www.github.com',
	'download_url': 'http://www.github.com',
	'author_email': 'My Email',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['gothonweb'],
	'scripts': [],
	'name': 'gothonweb'
}

setup(**config)
