from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='mysqlwrapperpackage',
      version='0.2',
      description='MySQL Python Wrapper Package',
      long_description=long_description,
      url='https://github.com/Sharonsyra/MySQLWrapperPackage',
      author='Sharon Waithira',
      author_email='sharonwaithii@gmail.com',
      license='MIT',
      install_requires=[
          'pymsql',
          'injector',
      ],
      packages=['MySQLWrapperPackage'],
      zip_safe=False)
