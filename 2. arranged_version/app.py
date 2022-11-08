API_KEY = '3ebf52c0-3ebf52c0'
EMAIL_ADDR= 'hzwedt@gmail.com'
PASSWORD = 'asdfghjkl2'

url = f"https://example.com/api/?api_key={API_KEY}"
line = '= '*30

print(line)
print("This is my API url", url)
print(line)

login_info = {'email': EMAIL_ADDR,'password': PASSWORD}
print("Login info is", login_info)
print(line)
