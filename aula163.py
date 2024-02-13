'''
video aula 276
datetime.timedelta e dateutil.relativetimedelta (calculando datas)
Docs:
https://dateutil.readthedocs.io/en/stable/relativedelta.html
https://docs.python.org/3/library/datetime.html#timedelta-objects
pip install python-dateutil types-python-dateutil
'''
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
delta = data_fim - data_inicio
adiciona_dez_dias = timedelta(days=10)
delta_relativo = relativedelta(data_fim, data_inicio)
print('-----')
print(data_fim > data_inicio)
print(data_fim < data_inicio)
print(data_fim == data_inicio)
print('-----')
print(delta)
print(delta.days, delta.seconds, delta.microseconds)  # segundos ref. a data
print(delta.total_seconds())
print('------')
print(data_fim + adiciona_dez_dias)
print(data_fim + relativedelta(seconds=60, minutes=10))
print('------')
print(delta_relativo)
print(delta_relativo.days, delta_relativo.years)
print('------')
