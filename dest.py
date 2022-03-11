import inpt
from requests_html import HTMLSession
place=''
def des():
    global place
    place=input('\rWhere would you like to travel\n')
    session = HTMLSession()
    url="https://www.google.com/maps/place/"+place
    try:
        r=session.get(url)
        r.html.render()
        about = r.html.xpath('/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[7]/div[1]/span/span/text()')
        inpt.typing()
        print("\r",about[0])
        inpt.typing()
        print("\rPLAN YOUR TRIP NOW!")
        inpt.typing()
        print(f"\ra. Find top attractions in {place}")
        inpt.typing()
        print(f"\rb. Find best hotels in {place}")
        inpt.destinpt()
    except:
        print('\rNot Found Try Again')

def destinfo():
    global place
    session = HTMLSession()
    url = "https://www.google.com/search?q=Top+sights+in+" + place
    try:
        r=session.get(url)
        r.html.render()
        print('\r',r.html.xpath('/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[3]/div/preview-carousel/div[2]/g-scrolling-carousel/div[1]/div/div/span/div[1]/a/div/div[2]/span[1]/text()'))
        print(r.html.xpath('/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[3]/div/preview-carousel/div[2]/g-scrolling-carousel/div[1]/div/div/span/div[2]/a/div/div[2]/span[1]/text()'))
        print(r.html.xpath('/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[3]/div/preview-carousel/div[2]/g-scrolling-carousel/div[1]/div/div/span/div[3]/a/div/div[2]/span[1]/text()'))
        print(r.html.xpath('/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[3]/div/preview-carousel/div[2]/g-scrolling-carousel/div[1]/div/div/span/div[4]/a/div/div[2]/span[1]/text()'))
        print(r.html.xpath('/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[3]/div/preview-carousel/div[2]/g-scrolling-carousel/div[1]/div/div/span/div[5]/a/div/div[2]/span[1]/text()'))
    except:
        print('\rNot Found Try Again')
