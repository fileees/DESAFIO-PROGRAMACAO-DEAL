text = input("Insira a palavra => ").upper()
reverse = ""
i = len(text) - 1

while i >= 0:
    reverse += text[i]
    i -= 1

if reverse == text:
    print(f'{text} É UM PALÍNDROMO!')
else:
    print(f'{text} NÃO É UM PALÍNDROMO')
