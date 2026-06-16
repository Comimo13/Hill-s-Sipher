from Database import Latin_Script
from Database import Cyrillic_Script
from Database import Japanese_Scripts
from Database import Spanish_Script
from Database import Korean_Hangul
from Database import Bengali_Script
from Database import Devanagari_Script
from Database import Hebrew_Script
from Database import Greek_Script
from Database import Arabic_Script
from Database import German_Script

def choose_language():
    mapping = {
        'Latin': Latin_Script,
        'Cyrillic': Cyrillic_Script,
        'Japanese': Japanese_Scripts,
        'Spanish': Spanish_Script,
        'Korean': Korean_Hangul,
        'Bengali': Bengali_Script,
        'Devanagari': Devanagari_Script,
        'Hebrew': Hebrew_Script,
        'Greek': Greek_Script,
        'Arabic': Arabic_Script,
        'German': German_Script
    }
    for num, lang in enumerate(mapping):
        num += 1
        print(num, '.', lang)

    language_input = input('Enter language(not index): ')
    language = mapping[language_input]
    return language