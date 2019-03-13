alph = 'UBbAdCcDeE fFgGhHiIkJjK?lLmMNnoOpPqrQRsStWuavVwTxZyYzX,.:;\!/[]{}!#@$%^(&*)-_=+`~)UBbUBbUBbUBbUBbUBbUBbUBbUBb'
                                             #alph - da sonda tekrarlanan UBb Index error almayaq deyedir.
def enc(alph, text, key, encrypted):
    print('Sifrelenir...')
    for x in text:
        if x in alph:
            old_ind = alph.index(x)
            new_ind = old_ind + key
            try:
                y = alph[new_ind]
            except IndexError:
                encrypted = ''
                print('Acar cox boyukdur! Daha kicik acar girin!')
                break
            encrypted += y
        else:
            encrypted += x
    if len (encrypted) > 0:
        print('Sifrelenmis metn:', encrypted)

def dec(alph, text, key, decrypted):
    print('Sifre chozulur...')
    for x in text:
        if x in alph:
            old_ind = alph.index(x)
            new_ind = old_ind - key
            y = alph[new_ind]
            decrypted += y
        else:
            decrypted += x
    print('Sifre chozuldu:', decrypted)

while True:
    print("""
    *********************************************
    [1] - Sifrele (Encrypt)
    [2] - Sifreni choz (Decrypt)
    *********************************************
    """)

    f = input('Sec(1/2): ')

    if f == '1':
        text = input('Sifrelenecek metni girin: ')
        key = int(input('Sifreleme acarini girin(Sifreni acmaq ucun lazim olacaq): '))
        encrypted = ''
        enc(alph, text, key, encrypted)
    elif f == '2':
        text = input('Sifresi acilacaq metn: ')
        key = int(input('Sifreleme acarini girin(Yazinin sifrelendiyi acar)'))
        decrypted = ''
        dec(alph, text, key, decrypted)
    else:
        print('Duzgun sechim edin!')
        continue
