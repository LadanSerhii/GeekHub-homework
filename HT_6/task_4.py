# Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді коду Морзе та виводить декодоване значення
# (латинськими літерами).
#    Особливості:
#     - використовуються лише крапки, тире і пробіли (.- )
#     - один пробіл означає нову літеру
#     - три пробіли означають нове слово
#     - результат може бути case-insensitive (на ваш розсуд - великими чи маленькими літерами).
#     - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки тощо використовуватися не будуть.
#     Лише латинські літери.
#     - додайте можливість декодування сервісного сигналу SOS (...---...)
#     Приклад:
#     --. . . -.- .... ..-- -...   .. ...   .... . .-. .
#     результат: GEEKHUB IS HERE


morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', ',': '--..', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.',
    ')': '-.--.-', 'SOS': '...---...'
    }


def sym_decode(sym):
    for key, value in morse_dict.items():
        if value == sym:
            return key


def word_decode(word):
    char_list = word.split()
    dec_word = ''
    for char in char_list:
         if sym_decode(char):
            dec_word += sym_decode(char)
         else:
            #do not change the icoming data = probably good practice to replace the uncoded symbol with '*'
            dec_word += '*'
    return dec_word


def morse_code(base_str):
    words = base_str.split('   ')
    dec_str = ''
    for element in words:
        if words.index(element) != len(words) - 1:
            dec_str += word_decode(element) + ' '
        else:
            dec_str += word_decode(element)
    return dec_str


print(morse_code("...---...   --. . . -.- .... ..-- -...   .. ...   .... . .-. ."))


