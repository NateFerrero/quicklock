from distutils.core import setup
setup(
  name = 'quicklock',
  packages = ['quicklock'],
  version = '0.1.7',
  description = 'A simple Python resource lock to ensure only one process at a time is operating with a particular resource.',
  author = 'Nate Ferrero',
  author_email = 'nateferrero@gmail.com',
  url = 'https://github.com/NateFerrero/quicklock',
  download_url = 'https://github.com/NateFerrero/quicklock/tarball/0.1.7',
  keywords = ['lock', 'locking', 'singleton', 'process', 'resource', 'exclusive lock'],
  classifiers = [],
  platforms='any',
  install_requires = [
    'psutil>=2.2'
  ]
)
