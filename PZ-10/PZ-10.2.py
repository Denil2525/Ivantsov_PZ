magnit = ['milk','salt','sugar']
pyatorochka = ['meat','milk','cheese']
perekrestok = ['milk','curd','cheese','sugar']
result = []
if magnit.count('milk') > 0:
    if magnit.count('cheese') > 0:
        result.append('magnit')
if pyatorochka.count('milk') > 0:
    if pyatorochka.count('cheese') > 0:
        result.append('pyatorochka')
if perekrestok.count('milk') > 0:
    if perekrestok.count('cheese') > 0:
        result.append('perekrestok')
result = str(result)
result = result.replace('[','')
result = result.replace(']','')
print(result)