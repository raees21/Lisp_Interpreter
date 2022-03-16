import sys

def tokenize(input_str):
    """
    Cleans and splits the input string into tokens
    :param input_str: the input string as a lisp expression
    :return: a list of tokens from the input string
    """

    # performs a syntax check and raises an error if the check fails
    valid = is_valid_syntax(input_str)
    if not valid:
        raise Exception("Syntax error!")
    
    string1 = input_str.replace("(", "( ")
    string2 = string1.replace(")", " )")
    result = string2.split()
    return result


def is_valid_syntax(input_str):
    """
    Perfoms the syntactic analysis by checking that the opening ( has a closing ).
    :param input_str: the input string as a lisp expression
    :return: boolean based on whether it satisfies the above condition or not
    """

    opening_count = input_str.count('(')
    closing_count = input_str.count(')')
    return (input_str.startswith('(')
        and input_str.endswith(')')
        and opening_count == closing_count)


def start_interpreter(input_str):
    tokens = tokenize(input_str)
    print(tokens)

if __name__ == '__main__':
    input_str = "(eq (car (10 20 30)) (* 2 5))"
    start_interpreter(input_str)

