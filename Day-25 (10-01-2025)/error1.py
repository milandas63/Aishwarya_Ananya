class MainError(Exception):
    def __init__(self):
        print("This is an error")


class HomeWorkError(Exception):
    def __init(self):
        print("Your home work is not done")


string = "Trident Academy"
name = "Ananya"
diction = {"party":"BJB","name":"Narendra Modi","age":69,"school":"Harrow"}
try:
    if name=="Ananya":
        raise HomeWorkError()
    print(100/2)
    print(string[5])
    print(diction["school"])
    print("There is no error")
except MainError:
    print("Main error")
except HomeWorkError:
    print("Please do your homework")
except ZeroDivisionError:
    print("Zero denominator not allowed")
except ArithmeticError:
    print("Arithmetic error")
except IndexError:
    print("Index error")
except KeyError:
    print("Key error")
else:
    print("Nil error")
finally:
    print("Must be executed")

