#!/usr/bin/env python
# @author Stefano Borini 

from distutils.core import setup

setup(name='graphstore',
      version='0.0.1',
      author="Stefano Borini",
      author_email="moc.liamg@inirob.onafets",
      maintainer="Stefano Borini",
      maintainer_email="moc.liamg@ypmehcoeht+inirob.onafets",
      description="Graph database storage",
      packages=[    'graphstore', 
                    "graphstore._graphstore.backends",
                    "graphstore._graphstore.graph",
                    ],
      package_dir={'graphstore' : 'graphstore'},
      )

