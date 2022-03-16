from parser import translate

num = int
symbol = str
Atom = (num, symbol)


def repl(prompt='Team 0108 Lisp> '):
    while True:
        val = eval(translate(input(prompt)))
        if val is not None: 
            print(schemestr(val))

def schemestr(exp):
    if isinstance(exp, list):
        return '(' + ' '.join(map(schemestr, exp)) + ')' 
    else:
        return str(exp)
    
def atom(token: str) -> Atom:
    """this returns an atom type either interger or a string"""
    try: return int(token)
    except ValueError:
        return symbol(token)