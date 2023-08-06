html = urlopen('https://www.snapdeal.com/products/academic-engineering-books?sort=plrty')
bs = BeautifulSoup(html.read(), 'html.parser')

session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
 'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
 'Accept':'text/html,application/xhtml+xml,application/xml;'
 'q=0.9,image/webp,*/*;q=0.8'}


try:
    html = urlopen('https://www.snapdeal.com/products/academic-engineering-books?sort=plrty')
except HTTPError as e:
    print(e)
else:
    print()

try:
    html = urlopen('https://www.snapdeal.com/products/academic-engineering-books?sort=plrty')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')

nev_collect = bs.findAll('p', {'class': 'product-title'})
for name in nev_collect:
    print(name.get_text())

ar_collect = bs.findAll('span', {'class': 'lfloat product-price'})
for ar in ar_collect:
    print(ar.get_text())

def scrape_product_details(url):
    resp = requests.get(url, headers=headers)




def main_driver():

    DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"
    wd = webdriver.Chrome(executable_path= DRIVER_PATH)
    wd.get("")

if __name__ == "__main_driver__":
    main_driver()
