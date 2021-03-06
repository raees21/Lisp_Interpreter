
def get_list_indexes(tokens):
    """
    Gets indexes of open and closed brackets
    :param tokens: the tokens generated by the tokenizer
    :returns (list, list): lists of open and close brackets
    """

    open_list = []
    closed_list = []

    for i in range(len(tokens)):
        if tokens[i] == '(':
            open_list.append(i)
        elif tokens[i] == ')':
            closed_list.append(i)
    
    return open_list, closed_list


def sanitizer(tokens):
    """
    Stores tokens as known values that can be processed further
    :param tokens: the tokens generated by the tokenizer
    :returns (list): sanitized tokens
    """

    for i in range(len(tokens)):
        if tokens[i].isdigit():
            tokens[i] = int(tokens[i])
        else:
            tokens[i] = tokens[i].upper()

    return tokens


def translate(tokens):
    """
    Structures the code into and intermediate form where tokens
    are stored as known values that can be processed further.
    :params tokens: the tokens generated by the tokenizer
    :returns (list): intermediate form or Abstract Syntax Tree
    """

    results = []
    instructions = []

    open_list, closed_list = get_list_indexes(tokens)
    tokens = sanitizer(tokens)
    open_list.reverse()

    for i in closed_list:
        for j in open_list:
            if j < i:
                if '(' in tokens[j + 1: i]:
                    temp_list = []
                    temp_list.append(tokens[j + 1])
                    temp_list.append(results[-1])
                    results.append(temp_list)
                else:
                    temp_list = []
                    if results:
                        temp_list.append(results[-1])
                        temp_list.append(tokens[j + 1:i])
                    else:
                        temp_list = tokens[j + 1:i]
                    results.append(temp_list)
                open_list.remove(j)
                break

    instructions.append(results[-1])
    return instructions
