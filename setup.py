from setuptools import find_packages, setup

setup(
    name="django-rest-captcha",
    version="0.3.0",
    author="evgeny.zuev",
    author_email="zueves@gmail.com",
    description="Lightweight version of django-simple-captcha for work with django-rest-framework",

    packages=find_packages(),
    package_data={'rest_captcha': ['fonts/*', '*.png']},
    python_requires='>=3.6',
    install_requires=[
        'djangorestframework>=3.5',
        'django',
        'pillow>=4.3.0'
    ]
)
