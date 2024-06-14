from print_color import Color

def get_user_input(message: str, choices: str = None, extra_newline: bool = False):

    if choices == None:
        result = input(Color.MAGENTA + message + " => " + Color.END)
    else:
        result = input(Color.YELLOW + message + " : " + Color.INPUT + choices + " => " + Color.END)

    if extra_newline:
        print()

    return result
    