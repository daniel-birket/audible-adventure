from time import sleep
with open("fontSize.var", "w") as f:
    f.write("12")
slp=2
def load():
    global size
    file=open("./fontSize.var", "r") 
    size=int(file.read())
    file.close
def printdelay(s):
    sleep(slp)
    print(s)
    sleep (slp)
def savesettings():
    file=open("./fontSize.var", "w")
    newsize=input("Type in new font size.")
    file.write(newsize)
    printdelay("Saved!")
    file.close()

while True:
    load()
    printdelay(size)
    savesettings()
