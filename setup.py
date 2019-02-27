#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name='MyQR',
    version='1.1',
    license='MIT',
    author_email='yujia.wang@tradingfront.cn',
    url='https://github.com/wukaMM/qrcode',
    description='Python qrcode',
    platforms=['any'],
    py_modules= ['MyQR'],
    packages= ['MyQR','MyQR.mylibs'],
    install_requires=['imageio', 'numpy', 'olefile', 'Pillow'],
    include_package_data=True,
)

