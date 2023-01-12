import re

def domain_name(url: str):
    reg = r"^(http|https)?(:\/\/)?(www.)?([a-zA-Z0-9_]*)\.(\S*)"
    return re.search(reg, url).group(4)


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
