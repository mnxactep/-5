def шифрование(текст, шаг):
    зашифрованный_текст = ""
    
    for символ in текст:
        if символ.isalpha():
            if символ.isupper():
                код_символа = ord(символ) - ord('А')
                зашифрованный_код = (код_символа + шаг) % 33
                зашифрованный_символ = chr(зашифрованный_код + ord('А'))
                зашифрованный_текст += зашифрованный_символ
            else:
                код_символа = ord(символ) - ord('а')
                зашифрованный_код = (код_символа + шаг) % 33
                зашифрованный_символ = chr(зашифрованный_код + ord('а'))
                зашифрованный_текст += зашифрованный_символ
        else:
            зашифрованный_текст += символ

    return зашифрованный_текст

def расшифровка(зашифрованный_текст, шаг):
    текст = ""

    for символ in зашифрованный_текст:
        if символ.isalpha():
            if символ.isupper():
                код_символа = ord(символ) - ord('А')
                расшифрованный_код = (код_символа - шаг) % 33
                расшифрованный_символ = chr(расшифрованный_код + ord('А'))
                текст += расшифрованный_символ
            else:
                код_символа = ord(символ) - ord('а')
                расшифрованный_код = (код_символа - шаг) % 33
                расшифрованный_символ = chr(расшифрованный_код + ord('а'))
                текст += расшифрованный_символ
        else:
            текст += символ

    return текст

def main():
    текст = input("Введите текст: ")
    шаг = int(input("Введите шаг сдвига: "))

    зашифрованный_текст = шифрование(текст, шаг)
    print("Зашифрованный текст:", зашифрованный_текст)

    расшифрованный_текст = расшифровка(зашифрованный_текст, шаг)
    print("Расшифрованный текст:", расшифрованный_текст)

if __name__ == "__main__":
    main()
