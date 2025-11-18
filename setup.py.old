from setuptools import setup, find_packages

setup(
    name="sacctladpsync",
    version="1.0.41",
    py_modules=[
        "sacctldapsync",
        "ldaplib", 
        "SlurmAccountManagerV41",
        "__init__"
    ],
    packages=[
        "sacctladpsync.py_slurm_client",
        "sacctladpsync.rest_api_docs"
    ],
    package_dir={
        'sacctladpsync.py_slurm_client': 'py_slurm_client',
        'sacctladpsync.rest_api_docs': 'rest_api_docs'
    },
    install_requires=[
        "click>=8.3.0",
        "ldap3>=2.9.1",
        "pyyaml>=6.0.3", 
        "requests>=2.32.5",
        "openapi>=2.0.0",
        "openapi-client>=1.1.7",
    ],
    entry_points={
        'console_scripts': [
            'sacctladpsync=sacctldapsync:main',
        ],
    },
)