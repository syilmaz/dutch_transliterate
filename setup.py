from setuptools import setup

setup(
   name='dutch_transliterate',
   version='0.1.0',
   author='syilmaz',
   author_email='syilmaz@handpickedagencies.com',
   packages=['german_transliterate'],
   url='http://github.com/syilmaz/dutch_transliterate',
   license='CC-BY-4.0 License',
   description='dutch_transliterate can clean and transliterate (i.e. normalize) Dutch text including abbreviations, numbers, timestamps etc.',
   long_description=open('README.md', encoding="UTF-8").read(),
   install_requires=[
       "num2words",
   ],
)
