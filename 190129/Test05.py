date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = {}
for i in range(0,len(date),1):
    close_table[date[i]] = close_price[i]

print(close_table)