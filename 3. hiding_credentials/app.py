from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
PASSWORD = os.getenv("PASSWORD")
url = f"https://app.com/api/?api_key={API_KEY}"
line = '= '*30
print(line)
print("This is my API url", url)
print(line)

login_info = {'email': EMAIL_ADDR,'password': PASSWORD}
print("Login info is", login_info)
print(line)