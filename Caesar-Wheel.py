alph = 'UBbAdCcDeE fFgGhHiIkJjK?lLmMNnoOpPqrQRsStWuavVwTxZyYzX,.:;\!/[]{}!#@$%^(&*)-_=+`~)                               '
                                             #alph - da sondaki boshluqlar error almayaq deyedir.
def enc(alph, text, key, encrypted):
    print('Shifrelenir...')
    for x in text:
        if x in alph:
            old_ind = alph.index(x)
            new_ind = old_ind + key
            if new_ind >= len(alph):
                new_ind = new_ind % len(alph) 
            y = alph[new_ind]
            encrypted += y
        else:
            encrypted += x
    if len (encrypted) > 0:
        print('Shifrelenmish metn:', encrypted)

def dec(alph, text, key, decrypted):
    print('Shifre chozulur...')
    for x in text:
        if x in alph:
            old_ind = alph.index(x)
            if key > len(alph):
                key = key % len(alph)
            new_ind = old_ind - key
            y = alph[new_ind]
            decrypted += y
        else:
            decrypted += x
    print('Shifre chozuldu:', decrypted)

while True:
    print("""
    *********************************************
    [1] - Shifrele (Encrypt)
    [2] - Shifreni choz (Decrypt)
    [3] - Chixish
    *********************************************
    """)

    f = input('Sech(1/2/3): ')

    if f == '1':
        text = input('Shifrelenecek metn: ')
        try:
            key = int(input('Shifreleme acharini girin(Shifreni achmaq uchun lazim olacaq): '))
        except ValueError:
            print('Eded girin!')
            continue
        encrypted = ''
        enc(alph, text, key, encrypted)
    elif f == '2':
        text = input('Shifresi achilacaq metn: ')
        try:
            key = int(input('Shifreleme acharini girin(Yazinin shifrelendiyi achar): '))
        except ValueError:
            print('Eded girin!')
            continue
        decrypted = ''
        dec(alph, text, key, decrypted)
    elif f == '3':
        quit()
    else:
        print('Duzgun sechim edin!')
        continue