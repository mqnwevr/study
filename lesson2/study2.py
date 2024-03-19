

# ---------------------------------------------
soovite = input('Kas te soovite remondi teha? ')
if soovite == 'jah':
    sein1 = int(input('esimene seine pikkus: '))
    sein2 = int(input('teine seine pikkus: '))
    print(sein1 * sein2 * 12, '$')
else:
    print('net tak net')

# ------------------------------------------------------------
name1 = input('Sinu nimi? ')
name2 = input('Jah sinu nimi?? ')
print(name1, 'ja', name2, 'on pinginaabrid tana!')
