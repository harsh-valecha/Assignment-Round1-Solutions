import requests
from bs4 import BeautifulSoup

# data lists
email = []
phone = []
social = []

# sending get request
##r = requests.get("https://ful.io/")
##if r.status_code == 200:
##    # fetching page source code
##    with open("index.html","wb") as f:
##        f.write(r.content)



# scraping information from html file
with open("index.html","rb") as f:
    soup = BeautifulSoup(f,'html.parser')
    for link in soup.find_all('a'):

        href = link.get('href')
        # social links
        if href.startswith('https://'):
            if ("facebook" in href) or ("linkedin" in href):
                social.append(href)

        if ('mailto' in href):
            email.append(href)
            
        # contact
        if href.startswith('tel:'):
            phone.append(href[4:])


# Output
print("Social Links - ")
for i in social:
    print(i )
print()
print("Email:")
for i in email:
    print(i, end = '\n')
print()
print('Contact:')
for i in phone:
    print(i)
    




