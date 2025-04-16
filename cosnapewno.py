import main as yufv

yufv.pr()

class Person():
    def __init__(self, firs_tname, last_name) -> None:
        self.firs_tname = firs_tname
        self.last_name = last_name
    def hello(self):
        print("Helo")




class Teacher(Person):
    def __init__(self, firs_tname, last_name) -> None:
        super().__init__(firs_tname, last_name)
    def hello(self):
        print("WItaj")
    def __str__(self) -> str:
        return f'{self.firs_tname}, {self.last_name}'
        
