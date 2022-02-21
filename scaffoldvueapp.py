from plumbum import local, colors
import sys
import re

def show_directory_exists_error_text(dir_name):
    print(colors.orchid | '[Directory Name Already Exists Error]')
    print(colors.yellow | f'  Directory name \'{sys.argv[1]}\' already exists.')

def show_directory_error_text(dir_name):
    print(colors.orchid | '[Directory Name Error]')
    print(colors.yellow | f'  Directory name \'{sys.argv[1]}\' cannot be used.')

def show_help_text():
     print(colors.orchid | '[Syntax Error]')
     print(colors.yellow | 'Usage: buildapp [projectname]')
     print(colors.yellow | '  buildapp is used to start up a new app body with Vue.js, Page.js, and Bootstrap for designing and Bower and Grunt for productivity.')
     print(colors.yellow | '  Shell script made by Olin Gallet September 2017, upgraded February 2022')

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

def create_directories(parent_dir):
     mkdir = local['mkdir']
     dirs_to_create =['js', 'css', 'assets', 'config', 'assets/videos', 'assets/images', 'assets/audio']
     mkdir(parent_dir)
     print(colors.yellow | f'  Creating directory: {parent_dir}')
     for dir in dirs_to_create:
         to_create = parent_dir + '/' + dir
         mkdir(to_create)
         print(colors.yellow | f'  Creating directory: {to_create}')

def create_routing_file(target_dir):
    echo = local['echo']
    js = "//put routing in this file, uses page.js\n"
    js = js + "page('/', index)";
    target_file = target_dir + '/js/routing.js'

    print(colors.yellow | f'  Creating routing file: {target_file}')
    (echo[js] > target_file)()

def validate_directory_name(dir_name):
    return bool(re.match(('^[a-zA-Z0-9_\- .]+$'), dir_name))

if __name__ == '__main__':
     if len(sys.argv) != 2:
          show_help_text()
     else:
         if local.path(sys.argv[1]).exists() and local.path(sys.argv[1]).is_dir():
              show_directory_exists_error_text(sys.argv[1])
         else:
             if validate_directory_name(sys.argv[1]):
                  show_intro_text()
                  print(colors.orchid | '[Starting directory creation!]')
                  create_directories(sys.argv[1])
                  print(colors.orchid | '[Ending directory creation!]')
                  print(colors.orchid | '[Starting file creation!]')
                  create_routing_file(sys.argv[1])
                  print(colors.orchid | '[Ending file creation!]')
             else:
                  show_directory_error_text(sys.argv[1])
