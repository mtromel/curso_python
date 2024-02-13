'''
video aula 280
locale para internacionalização
https://docs.python.org/3/library/locale.html
https://learn.microsoft.com/fr-fr/powershell/module/international
'''
import calendar
import locale


locale.setlocale(locale.LC_ALL, '')  # essa opção é melhor. Usa o padrão do SO.
# locale.setlocale(locale.LC_ALL, 'pt_BR')


print(calendar.calendar(2022))
print(locale.getlocale())
