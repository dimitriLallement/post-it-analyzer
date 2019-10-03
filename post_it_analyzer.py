import sys, getopt
import cv2
from color_analysis import nearest_color


DEFAULT_LANGUAGE = "en"
USAGE = "post_it_analyzer.py [-h|--help] [-v|--version=] [-l|--language=] <language>"
VERSION = "1.0"

#TODO replace print by logger / Add return code manager / Add unit test

def main(argv, language = DEFAULT_LANGUAGE):
    """ Main function """
    try:
        opts, args = getopt.getopt(argv,"hlv",["help","language=", "version"])

    except getopt.GetoptError:
        #Command line syntax errors
        print("Syntax error. Usage: {}".format(USAGE))
        sys.exit(2)

    language = DEFAULT_LANGUAGE

    #Options management    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("Usage: {}".format(USAGE))
            sys.exit()

        elif opt in ("-l", "--language"):
            if not arg:
                print("Syntax errror, missing parameter.\nUsage: {}".format(USAGE))
                sys.exit(1)
            language = arg

        elif opt in ("-v", "--version"):
            print("Version : {}".format(VERSION))
            sys.exit(0) 

    #TODO add core code here
    file = input("File: ").strip()
    image = cv2.imread(file)
    result = nearest_color(file)
    print(result)
    

if __name__ == "__main__":
    try:
        main(sys.argv[1:])

    except Exception as e:
        print(e.args) 
        print(e.__cause__) 