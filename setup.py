#!/usr/bin/env python

from setuptools import setup, find_packages

import io
import os
import sys
import textwrap
import argparse

setup(
    name="kiran-tests",
    version="1.0.0",
    description="Kiran automated test",
#    keywords='kiran-tests',
    # 通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=find_packages(),
#    packages_data={''},
    package_data = {
        'tests': ['*.ini'],
        'tests': ['features/apps/atril/*.feature',
            'features/apps/eom/*.feature',
            'features/apps/engrampa/*.feature',
            'features/apps/firefox/*.feature',
            'features/apps/gnote/*.feature',
            'features/apps/gucharmap/*.feature',
            'features/apps/mate-font-viewer/*.feature',
            'features/apps/mate-power-statistics/*.feature',
            'features/apps/mate-search-tool/*.feature',
            'features/apps/openapp/*.feature',
            'features/apps/pluma/*.feature',
            'features/kiran/calculator/*.feature',
            'features/kiran/control-center/*.feature',
            'features/kiran/controlpanel/*.feature',
            'features/kiran/panel/*.feature',
            
            ],
#        'data': ['images/*'],
    },
    data_files=[
    ('/usr/share/kiran-tests/files', ['data/files/engrampa-yasuo']),
    #('/usr/share/kiran-tests/images', ['data/images/kylin-shotwell.png']),
    ],
    entry_points={
          'console_scripts': [
              'kiran-tests = src.__main__:main'
          ]
    },
    install_requires=['dogtail','parse','parse_type','six','behave']
)
