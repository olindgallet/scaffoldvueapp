#!/usr/bin/python3

from plumbum import local, colors
import sys
import re
import os

def show_directory_error_text():
    print(colors.orchid | '[Directories Not Found Error]')
    print(colors.yellow | '  Could not find necessary folders such as node_modules and assets.')
    print(colors.yellow | '  Make sure you\'re executing this in the folder created by npm init vue@3.')

def show_help_text():
     print(colors.orchid | '[Friendly Help Message]')
     print(colors.yellow | 'Usage: python3 scaffoldvueapp.py')
     print(colors.yellow | '  buildapp is used to start up a new app body with Vue.js and Bootstrap.')
     print(colors.yellow | '  Shell script originally made by Olin Gallet September 2017, upgraded February 2022')

def show_intro_text():
     print(colors.blue | '==*== Let\'s make a web app!  Scaffolding with vue.js, Bootstrap, and other goodies! ==*==')
     print(colors.orchid | '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⣀⣀⣶⣄')
     print(colors.orchid | '⠀⠀⠀⠀⠀⠀⠀⢀⡠⣔⠮⠍⠛⠒⠒⠒⠚⠠⠽⣉⠙⠻⢿⣿⣿⣷')
     print(colors.orchid | '⠀⠀⠀⠀⠀⣠⡂⠕⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠢⢀⡹⠛⠋⠑⡄')
     print(colors.orchid | '⠀⣀⣀⣠⣼⠏⠀⠀⠀⠀⠀⠀⠀⠜⠑⣄⠀⠀⠀⠀⠀⠠⠊⠀⠀⠀⠀⣷')
     print(colors.orchid | '⣿⣿⣿⣿⡏⠀⠀⠀⢸⠉⢆⠀⠀⢸⣀⣸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏')
     print(colors.orchid | '⣿⣿⣿⣿⠃⠀⠀⠀⠸⣄⣸⡆⠀⠈⢿⣿⣿⠀⣠⣴⣶⣶⡄⠀⢀⣤⣾⣇⣀⣀⡀')
     print(colors.orchid | '⣿⣿⣿⣿⣦⣄⠀⠀⠀⢻⣿⣿⠀⠀⠈⠻⡿⠀⠘⠛⠛⠋⠁⠸⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⡿⢿⣿⣿⣷⢀⣀⠀⠻⠿⢀⣴⣶⣶⡆⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⣦⣤⠛⣿⣿⣿⡿⠃⠀⠀⠹⣿⣿⣿⠇⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⣿⣿⣦⡈⣿⣿⠇⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃')
     print(colors.orchid | '⠉⠻⣿⣿⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃')
     print(colors.orchid | '⠀⠀⠀⠀⠛⢿⣿⣿⣿⣷⢦⣄⣀⡀⠤⣤⣤⣀⣀⣬⣿⣿⣿⣿⣿⣿⣿⠟⠁')
     print(colors.orchid | '⠀⠀⠀⢠⣴⣿⣿⣿⣿⣿⣦⣭⣷⣶⣿⣿⡿⠿⠟⠋⠁⠉⠛⠛⠿⠋⠁')
     print(colors.blue | '==*== Updated February 2022 <3 <3 <3 ==*==')

def show_outro_text():
     print(colors.blue | '==*== Scaffolding complete! ==*==')
     print(colors.orchid | '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⣀⣀⣶⣄')
     print(colors.orchid | '⠀⠀⠀⠀⠀⠀⠀⢀⡠⣔⠮⠍⠛⠒⠒⠒⠚⠠⠽⣉⠙⠻⢿⣿⣿⣷')
     print(colors.orchid | '⠀⠀⠀⠀⠀⣠⡂⠕⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠢⢀⡹⠛⠋⠑⡄')
     print(colors.orchid | '⠀⣀⣀⣠⣼⠏⠀⠀⠀⠀⠀⠀⠀⠜⠑⣄⠀⠀⠀⠀⠀⠠⠊⠀⠀⠀⠀⣷')
     print(colors.orchid | '⣿⣿⣿⣿⡏⠀⠀⠀⢸⠉⢆⠀⠀⢸⣀⣸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏')
     print(colors.orchid | '⣿⣿⣿⣿⠃⠀⠀⠀⠸⣄⣸⡆⠀⠈⢿⣿⣿⠀⣠⣴⣶⣶⡄⠀⢀⣤⣾⣇⣀⣀⡀')
     print(colors.orchid | '⣿⣿⣿⣿⣦⣄⠀⠀⠀⢻⣿⣿⠀⠀⠈⠻⡿⠀⠘⠛⠛⠋⠁⠸⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⡿⢿⣿⣿⣷⢀⣀⠀⠻⠿⢀⣴⣶⣶⡆⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⣦⣤⠛⣿⣿⣿⡿⠃⠀⠀⠹⣿⣿⣿⠇⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⣿⣿⣦⡈⣿⣿⠇⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃')
     print(colors.orchid | '⠉⠻⣿⣿⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃')
     print(colors.orchid | '⠀⠀⠀⠀⠛⢿⣿⣿⣿⣷⢦⣄⣀⡀⠤⣤⣤⣀⣀⣬⣿⣿⣿⣿⣿⣿⣿⠟⠁')
     print(colors.orchid | '⠀⠀⠀⢠⣴⣿⣿⣿⣿⣿⣦⣭⣷⣶⣿⣿⡿⠿⠟⠋⠁⠉⠛⠛⠿⠋⠁')
     print(colors.blue | '==*== Remember to use "npm run" to see options to run scripts! ==*==')

def create_directories():
     mkdir = local['mkdir']
     dirs_to_create =['src'+os.path.sep+'assets'+os.path.sep+'js',
                      'src'+os.path.sep+'assets'+os.path.sep+'css',
                      'src'+os.path.sep+'assets'+os.path.sep+'videos',
                      'src'+os.path.sep+'assets'+os.path.sep+'images',
                      'src'+os.path.sep+'assets'+os.path.sep+'audio']
     for dir in dirs_to_create:
         print(colors.yellow | f'  Creating directory: {dir}')
         mkdir(dir)

def install_npm_dependencies():
     bootstrap = local['npm']['install', 'bootstrap', '--save-prod']
     print(colors.yellow | '  Installing bootstrap. . .')
     print(colors.green | bootstrap.run()[1])

def install_grunt():
     grunt = local['npm']['install', '--save-dev', 'grunt']
     print(colors.yellow | '  Installing grunt. . .')
     print(colors.green | grunt.run()[1])
     grunt_concat = local['npm']['install', '--save-dev', 'grunt-contrib-concat']
     print(colors.yellow | '  Installing grunt-contrib-concat. . .')
     print(colors.green | grunt_concat.run()[1])
     grunt_uglify = local['npm']['install', '--save-dev', 'grunt-contrib-uglify']
     print(colors.yellow | '  Installing grunt-contrib-uglify. . .')
     print(colors.green | grunt_uglify.run()[1])
     grunt_copy = local['npm']['install', '--save-dev', 'grunt-contrib-copy']
     print(colors.yellow | '  Installing grunt-contrib-copy. . .')
     print(colors.green | grunt_copy.run()[1])

def copy_bootstrap_files():
     bs_css_srcdir = 'node_modules'+os.path.sep+'bootstrap'+os.path.sep+'dist'+os.path.sep+'css'
     bs_css_targetdir = 'src'+os.path.sep+'assets'+os.path.sep+'css'
     bs_js_srcdir = 'node_modules'+os.path.sep+'bootstrap'+os.path.sep+'js'+os.path.sep+'dist'
     bs_js_targetdir = 'src'+os.path.sep+'assets'+os.path.sep+'js'
     bs_bootstrap_css = local['cp'][bs_css_srcdir+os.path.sep+'bootstrap.css', bs_css_targetdir]
     print(colors.yellow, '  Copying bootstrap.css to css. . .')
     print(colors.green | bs_bootstrap_css.run()[1])
     bs_bootstrap_grid_css = local['cp'][bs_css_srcdir+os.path.sep+'bootstrap-grid.css',bs_css_targetdir]
     print(colors.yellow, '  Copying bootstrap_grid_css to css. . .')
     print(colors.green | bs_bootstrap_grid_css.run()[1])
     bs_bootstrap_reboot_css = local['cp'][bs_css_srcdir+os.path.sep+'bootstrap-reboot.css',bs_css_targetdir]
     print(colors.yellow, '  Copying bootstrap-reboot.css to css. . .')
     print(colors.green | bs_bootstrap_reboot_css.run()[1])
     bs_bootstrap_utilities_css = local['cp'][bs_css_srcdir+os.path.sep+'bootstrap-utilities.css', bs_css_targetdir]
     print(colors.yellow, '  Copying bootstrap-utilities.css to css. . .')
     print(colors.green | bs_bootstrap_utilities_css.run()[1])
     bs_button_js = local['cp'][bs_js_srcdir+os.path.sep+'button.js', bs_js_targetdir]
     print(colors.yellow | '  Copying bootstrap button.js to js. . .')
     print(colors.green | bs_button_js.run()[1])
     bs_collapse = local['cp'][bs_js_srcdir+os.path.sep+'collapse.js', bs_js_targetdir]
     print(colors.yellow | '  Copying bootstrap collapse.js to js. . .')
     print(colors.green | bs_collapse.run()[1])
     bs_dropdown = local['cp'][bs_js_srcdir+os.path.sep+'dropdown.js', bs_js_targetdir]
     print(colors.yellow | '  Copying bootstrap dropdown.js to js. . .')
     print(colors.green | bs_dropdown.run()[1])
     bs_popover = local['cp'][bs_js_srcdir+os.path.sep+'popover.js', bs_js_targetdir]
     print(colors.yellow | '  Copying bootstrap popover.js to js. . .')
     print(colors.green | bs_popover.run()[1])
     bs_tooltip = local['cp'][bs_js_srcdir+os.path.sep+'tooltip.js', bs_js_targetdir]
     print(colors.yellow | '  Copying bootstrap tooltip.js to js. . .')
     print(colors.green | bs_tooltip.run()[1])

if __name__ == '__main__':
     if len(sys.argv) > 1:
          show_help_text()
     elif not os.path.isdir('node_modules') or not os.path.isdir('src'+os.path.sep+'assets'):
          show_directory_error_text()
     else:
          show_intro_text()
          print(colors.orchid | '[Starting directory creation!]')
          create_directories()
          print(colors.orchid | '[Ending directory creation!]')
          print(colors.orchid | '[Starting npm dependency installation!]')
          install_npm_dependencies();
          install_grunt();
          print(colors.orchid | '[Ending npm dependency installation!]')
          print(colors.orchid | '[Starting file copying!]')
          copy_bootstrap_files();
          print(colors.orchid | '[Ending file copying!]')
          show_outro_text()
