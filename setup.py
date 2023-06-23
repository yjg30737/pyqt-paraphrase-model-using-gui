from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-paraphrase-model-using-gui',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'huggingface_gui': ['hf-logo.svg']},
    description='Using paraphrase(text2text generation) model from huggingface in Python desktop app',
    url='https://github.com/yjg30737/pyqt-paraphrase-model-using-gui.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.14',
        'huggingface_hub',
        'transformers',
    ]
)