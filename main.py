import keyboard
import transliteration
from trial import ListLabelApp

app=ListLabelApp()

def update_items_from_external(items):
    new_items = items
    app.update_items_external(new_items)

def print_typed_words():
    current_word = ""
    strset='abcdefghijklmnopqrstuvwxyz'
    ll=None
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name in strset:
                current_word += event.name
            elif event.name == 'backspace':
                current_word = current_word[:-1]
                
            elif event.name == 'enter':
                keyboard.write('\n')
                current_word =""
            elif event.name == 'space':
                keyboard.write(ll[0]+" ")
                current_word=""
            else:
                # Handle other special characters as neededकैसे 
                pass
        if current_word=="":
            continue
        ll=transliteration.getSuggestions(current_word)
        update_items_from_external(ll)
        print(ll)

if __name__ == "__main__":
    print_typed_words()
