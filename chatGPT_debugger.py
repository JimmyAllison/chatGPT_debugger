import traceback
import re
import functools
import os
from chatGPT_debugger.callAPI import call_chatGPT
from chatGPT_debugger.is_wrapped import is_wrapped

        

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print()
            print()
            tb = traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__)
            error = "\n".join(tb[-2:])
            print(error)
            line_number = re.search(r'line\s+(\d+)', error).group(1)
#             line_number = str(max(1,int(line_number) - 1))
            
            print(f"chatGPT Detected an error in line {line_number}")
            print("#" * 100)
            print()
            print(f"\033[31mError Message: {error}\033[0m")
            print("#" * 100)
            
            function_name = re.search(r'in\s+(\w+)', error).group(1)

            if function_name == func.__name__:
                response = call_chatGPT([func],line_number,error)
                print("_" * 100)
                print(response)
                print(f"_" * 100)
            
            else:
                wrapped_flag,error_func = is_wrapped(function_name)
                if wrapped_flag:
                    response = call_chatGPT([func,error_func],line_number,error)
                    print("_" * 100)
                    print(response)
                    print(f"_" * 100)
                    
                    
                else:
                    print()
                    print(f"""
                     \n\033[31mWarning: The error you're encountering occurs in a function named\033[0m <{function_name}>. \033[31mHowever, this function has not been Decorated, which may prevent ChatGPT from providing an effective solution. If possible, please Decorate the function and try again... (If this Warning appear for third party/ inbuild functions please ignore this warning.)\033[0m
                """
                         )
                    response = call_chatGPT([func],line_number,error)
                    print("_" * 100)
                    print(response)
                    print(f"_" * 100)
                    
    setattr(wrapper, "key", "wrapped")
    return wrapper
