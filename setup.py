from distutils.core import setup

long_description = ''

try:
    import subprocess
    import pandoc

    process = subprocess.Popen(
        ['which pandoc'],
        shell=True,
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    pandoc_path = process.communicate()[0]
    pandoc_path = pandoc_path.strip('\n')

    pandoc.core.PANDOC_PATH = pandoc_path

    doc = pandoc.Document()
    doc.markdown = open('README.md').read()

    long_description = doc.rst

except:
    pass

setup(
  name = 'quicklock',
  packages = ['quicklock'],
  version = '0.1.3',
  description = 'A simple Python resource lock to ensure only one process at a time is operating with a particular resource.',
  author = 'Nate Ferrero',
  author_email = 'nateferrero@gmail.com',
  url = 'https://github.com/NateFerrero/quicklock', # use the URL to the github repo
  download_url = 'https://github.com/NateFerrero/quicklock/tarball/0.1.3',
  keywords = ['lock', 'locking', 'singleton', 'process', 'resource', 'exclusive lock'],
  classifiers = [],
)
