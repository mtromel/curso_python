a = 'A'
b = 'B'
c = 1.1

# string = 'a={} b={} c{:.2f }
# formato = string.format(a, b, c)

string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c) # quando precisar nomear um dos argumentos todos os argumentos que vem depois desse
                                                   # nomeado precisam ser nomeados também. Ex. se nomear apenas o 'c', 'a' e 'b' não
                                                   # precisam estar nomeados. Mas se nomear o 'a' todos depois dele precisa nomear.

print(formato)
