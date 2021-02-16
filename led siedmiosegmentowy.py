print('Oto wyświetlacz led w twojej konsoli.\nPodaj liczbe a ja ją wyświetle')
jeden = '''
  #
  #
  #
'''
dwa = '''
###
  #
###
#
###
'''
trzy = '''
###
  #
###
  #
###
'''
cztery ='''
# #
# #
###
  #
  #
'''
piec ='''
###
#
###
  #
###
'''
szesc = '''
###
#
###
# #
###
'''
siedem ='''
###
  #
  #
  #
  #
'''
osiem = '''
###
# #
###
# #
###
'''
dziewiec ='''
###
# #
###
  #
###
'''
zero = '''
###
# #
# #
# #
###
'''
liczba = input ()

for i in liczba:
    if i == '0':
        print (zero)
    elif i == '1':
        print (jeden)
    elif i == '2':
        print (dwa)
    elif i == '3':
        print (trzy)
    elif i == '4':
        print (cztery)
    elif i == '5':
        print (piec)
    elif i == '6':
        print (szesc)
    elif i == '7':
        print (siedem)
    elif i == '8':
        print (osiem)
    elif i == '9':
        print (dziewiec)
