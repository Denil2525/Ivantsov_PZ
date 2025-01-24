link = "C:/Projects/ValleyOS/Game.exe"
ammount = link.count('/')
link = link.split('/')
while ammount != 0:
    link.pop(0)
    ammount -= 1
link = str(link)
link = link.split('.')
link.pop(1)
link = str(link)
link = link.replace('[','')
link = link.replace(']','')
link = link.replace('"','')
link = link.replace("'",'')
print(link)