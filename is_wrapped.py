
def is_wrapped(func_name):
    # Get the function object from the name
    try:
        func = globals()[function_name]
        key = func.key
        
        if key == "wrapped":
            return True,func
        else:
            return False,None
        
    except:
        return False,None
