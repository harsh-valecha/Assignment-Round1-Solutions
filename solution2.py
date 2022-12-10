import requests
from bs4 import BeautifulSoup

# data lists
email = []
phone = []
social = []


# reference lists
social_media = ["facebook","linkedin","github","youtube","twitter","instagram","discord"]
contact = ["tel:","phone:","mobile:"]


url= input("Enter URL:")

#sending get request
try :
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content,'html.parser')
        for link in soup.find_all('a'):
            if link.has_attr('href'):
                href = link.get('href')
                # social links
                if href.startswith('https://'):
                    social.extend([href for i in social_media if (i in href) and (href not in social)])

                # emails
                if ('mailto' in href):
                    mail = href.split('?')[0][7:]
                    email.append(mail)
                    
                # contact
                m1= href.lower()
                phone.extend([href.split(':')[1] for i in contact if i in m1])
    # Output
    print("Social Links - ")
    for i in social:
        print(i )
    print()
    print("Email/s - ")
    for i in email:
        print(i, end = '\n')
    print()
    print('Contact:')
    for i in phone:
        print(i)
        
    else:
        print(f"Response Status Code :{r.status_code}")
except Exception as err:
    print(err)





