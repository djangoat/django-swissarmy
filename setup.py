from setuptools import setup, find_packages

version = __import__('swissarmy').__version__

setup(
    name='django-swissarmy',
    version=version,
    description='Handy dandy things for Django',
    license='MIT',
    url='https://github.com/djangoat/django-swissarmy',
    author='Djangoat',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
)
