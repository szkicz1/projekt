from random import randint, choice

print('A - hejter węgier (koszmarny poziom trudności. Węgierski patriotyzm = 0 dostępny tylko podstawowy atak)')
print('B - (trudny poziom trudności. Węgierski patriotyzm = 25 nie zwiększa sie wraz z poziomem postaci)')
print('C - neutralny co do węgier (średni poziom trudności. Węgierski patriotyzm = 50 zwiększa sie wraz z poziomem postaci)')
print('D - entuzjasta węgier(łatwy poziom trudności. Węgierski patriotyzm = 100 zwiększa sie wraz z poziomem postaci)')

#------------------------------------------------------------
klasa_postaci = input ('wybierz klasę postaci:')
if klasa_postaci == ('A'):
    węgierska_esencja = 0
elif klasa_postaci == ('B'):
    węgierska_esencja = 25
elif klasa_postaci == ('C'):
    węgierska_esencja = 50
elif klasa_postaci == ('D'):
    węgierska_esencja = 100
elif klasa_postaci == ('E'):
    węgierska_esencja = 200
else:
    print('tak bez postaci chcesz grać chamie i prostaku proszę bardzo')
    life = 50
    węgierska_esencja = 0
life = 100
esencja = 0

#------------------------------------------------------------
name = input('Podaj imie twojej postaci (polecam imie MARIAN CZOPSON oraz nawet bardziej polecam imiona Kalejdoskop i celina.w.podróży):')
if name == ('MARIAN CZOPSON'):
    life += 10
elif name == ('Kalejdoskop'):
    life += 20
elif name == ('celina.w.podróży'):
    life += 20



#------------------------------------------------------------
def uderzenie_w_dupe():
    return randint(3, 10)


def strzał_z_liścia():
    global węgierska_esencja
    if węgierska_esencja < 10:
        print("-"*40)
        print("Nie masz węgierskiego patriotyzmu!")
        return 0
    węgierska_esencja -= 10
    return randint(9, 14)



def cimcirimcim():
    global węgierska_esencja
    if węgierska_esencja < 10:
        print("-"*40)
        print("Nie masz węgierskiego patriotyzmu!")
        return 0
    węgierska_esencja -= 10
    return randint(13, 20)

def odpoczynek():
    global węgierska_esencja
    if węgierska_esencja > 97:
        print("-"*40)
        print("masz wystarczająco węgierskiego patriotyzmu!")
        return 0
    węgierska_esencja += 3


def super_ultra_mega_hiper_diper_atak():
    global esencja
    if esencja < 5:
        print("-"*40)
        print("Nie masz esencji z przeciwników!")
        return 0
    esencja -= 5
    return randint(125, 150)

def w_prawo():
    return 1
def w_lewo():
    return 2
def prosto():
    return 3

#------------------------------------------------------------
def wybierz_atak():
    print('1 - Wykonaj Normalny Atak (zadaje obrażenia)')
    print('2 - walnij z liścia dekla! (zadaje obrażenia)')
    print('3 - super ultra mega hiper diper atak (ultimate z 5 zabitych przeciwników)')
    print('4 - cimcirimcim! (leczy 10 życia kosztem 5 węgieskiego patriotyzmu)')
    print('5 - odpoczynek (przywraca 3 węgierskiego patriotyzmu lecz tracisz kolejke)')
    jajo = input().upper()
    if jajo == '1':
        return uderzenie_w_dupe()
    elif jajo == '2':
        return strzał_z_liścia()
    elif jajo == '3':
        return super_ultra_mega_hiper_diper_atak()
    elif jajo == '4':
        return cimcirimcim
    elif jajo == '5':
        return odpoczynek
    else:
        print("Nie wybrano ataku")
        return 0
    
#--------------------------------------------------------------
def wybierz_drogę():
    print('jesteś w pustym pomieszczeniu')
    print('w którą strone idziesz?')
    print('D/d - w prawo')
    print('A/a - w lewo')
    print('W/w - do przodu')
    jajo = input().upper()
    if jajo == 'D':
        return randint(1, 3)
    elif jajo == 'A':
        return randint(4, 6)
    elif jajo == 'W':
        return randint(7, 9)
    else:
        print("Nie wybrano drogi")
        return 0
    


#------------------------------------------------------------
def random_oponent():
    opponents = [
        ["opętany człowiek", 15, 3,],
        ["opętany krasnoludek", 10, 3,]
    ]
    return choice(opponents)

def random_oponent2():
    opponents = [
        ["opętany wampir", 25, 5,],
        ["opętany elf", 18, 4,]
    ]
    return choice(opponents)

def random_oponent3():
    opponents = [
        ["opętany czarnoksiężnik", 35, 8,],
        ["opętany mag", 20, 5,]
    ]
    return choice(opponents)
#------------------------------------------------------------
def boss():
    booss = [
        ["Duch", 250, 14,]
    ]
    return choice(booss)
#--------------------------------------------------------------

print('-'*200)
print('Trafiłes do lochów w celu zbadania dziwnych dzwięków i znikania stworzeń i ludzi.')
print('musisz to zbadać')
szala = 0
zbroja = 0
if klasa_postaci != 'A' or 'B' or 'C' or 'D' or 'E':
    max_live = 50
else:
    max_live = 100
while life > 0 and szala < 16:
    print('-'*200)
    droga = wybierz_drogę()
    liczba_zabitych_przeciwników = 0
    tiririri = 0
    

    while droga == 1 and tiririri < 1 and szala < 15:
        opponent = random_oponent()
        print('-'*200)


        while opponent[1] > 0 and liczba_zabitych_przeciwników < 1:
            print(f"{name} walczy teraz z {opponent[0]}")
            print(f"Przeciwnik ma {opponent[1]} HP i zadaje Ci {opponent[2]} obrażeń")
       
            life -= opponent[2]
            if life <= 0:
                print('PRZEGRAŁEŚ!!!')
                break


            print(f"Masz {life} HP i {węgierska_esencja} węgierskiego patriotyzmu")
            atak = wybierz_atak()
            if atak == cimcirimcim:
                if klasa_postaci != 'A' or 'B' or 'C' or 'D' or 'E':
                    if life > 40:
                        print('masz za dużo życia')
                    else:
                        life += 10
                else:
                    if zbroja == 0:
                        if life > 90:
                            print('masz za dużo życia')

                        else:
                            life += 10
                    elif zbroja == 1:
                        if life > 120:
                            print('masz za dużo życia')
                        else:
                            life += 10
                    elif zbroja == 2:
                        if life > 150:
                            print('masz za dużo życia')
                        else:
                            life += 10
                    elif zbroja == 3:
                        if life > 180:
                            print('masz za dużo życia')
                        else:
                            life += 10
                    elif zbroja == 4:
                        if life > 210:
                            print('masz za dużo życia')
                        else:
                            life += 10
                    elif zbroja == 5:
                        if life > 240:
                            print('masz za dużo życia')
                        else:
                            life += 10
                    elif zbroja == 6:
                        if life > 270:
                            print('masz za dużo życia')
                        else:
                            life += 10
                    elif zbroja == 7:
                        if life > 300:
                            print('masz za dużo życia')
                        else:
                            life += 10
                    elif zbroja == 8:
                        if life > 330:
                            print('masz za dużo życia')
                        else:
                            life += 10
                    elif zbroja == 9:
                        if life > 360:
                            print('masz za dużo życia')
                        else:
                            life += 10

                
            elif atak == odpoczynek:
                if klasa_postaci == 'A':
                    print ('ta umiejętność nie jest dostępna dla twojej klasy postaci')    
                elif klasa_postaci == 'B':
                    if węgierska_esencja > 20:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                elif klasa_postaci == 'C':
                    if węgierska_esencja > 45:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                elif klasa_postaci == 'D':
                    if węgierska_esencja > 95:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                elif klasa_postaci == 'E':
                    if węgierska_esencja > 195:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                else:
                    print('ta umiejętność nie jest dostępna dla twojej klasy postaci')
            else:
                opponent[1] -= atak
                print(f"Zadałeś {atak} obrażeń")


        if opponent[1] <= 0:
            print('Zabiłeś przeciwnika!!!')
            liczba_zabitych_przeciwników += 1
        liczba_zabitych_przeciwników -= 1
        esencja += 1
        szala += 1
        tiririri += 1
    
    while droga == 2 and tiririri < 1 and szala < 15:
        print('-'*200)
        print('trafiasz do pustego pomieszczenia')
        szala += 1
        tiririri += 1

    while droga == 3 and tiririri < 1 and szala < 15:
        print('-'*200)
        print('trafiłes do pustego pomieszczenia')
        szala += 1       
        tiririri += 1

#-----------------------------------------------------------------------------------------------------

    while droga == 4 and tiririri < 1 and szala < 15:
        opponent = random_oponent2()
        print('-'*200)


        while opponent[1] > 0 and liczba_zabitych_przeciwników < 1:
            print(f"{name} walczy teraz z {opponent[0]}")
            print(f"Przeciwnik ma {opponent[1]} HP i zadaje Ci {opponent[2]} obrażeń")
       
            life -= opponent[2]
            if life <= 0:
                print('PRZEGRAŁEŚ!!!')
                break


            print(f"Masz {life} HP i {węgierska_esencja} węgierskiego patriotyzmu")
            atak = wybierz_atak()
            if atak == cimcirimcim:
                if klasa_postaci != 'A' or 'B' or 'C' or 'D' or 'E':
                    if life > 40:
                        print('masz za dużo życia')    
                    else:
                        life += 10
                else:
                    if life > 90:
                        print('masz za dużo życia')
                    else:
                        life += 10
                
            elif atak == odpoczynek:
                if klasa_postaci == 'A':
                    print ('ta umiejętność nie jest dostępna dla twojej klasy postaci')    
                elif klasa_postaci == 'B':
                    if węgierska_esencja > 20:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                elif klasa_postaci == 'C':
                    if węgierska_esencja > 45:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                elif klasa_postaci == 'D':
                    if węgierska_esencja > 95:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                elif klasa_postaci == 'E':
                    if węgierska_esencja > 195:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                else:
                    print('ta umiejętność nie jest dostępna dla twojej klasy postaci')
            else:
                opponent[1] -= atak
                print(f"Zadałeś {atak} obrażeń")


        if opponent[1] <= 0:
            print('Zabiłeś przeciwnika!!!')
            liczba_zabitych_przeciwników += 1
        liczba_zabitych_przeciwników -= 1
        esencja += 1
        szala += 1
        tiririri += 1
    
    while droga == 5 and tiririri < 1 and szala < 15:
        print('-'*200)
        print('trafiasz do pustego pomieszczenia')
        szala += 1      
        tiririri += 1
    
    while droga == 6 and tiririri < 1 and szala < 15:
        print('-'*200)
        print('znalazłeś potkę do leczenia (przywraca 50 życia nawet gdy nie pozwala na to jego limit)')
        if klasa_postaci == 'A' or 'B' or 'C' or 'D' or 'E':
            life +=50
            print(f'zycie zwrosło o 50 teraz wynosi {life}')                   
        else:
            print('nie możesz używać przedmiotów z racji braku klasy postaci')
            
        szala += 1       
        tiririri += 1

#----------------------------------------------------------------------------------------------

    while droga == 7 and tiririri < 1 and szala < 15:
        opponent = random_oponent3()
        print('-'*200)


        while opponent[1] > 0 and liczba_zabitych_przeciwników < 1:
            print(f"{name} walczy teraz z {opponent[0]}")
            print(f"Przeciwnik ma {opponent[1]} HP i zadaje Ci {opponent[2]} obrażeń")
       
            life -= opponent[2]
            if life <= 0:
                print('PRZEGRAŁEŚ!!!')
                break


            print(f"Masz {life} HP i {węgierska_esencja} węgierskiego patriotyzmu")
            atak = wybierz_atak()
            if atak == cimcirimcim:
                if klasa_postaci != 'A' or 'B' or 'C' or 'D' or 'E':
                    if life > 40:
                        print('masz za dużo życia')    
                    else:
                        life += 10
                else:
                    if life > 90:
                        print('masz za dużo życia')
                    else:
                        life += 10
                
            elif atak == odpoczynek:
                if klasa_postaci == 'A':
                    print ('ta umiejętność nie jest dostępna dla twojej klasy postaci')    
                elif klasa_postaci == 'B':
                    if węgierska_esencja > 20:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                elif klasa_postaci == 'C':
                    if węgierska_esencja > 45:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                elif klasa_postaci == 'D':
                    if węgierska_esencja > 95:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                elif klasa_postaci == 'E':
                    if węgierska_esencja > 195:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                else:
                    print('ta umiejętność nie jest dostępna dla twojej klasy postaci')
            else:
                opponent[1] -= atak
                print(f"Zadałeś {atak} obrażeń")


        if opponent[1] <= 0:
            print('Zabiłeś przeciwnika!!!')
            liczba_zabitych_przeciwników += 1
        liczba_zabitych_przeciwników -= 1
        esencja += 1
        szala += 1
        tiririri += 1

    while droga == 8 and tiririri < 1 and szala < 15:
        print('-'*200)
        print('trafiasz do pustego pomieszczenia')
        szala += 1      
        tiririri += 1

    while droga == 9 and tiririri < 1 and szala < 15:
        print('-'*200)
        if klasa_postaci == 'A' or 'B' or 'C' or 'D' or 'E':
            max_live += 30
            print(f'znalazłeś zbroje + 30 do maksymalnego życia maksymalne życie to teraz {max_live}')
        else:
            print('nie możesz używać przedmiotów ze względu na brak klasy postaci')
        zbroja += 1
        szala += 1      
        tiririri += 1
    while szala == 15:
        duch = boss()
        print('-'*200)
        print('trafiłeś na boosa okazał się on potężnym duchem który stał za opętaniami wcześniejszych przeciwników.')
        print('to właśnie jego pokonanie jest twoim celem')
        while duch[1] > 0 and liczba_zabitych_przeciwników < 1:
            print(f"{name} walczy teraz z {duch[0]}")
            print(f"Przeciwnik ma {duch[1]} HP i zadaje Ci {duch[2]} obrażeń")
       
            life -= duch[2]
            if life <= 0:
                print('PRZEGRAŁEŚ!!!')
                break


            print(f"Masz {life} HP i {węgierska_esencja} węgierskiego patriotyzmu")
            atak = wybierz_atak()
            if atak == cimcirimcim:
                if klasa_postaci != 'A' or 'B' or 'C' or 'D' or 'E':
                    if life > 40:
                        print('masz za dużo życia')    
                    else:
                        life += 10
                else:
                    if life > 90:
                        print('masz za dużo życia')
                    else:
                        life += 10
                
            elif atak == odpoczynek:
                if klasa_postaci == 'A':
                    print ('ta umiejętność nie jest dostępna dla twojej klasy postaci')    
                elif klasa_postaci == 'B':
                    if węgierska_esencja > 20:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                elif klasa_postaci == 'C':
                    if węgierska_esencja > 45:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                elif klasa_postaci == 'D':
                    if węgierska_esencja > 95:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                elif klasa_postaci == 'E':
                    if węgierska_esencja > 195:
                        print('masz za dużo węgierskiego patriotyzmu')
                    else:
                        węgierska_esencja += 5
                else:
                    print('ta umiejętność nie jest dostępna dla twojej klasy postaci')
            else:
                duch[1] -= atak
                print(f"Zadałeś {atak} obrażeń")


        if duch[1] <= 0:
            print('Zabiłeś bossa!!!')
            liczba_zabitych_przeciwników += 1
        liczba_zabitych_przeciwników -= 1
        esencja += 1
        szala += 1
        tiririri += 1
while szala == 16 and life > 0:
    print('gratulacje przeszedłeś gre po zabiciu ducha wyszedłeś z lochów i otrzymałeś')
    print('zapłate za wykonane zadanie po czym ruszyłeś w swoją stronę')
    break    
