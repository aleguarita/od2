from setuptools import setup, find_packages


def le_arquivo(nome):
    with open(nome, 'r', encoding='utf-8') as file:
        return file.read()


setup(
    name="od2aag",
    version='0.0.1',
    packages=find_packages(),
    author='Alessandro Guarita',
    description='Módulo para Old Dragon 2',
    long_description=le_arquivo('README.md'),
    long_description_content_type='text/markdown',
    LICENCE='MIT',
    python_requires='>=3.11',
)

