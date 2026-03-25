from setuptools import setup, find_packages

setup(
    name='flask-bmi-calculator',
    version='1.0.0',
    description='Flask BMI Calculator Application',
    author='Flask BMI',
    python_requires='>=3.10',
    packages=find_packages(),
    install_requires=[
        'flask',
        'pymysql',
        'gunicorn',
    ],
    include_package_data=True,
)
