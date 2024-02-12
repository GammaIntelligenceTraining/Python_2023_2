import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                         ' (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
usd_yen_url = 'https://www.google.com/search?q=usd+to+yen&sca_esv=9a94bee5ed3f9006&sxsrf=ACQVn0-3p2Zd7yjiULl7O1O5__1M3TMbIg%3A1707747351641&source=hp&ei=FyjKZY2DJcLUxc8Pw4a2gAg&iflsig=ANes7DEAAAAAZco2J_lnlI_Kf300aFQ3sOGb8E27TaKz&ved=0ahUKEwjN6ojS_qWEAxVCavEDHUODDYAQ4dUDCA0&uact=5&oq=usd+to+yen&gs_lp=Egdnd3Mtd2l6Igp1c2QgdG8geWVuMg8QIxiABBiKBRgnGEYYggIyChAAGIAEGBQYhwIyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEjwVlC2QViBUXABeACQAQCYAVWgAcIEqgECMTC4AQPIAQD4AQGoAgrCAgcQIxjqAhgnwgIKECMYgAQYigUYJ8ICCxAAGIAEGIoFGJECwgIQEC4YgAQYigUYQxjHARjRA8ICCxAuGIAEGMcBGNEDwgIFEC4YgATCAgoQABiABBiKBRhDwgIHEAAYgAQYCg&sclient=gws-wiz'
eur_aud_url = 'https://www.google.com/search?q=eur+to+aud&sca_esv=9a94bee5ed3f9006&sxsrf=ACQVn08XlpfbiarJMnReEHtokpBYfXsTNw%3A1707747364743&ei=JCjKZfv_LLu-wPAP8PyS8Ac&ved=0ahUKEwj7oarY_qWEAxU7HxAIHXC-BH4Q4dUDCBA&uact=5&oq=eur+to+aud&gs_lp=Egxnd3Mtd2l6LXNlcnAiCmV1ciB0byBhdWQyChAAGIAEGIoFGEMyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARIiEFQvxZYozxwBngBkAEAmAGzAaABtgmqAQQxNy4xuAEDyAEA-AEBqAIUwgIKEAAYRxjWBBiwA8ICDRAAGIAEGIoFGEMYsAPCAgsQABiABBiKBRiRAsICChAjGIAEGIoFGCfCAg8QIxiABBiKBRgnGEYYggLCAhkQABiABBiKBRhGGIICGJcFGIwFGN0E2AEBwgIHECMY6gIYJ8ICExAAGIAEGIoFGEMY6gIYtALYAQLCAhAQLhjHARjRAxiABBiKBRgnwgILEC4YgAQYxwEY0QPCAgwQABiABBiKBRhDGArCAh0QLhjHARjRAxiABBiKBRiXBRjcBBjeBBjgBNgBA8ICDxAAGIAEGIoFGEMYRhiCAsICGxAAGIAEGIoFGEMYRhiCAhiXBRiMBRjdBNgBAcICChAAGIAEGBQYhwLiAwQYACBBiAYBkAYKugYGCAEQARgTugYGCAIQARgBugYGCAMQARgU&sclient=gws-wiz-serp'

def convert(url):
    response = requests.get(url, headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        element = soup.find('span', class_='DFlfde SwHCTb')
        return float(element.get('data-value'))
        # rate = float(element.string.replace(',', '.'))
        # return rate
    else:
        print('Error connecting.')

print(100 * convert(usd_yen_url))
# convert(usd_yen_url)
print(100 * convert(eur_aud_url))