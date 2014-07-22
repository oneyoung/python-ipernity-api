from distutils.core import setup

with open('README.txt') as f:
    long_description = f.read()

setup(name='ipernity_api',
      version='0.13',
      description='Python Ipernity API',
      long_description=long_description,
      author='oneyoung',
      author_email='guowangyang@gmail.com',
      url='https://github.com/oneyoung/python-ipernity-api',
      license='Apache 2.0',
      packages=['ipernity_api'],
      platforms=['any'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 2 :: Only',
          'Topic :: Utilities',
      ],)
