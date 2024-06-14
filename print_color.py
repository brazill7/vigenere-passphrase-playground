class Color:
    END = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

    WARNING = RED
    NORMAL = YELLOW
    IMPORTANT = CYAN
    DEBUG = GREEN
    INPUT = MAGENTA


class ColorOutputItem:
    def __init__(self, color: str, message: str):
        self.color = color
        self.message = message

def print_c(output_item_array: list[ColorOutputItem]):
    """
    Print colored messages to the console.

    Args:
        output_item_array (List[ColorOutputItem]): A list of ColorOutputItem objects
            representing debug messages to be printed.

    Each ColorutputItem object should have the following attributes:
        - message (str): The message to be printed.
        - color (str): ANSI escape code for the color of the message.
    """
    for item in output_item_array:
        print(item.color + item.message, end='')
    print(Color.END)