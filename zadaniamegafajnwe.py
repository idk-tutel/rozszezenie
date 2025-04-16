def zad1(listaaaaaa=[1, 2, 3, 4, 5, 6, 7, 8, 9, 34, 56, 5, 256, 346, 457, 2345, 47, 4326, 679, 235, 88]):
    w=listaaaaaa[0]
    for i in listaaaaaa:
        if i > w:
            w=i
    print(w)
zad1()
def zad2(listaaaaa=[1, 34, 1, 367, 1, 467, 2, 1, 546, 1, 345, 367, 1], element=1):
    w=0
    for i in listaaaaa:
        if i == element:
            w+=1
    print(w)
zad2()
def zad3(listaaaa=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(listaaaa[::-1])
zad3()
def zad4(stringinging="0aaaaagafga()(())()dsgf"):
    w=0
    for i in stringinging:
        if i == "(":
            w+=1
        if i == ")":
            w-=1
        if w<0:
            break
    if w != 0:
        print("zle")
    else:
        print("jest git")
zad4()
class zad5():
    def __init__(self, value):
        self.value = value
        self.next = None
    def add(self, newvalue):
        if self.next == None:
            self.next = zad5(newvalue)
        else:
            self.next.add(newvalue)
    def take(self):
        pass
