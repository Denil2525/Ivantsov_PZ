#В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
#мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
#1. полный список всех товаров.
magnit = {'milk','salt','sugar'}
pyatorochka = {'meat','milk','cheese'}
perekrestok = {'milk','curd','cheese','sugar'}
result = magnit | pyatorochka | perekrestok
result = str(result)
result = result.replace('{','')
result = result.replace('}','')
print(result)
