
'''
setup.py for pantry bell

'''

from distutils.core import setup
import os, glob

def get_version():

    '''return version from fixed always must exist file

       Making very broad assumptions about the 
       existence of files '''
    
    v = open('pantrybell/version.txt').read().strip()
    return v




def main():

    setup(name='pantrybell',
          version=get_version(),
          packages=['pantrybell'
                   ],
          author='Paul Brian',
          author_email='paul@mikadosoftware.com',
          url='https://github.com/lifeistillgood/pantrybell',
          license='BSD 3 Clause',
          description='Co-ordinating Jenkins Jobs',
          long_description='see description',
          install_requires=[
              "flask >= 0.8"
              ,"rhaptos2.common"
                           ],
          package_data={'pantrybell': ['templates/*.*', 'static/*.*', 'version.txt'],
                        },

          
          )



if __name__ == '__main__':
    main()

