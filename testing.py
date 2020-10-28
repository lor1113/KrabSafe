from requests_html import HTMLSession

def get_proxies():
    session = HTMLSession()
    url = 'https://free-proxy-list.net/'
    data = session.get(url)
    proxies = []
    proxy = ""
    switch = 0
    for each in data.html.find("table > tbody > tr > td"):
        if switch == 1:
            proxy = proxy + ":" + each.text
            proxies.append(proxy)
            switch = 0
        else:
            if "." in each.text:
                proxy = each.text
                switch = 1
    return proxies

print(get_proxies())