from distutils.core import setup

setup(
    name='django-count-image-captcha',
    version='0.1',
    description='Captcha with image count challenge for Django 1.7+',
    long_description=open('README.md').read(),
    author='ELCODO',
    author_email='info@elcodo.pl',
    url='https://github.com/elcodo/django-count-image-captcha',
    packages=['image_count_captcha'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'],
    )
