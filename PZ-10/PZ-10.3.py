magnit = ['milk','salt','sugar']
pyatorochka = ['meat','milk','cheese']
perekrestok = ['milk','curd','cheese','sugar']
result = []
if magnit.count('sugar') > 0:
    result.append('magnit')
if pyatorochka.count('sugar') > 0:
    result.append('pyatorochka')
if perekrestok.count('sugar') > 0:
    result.append('perekrestok')
result = str(result)
result = result.replace('[','')
result = result.replace(']','')
print(result)