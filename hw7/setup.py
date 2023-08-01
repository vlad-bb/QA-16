from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder_vby2023',
    version='0.0.1',
    description='Very useful code',
    url='http://github.com/dummy_user/useful',
    author='Flying Circus',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['colorama'],
    entry_points={'console_scripts': ['sort = clean_folder.main:clean']}
)