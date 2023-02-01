import os
import keyring

        
def store_api_key():
    save_permenant = os.environ.get("save_flag")
    if save_permenant == "True" or save_permenant is None:
        api_key = keyring.get_credential(service_name="chatGPT_debugger",username=None)
        if api_key is None or api_key.password == "null":
            api_key = input("Enter your OpenAI API key: ")
            try:
                keyring.set_password(service_name="chatGPT_debugger",username="User",password=api_key)
                os.environ["save_flag"] = "True" 
            except:
                os.environ["API_KEY"] = api_key
                os.environ["save_flag"] = "False"
        else:
            api_key = api_key.password

    else:
        api_key = os.environ.get("API_KEY")
        if api_key is None or api_key == "null":
            api_key = input("Enter your OpenAI API key: ")
            os.environ["API_KEY"] = api_key


    return api_key,save_permenant
