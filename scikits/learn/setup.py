from os.path import join, dirname
import numpy
from Cython.Distutils import build_ext

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('learn',parent_package,top_path)
    config.add_subpackage('em')
    config.add_subpackage('datasets')
    config.add_subpackage('feature_selection')
    config.add_subpackage('glm')
    config.add_subpackage('manifold')
    config.add_subpackage('utils')

    include_dirs = []
    if top_path != '':
         # so that top-level setup.py could build
        include_dirs += [join(dirname(__file__), 'src')]

    config.add_extension('libsvm',
                         define_macros=[('LIBSVM_EXPORTS', None),
                                        ('LIBSVM_DLL',     None)],
                         sources=[join('src', 'libsvm.pyx'),
                                  ],
                         include_dirs=['/usr/include/libsvm-2.0/libsvm']
                                      + include_dirs,
                                      # [numpy.get_include()] +
                         libraries=['svm'],
                         depends=[join('src', 'libsvm_helper.c'),
                                  ])

    config.add_extension('BallTree',
                         sources=[join('src', 'BallTree.cpp')],
                         include_dirs=[numpy.get_include()]
                         )


    return config

    config.add_subpackage('utils')
    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(cmdclass={'build_ext': build_ext},
          **configuration(top_path='').todict())
