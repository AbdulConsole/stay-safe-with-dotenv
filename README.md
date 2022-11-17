# USING .env TECHNIQUE TO HIDE DATA, KEYS AND SECRETS TOKENS OR API_KEYS

1. pip install python-dotenv
2. arrange secrets
3. Create a file named '.env', from dotenv import load_dotenv and call load_dotenv() also import os---- now use os.getenv("API_KEY") to asses variables from.env file
4. Create '.gitignore' add the fiile and push 

This is an instance of a file where the API_KEY, email and password have been hidden in the environmental variables.

## Saved into '.env' file
```
API_KEY = '3ebf52c0-3ebf52c0'
EMAIL_ADDR= 'hzwedt@gmail.com'
PASSWORD = 'asdfghjkl2'
```
## '.gitignore' also created

with content: ```.env```

# Credit
1. Creator of Python programming language 
2. Creator of git and GitHub 
3. Author of python-dotenv library
4. ...
