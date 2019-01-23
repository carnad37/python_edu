today="20010331Rainy"
year=today[:4]
month=today[4:6]
days=today[6:8]
weather=today[8:]
print('Year:',year,'\nMonth:',month,'\nDays:',days,'\nWeather:',weather)
print('%s년'%year+'\n%s월'%month+'\n%s일'%days+'\n%s'%weather)