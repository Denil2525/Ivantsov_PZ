weather = {}
inf = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'
inf = inf.split()
weather['Погода за'] = inf[0]
weather['Январь'] = inf[1]
weather['Февраль'] = inf[2]
weather['Март'] = inf[3]
weather['Апрель'] = inf[4]
weather['Май'] = inf[5]
weather['Июнь'] = inf[6]
weather['Июль'] = inf[7]
weather['Август'] = inf[8]
weather['Сентябрь'] = inf[9]
weather['Октябрь'] = inf[10]
weather['Ноябрь'] = inf[11]
weather['Декабрь'] = inf[12]
print(weather)