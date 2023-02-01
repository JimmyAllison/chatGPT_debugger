
import os
import openai
import socket
import keyring

def is_connected():
    try:
        # Try to connect to Google's website
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def get_response(prompt,api_key = None,max_tokens = 720):
    save_permenant = os.environ.get("save_flag")
    if api_key is None:
        print("\n\033[31mPlease Provide OpenAI's API_KEY. 404 ERROR!\033[0m")
        return None
        
    openai.api_key = api_key
    
    connected = is_connected()
    
    if not connected:
        print("\n\033[31mPlease Check Your Internet Connection. 404 ERROR!\033[0m")
        return None
    
    try:
        print(f"ChatGPT Investigating The Problem, Please wait a Moment...")
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt=prompt,
          temperature=0.7,
          max_tokens=max_tokens,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        return response["choices"][0]["text"]
    
    
    except openai.error.AuthenticationError as error:
        openai.api_key = None
        if save_permenant == "True" or save_permenant is None:
            keyring.set_password(service_name="chatGPT_debugger",username="User",password="null")
        else:
            os.environ["API_KEY"] = "null"
            
        print(f"\n\033[31m{error}\033[0m")
        return None
