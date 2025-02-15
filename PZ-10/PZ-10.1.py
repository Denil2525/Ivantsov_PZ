magnit = {'milk','salt','sugar'}
pyatorochka = {'meat','milk','cheese'}
perekrestok = {'milk','curd','cheese','sugar'}
result = magnit | pyatorochka | perekrestok
result = str(result)
result = result.replace('{','')
result = result.replace('}','')
print(result)