print('Tere! Olen sinu uus sober - Python!')
nimi = input('Mis sinu nimi on? ').capitalize()
print(nimi, ', oi kui ilus nimi!')
answer = input('Kas leian Sinu keha indeksi? 0-ei, 1-jah => ')
vastus = ''
if int(answer) == 1:
    try: 
        pikkus = int(input('Sinu pikkus on? '))
        mass = int(input('Sinu mass on? '))
        indeks = mass / (0.01 * pikkus)**2
        print(nimi + '! Sinu keha indeks on: ', "%.1f" % indeks)
        if indeks < 16:
            vastus = 'tervisele ohtlik alakaal.'
        elif indeks < 20:
            vastus = 'alakaal.'
        elif indeks < 26:
            vastus = 'normaalkaal.'
        elif indeks < 31:
            vastus = 'ulekaal.'
        elif indeks < 36:
            vastus = 'rasvumine.'
        elif indeks < 41:
            vastus = 'tugev rasvumine.'
        else:
            vastus = 'tervisele ohtlik rasvumine.'
        print('See on ', vastus)
    except:
        print('ValueError')
else:
    print('Kahju! See on vaga kasulik info!\n')

print('Kohtumiseni, ' + nimi + '! Igavesti Sinu, Python!')    