import datetime
import sys, os
from src.tools.post_file import post_file
from src.tools.create_path import create_puth


def app():
    flag = False
    while not flag:
        r = post_file('main.py', 'AgAAAAAcYqxYAADLWwWpsXAbJ0eYp9noiVDT8To')
        if r.status_code == 201:
            flag = True
        else:
            create_puth('AgAAAAAcYqxYAADLWwWpsXAbJ0eYp9noiVDT8To')

    print(post_file('main.py', 'AgAAAAAcYqxYAADLWwWpsXAbJ0eYp9noiVDT8To'))
    # option = [i for i, x in enumerate(sys.argv[1:]) if x == '--file'] or len(sys.argv)
    # option = option[0]
    # text = ' '.join(sys.argv[:option:])
    # file_name = sys.argv[option+2:]
    # if len(file_name) > 0
    #     print(os.path.exists(file_name[0]))
