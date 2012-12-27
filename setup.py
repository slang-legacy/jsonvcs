from distutils.core import setup

setup(
	name='mongo_vcs',
	version='0.0.1',
	author='Sean Lang',
	author_email='slang800@gmail.com',
	packages=['mongo_vcs'],
	scripts=[],
	url='',
	license='LICENSE',
	description='version control for documents in MongoDB',
	long_description=open('README.rst').read(),
	install_requires=[
		"pymongo >= 2.4.1",
		"json_tools >= 0.1.30",
	],
)
