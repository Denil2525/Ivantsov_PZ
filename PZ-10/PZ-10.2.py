#В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
#мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
#2. в каких магазинах можно приобрести одновременно молоко и сыр.
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
