from setuptools import setup, find_packages

version = '4.3.2.dev0'

setup(name='customplone.app.locales',
      version=version,
      description="Translation files for Plone",
      long_description=open("README.md").read(),
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
        ],
      keywords='plone i18n locale translation',
      author='Plone Foundation',
      author_email='vasnake@gmail.com',
      url='http://pypi.python.org/pypi/plone.app.locales',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['customplone', 'customplone.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      )
