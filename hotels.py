from requests_html import HTMLSession

import dest
import inpt

city=''
def chotel():
    inpt.typing()
    global city
    city=input("\rSearch hotels in any city!\nEnter the city name:\n")
    session=HTMLSession()
    url = "https://www.google.com/travel/hotels/" + city
    try:
        r=session.get(url)
        r.html.render()
        print('A:',r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[1]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[1]/h2/text()'))
        print(r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[1]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]/text()'),'\t\t\tRating:',r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[1]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[2]/a/span/span/span/span[1]/span/span/span/span/span[1]/text()'))
        aa=r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[1]/c-wiz/div/a/@href')
        print('https://www.google.com'+aa[0])
        print('B:',r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[2]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[1]/h2/text()'))
        print(r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[2]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]/text()'),'\t\t\tRating:',r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[2]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[2]/a/span/span/span/span[1]/span/span/span/span/span[1]/text()'))
        bb=r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[2]/c-wiz/div/a/@href')
        print('https://www.google.com' + bb[0])
        print('C:',r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[3]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[1]/h2/text()'))
        print(r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[3]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]/text()'),'\t\t\tRating:',r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[3]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[2]/a/span/span/span/span[1]/span/span/span/span/span[1]/text()'))
        cc = r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[3]/c-wiz/div/a/@href')
        print('https://www.google.com' + cc[0])
        print('D:',r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[4]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[1]/h2/text()'))
        print(r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[4]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]/text()'),'\t\t\tRating:', r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[4]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[2]/a/span/span/span/span[1]/span/span/span/span/span[1]/text()'))
        dd = r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[4]/c-wiz/div/a/@href')
        print('https://www.google.com' + dd[0])


    except:
        print('\rNot Found Try Again')

def shotel():
    global city
    city=dest.place
    session = HTMLSession()
    url = "https://www.google.com/travel/hotels/" + city
    try:
        r = session.get(url)
        r.html.render()
        print(r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[1]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[1]/h2/text()'))
        print(r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[1]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]/text()'),'\t\t\tRating:', r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[1]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[2]/a/span/span/span/span[1]/span/span/span/span/span[1]/text()'))
        print(r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[2]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[1]/h2/text()'))
        print(r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[2]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]/text()'),'\t\t\tRating:', r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[2]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[2]/a/span/span/span/span[1]/span/span/span/span/span[1]/text()'))
        print(r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[3]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[1]/h2/text()'))
        print(r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[3]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]/text()'),'\t\t\tRating:', r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[3]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[2]/a/span/span/span/span[1]/span/span/span/span/span[1]/text()'))
        print(r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[4]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[1]/h2/text()'))
        print(r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[4]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]/text()'),'\t\t\tRating:', r.html.xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[4]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[2]/a/span/span/span/span[1]/span/span/span/span/span[1]/text()'))

    except:
        print('\rNot Found Try Again')

