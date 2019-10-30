from distutils.core import setup, Extension

# define the extension module
contour_module = Extension('contour', 
                    sources=['contour_module.cpp'],
                    extra_compile_args=['-std=c++11']
                 )

# run the setup
setup(ext_modules = [contour_module])

