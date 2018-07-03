import sys
from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'include_files': [
            'image1.png',
            'image2.png'
        ],
        'path': sys.path + ['modules']
    }
}

executables = [
    Executable('SnakeApple.py')
]

setup(name='advanced_cx_Freeze_sample',
      version='0.1',
      description='Advanced sample cx_Freeze script',
      options=options,
      executables=executables
      )
