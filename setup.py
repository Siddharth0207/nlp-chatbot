from setuptools import setup, find_packages

setup(
    name='nlp_chatbot',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List of dependencies, or leave this empty if using requirements.txt
    ],
    entry_points={
        'console_scripts': [
            # Example: 'nlp-chatbot=nlp_chatbot.cli:main',
        ],
    },
    author='Siddharth Gautam Kushwaha',
    author_email='siddharthkushwaha33@gmail.com',
    description='A simple NLP-based chatbot using Transformers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Siddharth0207/nlp-chatbot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
