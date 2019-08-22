from setuptools import setup, find_packages

setup(
    name='oidc_validators',
    version='0.5.0',
    description='Validates OIDC token',
    url='http://github.com/unit9/oidc-validators-python',
    author='Abirafdi Raditya Putra',
    author_email='raditya.putra@unit9.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'cryptography==2.7',
        'PyJWT==1.7.1'
    ],
    zip_safe=False,
    python_requires=">=3.7",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
