import inspect
import os
import keyring
from chatGPT_debugger.engine import get_response 
from chatGPT_debugger.store_api_key import store_api_key

def call_chatGPT(funcs,line_number,e):
    sources = []
    for func in funcs:
        source = inspect.getsource(func)
        sources.append(source)
    
    if len(sources) == 1:
        ques = f"""I'm Stuggling with an Error in line {line_number}, the error says \n {e}. and Here is the code 
        {sources[0]} \n\n
        please provide the answer with these informations:
            01. why this error occurs (Note: Give Indepth Explanation)
            02. how to fix this error
            03. Corrected Code (Note: only write is you're very confident with the answer)

        Also when you submitting the output don't write my notes again.
        """
    else:
        ques = f"""
        I'm Stuggling with an Error in line {line_number}, the error says \n {e}.and Here is the code 
        {sources[0]} \n\n.
        """
        for source in sources[1:]:
            ques += f"/n {source}"
        
        ques += """/n please provide the answer with these informations:
            01. why this error occurs (Note: Give Indepth Explanation)
            02. how to fix this error
            03. Corrected Code (Note: only write is you're very confident with the answer)

        Also when you submitting the output don't write my notes again."""
        
    ques = ques.replace("@debug" ,"")
    
    api_key,save_permenant = store_api_key()
        
    response = get_response(ques,api_key)

    return f"\033[32m{response}\033[0m"
