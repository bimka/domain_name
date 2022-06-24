import re

urls = [
    "http://github.com/carbonfive/raygun", # "github"
    "http://www.zombie-bites.com",# "zombie-bites"
    "https://www.cnet.com", # "cnet"
    "http://google.com", # "google"
    "http://google.co.jp", # "google"
    "www.xakep.ru", # "xakep"
    "https://youtube.com", #"youtube"
    123123,
]

def domain_name(url: str) -> str:
    try:
        domain: str = re.findall(r'([^w/\.][\w-]+)\.', url)[0]
        return domain
    except TypeError as error:
        print(error)

if __name__ == '__main__':
    for url in urls:
        print(domain_name(url))
   