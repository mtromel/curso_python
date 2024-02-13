'''
video aula 279
Usando calendar para calendários e datas
httsp://docs.python.org/3/library/calendar.html
calendar é usado para coisas genéricas de calendários e datas
Com calendar, você pode saber coisas como:
- Qual o último dia do mês (ex.: monthrange)
- Qual o nome e número do dia de determinada data (ex.: weekday)
- Criar um calendário em si (ex.: monthcalendar)
- Trabalhar com coisas específicas de calendários (ex.: calendar, month)
Por padrão dia da semana começa em 0 até 6
0 = segunda-feira | 6 = domingo
'''
import calendar


# print(calendar.calendar(2022))
print(calendar.month(2022, 12))
print(calendar.monthrange(2022, 12))
# retorna o dia da semana do primeiro dia e o ultimo dia do mês.
print(list(enumerate(calendar.day_name)))

numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022, 12)
print(f'{calendar.day_name[numero_primeiro_dia]} -- 1,'
      f' {calendar.day_name[calendar.weekday(2022, 12, ultimo_dia)]}, '
      f'{ultimo_dia}')

print(calendar.monthcalendar(2022, 12))
# mostra as semanas do mês. Os valores 0 que mostra é porque aquele dia da
# semana não pertence ao mês solicitado.

for week in calendar.monthcalendar(2022, 12):
    print(list(enumerate(week)))

for week in calendar.monthcalendar(2022, 12):
    for day in week:
        if day == 0:
            continue
        print(day)
