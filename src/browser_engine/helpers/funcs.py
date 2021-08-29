from src.browser_engine.helpers.CONSTANTS import WHITESPACE, ASCII_DIGIT, ASCII_ALPHA


def is_whitespace(string):
    return all([char in WHITESPACE for char in string])


def inside(constant, char):
    """
    NORMALLY THE STATEMENT "" in "any_string" WILL RETURN TRUE, THIS FUNCTION AVOIDS THAT
    READ AS: "IF INSIDE CONSTANT IS CHAR"
    """

    if char != "":
        return char in constant
    else:
        return False


def is_name_code_point(char):
    return is_name_start_code_point(char) or (char in ASCII_DIGIT) or (char == "-")


def is_name_start_code_point(char):
    return inside(ASCII_ALPHA, char) or is_non_ascii_code_point(char) or char == "_"


def is_non_ascii_code_point(char):
    # ASCII is a 7 bit encoding, 2^7 = 128.
    # ∴, any char with code point > 128 is a non ascii character
    return ord(char) > 128
