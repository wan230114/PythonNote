from bs4 import BeautifulSoup
import requests

url = "https://ftp.ncbi.nlm.nih.gov/repository/clone/reports/Mus_musculus/"
url = "https://ftp.ncbi.nlm.nih.gov/repository/clone/reports/Homo_sapiens/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
res = requests.get(url, headers=headers)

t = BeautifulSoup(res.text, features="html.parser")
for x in t.find_all("a"):
    if x["href"].startswith("RP11"):
        print(url + x["href"])
