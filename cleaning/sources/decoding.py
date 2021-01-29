import ast

def decoding(string):
    result = string
    try:
        result = ast.literal_eval(string)
    finally:
        result = result.decode() if isinstance(result, bytes) else string
    return result