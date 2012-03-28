from setuptools import setup
import sys, os

README = open(os.path.join(os.path.dirname(__file__), 'README')).read()

version = 0.1

setup(
    name="NoseTwilio",
    version=version,
    description="Nose plugin to only run TwilioTestCase tests",
    long_description=README,
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Natural Language :: English',
      'Programming Language :: Python :: 2.7',
      'Topic :: Software Development :: Testing'
    ],
    keywords='nose twilio',
    author='Chad Gallemore',
    author_email='cgallemore@gmail.com',
    url='https://github.com/cgallemore/nose-twilio',
    license='BSD',
    entry_points = {
        'nose.plugins.0.10': [ 'twilio-filtering =  nosetwilio:NoseTwilio']
    },
    py_modules = ['nosetwilio'],
    install_requires = ['nose>=0.10.1']
)