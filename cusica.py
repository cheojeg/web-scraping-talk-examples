import requests

url = "http://www.cusica.com/home/ultimaMusicaAjax"

payload = ""
headers = {
    'accept': "*/*",
    'origin': "http://www.cusica.com",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded",
    'referer': "http://www.cusica.com/",
    'accept-encoding': "gzip, deflate",
    'accept-language': "es-US,es;q=0.9,es-419;q=0.8,en;q=0.7",
    'cookie': "_ga=GA1.2.1741539723.1522604541; _gid=GA1.2.1650168972.1522604541; CAKEPHP=cb9cfa534e6fbaa82caa14c316d523f9; _gat=1; _gat_UA-56745641-1=1",
    'cache-control': "no-cache",
    'postman-token': "66fab0d1-dca2-97f6-76d6-943564a20c94"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
