#using .env method to hide data
1. pip install python-dotenv
2. arrange secrets
3. Create a file named '.env', from dotenv import load_dotenv and call load_dotenv() also import os---- now use os.getenv("API_KEY") to asses variables from.env file
4. Create '.gitignore' add the fiile and push 