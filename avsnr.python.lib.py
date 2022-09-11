import requests,re

query = input('Name Library ⁿʳ: ')
url = f'https://pypi.org/search/?q={query}&o='

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en,ar;q=0.9,en-US;q=0.8',
    'cache-control': 'no-cache',
    'cookie': '_ga=GA1.2.320732397.1655244515; _gid=GA1.2.418333840.1662563556; session_id=L0K-7HpFT80GJ_aAVti3oUhy1cx9Ej1jFs9e-x_q3EM.Yxofww.GXXa2UButDeNxJetUl44Y62DlzBOQqqvPlEPO6m1M3XiWWC1ASi9Tq0dc8Kthcm_ChCKM8ZfkJ6Ox-r1z_KEQA',
    'pragma': 'no-cache',
    'referer': 'https://pypi.org/search/?q=search',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

req = requests.get(url , headers=headers).text
q = re.findall('<span class="package-snippet__name">(.*?)</span>', req)

for i in range(len(q)):
    print(q[i])
    
