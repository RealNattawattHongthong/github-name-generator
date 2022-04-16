import names , requests
from colorama import *
url_base = 'https://github.com/'


amount = int(input(Fore.LIGHTRED_EX + 'Enter the number of users that do you want to gen >  '))
print("Powered By nattawatt#8556")

for i in range(amount):
    url = url_base + (names.get_first_name())
    r = requests.get(url)
    

    if r.status_code == 200:
        print(Fore.GREEN + "[Valid link] => " + Fore.RESET + url)
        open('github.log', 'a+').write(url + "\n")
    else:
        print(Fore.RED + "[Invalid link] => " + Fore.RESET + url , r.status_code)
