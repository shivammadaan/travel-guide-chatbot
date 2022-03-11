import time
import dest
import hotels
import flights
import outpt


def typing():
    er=".."
    for i in range(3):
        print("\r",er*(i+1),end="")
        time.sleep(0.5)
typing()
line='\rHey how can i help you? \nare you looking for\n1.Destination Guide\n2.Hotels\n3.Air Tickets\n'
def inp():
    time.sleep(1)
    global line
    x=input(line)
    x=x.lower()
    hey=('hi','hey','hy','hello')
    how=('how are you','how you')
    if x in hey:
        typing()
        line="\rhello user \n"
        return True
    elif x in how:
        typing()
        line='\ri\'m good hope you are fine \nhow can i help you \n1.Destination Guide\n2.Hotels\n3.Air Tickets\n'
        return True
    elif x=='1':
        typing()
        dest.des()
        return False
    elif x=='2':
        hotels.chotel()
        return False
    elif x=='3':
        flights.fly()
        return False
    else:
        typing()
        line='\rSorry I don\'t understand \nPlease try again\n'
        return True

def destinpt():
    option=input()
    if option=='a':
        typing()
        dest.destinfo()
    elif option=='b':
        typing()
        print("\r")
        hotels.shotel()


