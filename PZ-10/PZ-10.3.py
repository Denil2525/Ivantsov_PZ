#В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
#мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
#3. в каких магазинах можно приобрести сахар.
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
