'''
video aula 274
Criando datas com módulo datetime
datetime(ano, mês, dia)
datetime(ano, mês, dia, horas, minutos, segundos)
datetime.now()
https://pt.wikipedia.org/wiki/Era_Unix
datetime.fromtimestamp(Unix Timestamp)
https://docs.python.org/3/library/datetime.html
Para timezones
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
instalando o pytz
pip install pytz types-pytz
'''
'''from datetime import datetime

data_str_data = '2022-04-20 07:49:23'
data_str_fmt = '%Y-%m-%d %H:%M:%S'

# data = datetime(2022, 4, 20, 7, 49, 23)
# a partir da hora é opcional informar. Se não informado assume 0
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)'''

# video aula 275
from datetime import datetime
from pytz import timezone

# data = datetime.now(timezone('Asia/Tokyo'))
data = datetime.now(timezone('America/Sao_Paulo'))
print(data.timestamp())
print(datetime.fromtimestamp(1706481099))
print('------')
print(data)
