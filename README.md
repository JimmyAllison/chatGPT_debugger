# ChatGPT Debugger
This package allows you to debug Python code with the help of **ChatGPT3**, a large language model developed by OpenAI. Instead of just getting an error message when running your code, you will get a more detailed explanation of why the error occurred, how to fix it, and a corrected version of the code. This can save you time and effort in trying to figure out why your code is not working, and give you a better understanding of how to fix it. The package integrates ChatGPT3's advanced language processing capabilities to provide you with accurate and helpful debugging information. Whether you're a beginner or an experienced programmer, the ChatGPT_debugger can help you write better and more efficient code.

## Instructions

1. Install:

```
pip install chatGPT_debugger
```

2. How to Debug Python code with ChatGPT_debugger:

The ChatGPT_debugger package offers an easy way to debug your Python code. To use it, simply add the debug decorator to the function you want to debug. For example:

```python
from chatGPT_debugger.chatGPT_debugger import debug

@debug
def calculate_age(date_of_birth:int) -> int:
    current_year = "2023"
    age = current_year - date_of_birth
    return age
    
calculate_age(2000)
```

By using the debug decorator, instead of encountering an error, you will receive output explaining why the error occurred, how to fix it, and the corrected code, among other things."

3. The Benefits of ChatGPT_debugger

The ChatGPT_debugger package is an extremely useful tool for beginner Python programmers. Debugging code can often be a challenging and time-consuming task, especially for those who are just starting out. With the ChatGPT_debugger, however, debugging is made simple and intuitive. By simply adding the debug decorator to your code, you can receive detailed information about any errors or issues, including explanations, suggestions for fixing the problem, and corrected code. This makes it easier for beginner programmers to identify and resolve problems, allowing them to focus on writing and improving their code. The ChatGPT_debugger is an excellent resource for anyone looking to streamline their debugging process and become more confident in their Python programming skills.
