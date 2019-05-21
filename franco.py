from datetime import datetime, date, time, timedelta

ahora = datetime.now()
mas_90 = ahora + timedelta(minutes = 90)
cadena = mas_90.strftime()
print (mas_90)