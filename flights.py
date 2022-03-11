from requests_html import HTMLSession
import inpt

whereto=""
fromm=""
def fly():
    global whereto
    if whereto == "":
        inpt.typing()
        fromm = input("\rEnter your home location\n")
        inpt.typing()
        whereto = input("\rWhere do you want to fly?\n")
    session=HTMLSession()
    url = "https://www.google.com/search?q=flights+to+" + whereto +"from"+fromm
    try:
        r = session.get(url)
        r.html.render()
        print('Airline Name :',r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[1]/span[1]/text()'),end='\t\t')
        print('Time Duration :',r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[1]/span[2]/text()'),end='\t\t')
        print('Flight Type :',r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[1]/span[3]/text()'),end='\t\t')
        print('Price Starting From :',r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[1]/span[4]/span/text()'))
        aa=r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[1]/@href')
        print(aa[0])
        print('Airline Name :', r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[2]/span[1]/text()'),end='\t\t')
        print('Time Duration :', r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[2]/span[2]/text()'),end='\t\t')
        print('Flight Type :', r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[2]/span[3]/text()'),end='\t\t')
        print('Price Starting From :', r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[2]/span[4]/span/text()'))
        bb = r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[2]/@href')
        print(bb[0])
        print('Airline Name :', r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[3]/span[1]/text()'),end='\t\t')
        print('Time Duration :', r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[3]/span[2]/text()'),end='\t\t')
        print('Flight Type :', r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[3]/span[3]/text()'),end='\t\t')
        print('Price Starting From :', r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[3]/span[4]/span/text()'))
        cc = r.html.xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[3]/@href')
        print(cc[0])
        inpt.typing()
        print('\rBOOK NOW!')
    except:
        print('\rNot Found Try Again')
    print('\n','Could\'nt find what you are looking for?\n Try to be specific with your search')