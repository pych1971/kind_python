morze = {".-": "А", "-...": "Б", ".--": "В", "--.": "Г", "-..": "Д", ".": "Е", "...-": "Ж", "--..": "З", "..": "И",
         ".---": "Й", "-.-": "К", ".-..": "Л", "--": "М", "-.": "Н", "---": "О", ".--.": "П", ".-.": "Р", "...": "С",
         "-": "Т", "..-": "У", "..-.": "Ф", "....": "Х", "-.-.": "Ц", "---.": "Ч", "----": "Ш", "--.-": "Щ",
         ".--.-": "Ъ", "-.--": "Ы", "-..-": "Ь", "...-...": "Э", "..--": "Ю", ".-.-": "Я", "-...-": " "}

for i in input().split():
    print(morze.get(i).lower(), end='')