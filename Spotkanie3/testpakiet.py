#import pakiet.modul1
#from pakiet.modul1 import foo
#from pakiet.modul1 import *
from pakiet import modul1

def foo():
    print("inne foo")

#print(pakiet.modul1.foo())
print(foo())
print(modul1.foo())