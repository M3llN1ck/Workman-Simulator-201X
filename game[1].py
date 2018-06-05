print('Workman Simulator 20XX')
version=('0.5a')
def money_earn():
    """Earning money"""
    parameters[0]+=2
    parameters[2]-=1
    parameters[3]-=1
def eat_food():
    """Eating food"""
    parameters[0]-=1
    parameters[3]+=1
def play_games():
    """Playing games"""
    parameters[0]-=1
    parameters[2]+=1
def sleep():
    """Just sleep"""
    parameters[1]+=1
    parameters[0]-=1
parameters=[10,10,10,10]
while True:
    print('1.Start game')
    print('2.Controls')
    print('3.Credits')
    print('4.Exit dat shit!')
    choose=input('>>>')
    if choose==('1'):
        while True:
            print('Money:'+str(parameters[0]))
            print('Health:'+str(parameters[1]))
            print('Happiness:'+str(parameters[2]))
            print('Food:'+str(parameters[3]))
            print('1.Work')
            print('2.Buy food')
            print('3.Play games')
            print('4.Sleep')
            print('5.Shop')
            print('6.Exit to menu')
            gme=input('>>>')
            if gme==('1'):
                money_earn()
            elif gme==('2'):
                eat_food()
            elif gme==('3'):
                play_games()
            elif gme==('4'):
                sleep()
            elif gme==('5'):
                print('SOON')
                buy=input('>>>')
                if buy==('1'):
                    print('Pucharse successful!')
                else:
                    print('Soon')
            elif gme==('6'):
                break
            else:
                print('Are u fucking idiot??!!')
    elif choose==('2'):
        print('Just print numbers & press enter')
    elif choose==('3'):
        print('Made by MellNick with help of Vadim.2018')
    elif choose==('4'):
        print('Bye')
        break
    elif choose==('version'):
        print('The version is:'+version+'.')
        print('You can get the last version at github.com/')
        #The link doesn't exist!
    else:
       print('Fuck You')