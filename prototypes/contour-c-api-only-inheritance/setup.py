from distutils.core import setup, Extension

# define the extension module
contour_module = Extension('contour', 
                    sources = ['Contour.cpp', 'contour_module.cpp'],
                    headers = ['Contour.h'],
                    extra_compile_args = ['-std=c++11']
                 )

# run the setup
setup(
  name = 'contour',
  ext_modules = [contour_module]
)

