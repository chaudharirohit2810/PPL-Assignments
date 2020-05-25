import time
from datetime import datetime
hosts_path = "/etc/hosts"

redirect = "127.0.0.1"

website_list = []
website = input("Enter the website you want to block: ")
website_list.append(website)
print(website_list)
with open(hosts_path, 'r+') as file:
    content = file.read()
    for website in website_list:
        if website in content:
            pass
        else:
            file.write(redirect + " " + website + "\n")

