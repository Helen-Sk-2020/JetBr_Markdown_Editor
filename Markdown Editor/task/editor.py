# print("""# John Lennon
# or ***John Winston Ono Lennon*** was one of *The Beatles*.
# Here are the songs he wrote I like the most:
# * Imagine
# * Norwegian Wood
# * Come Together
# * In My Life
# * ~~Hey Jude~~ (that was *McCartney*)""")


def help_editor():
    
    formatters = ['!help', '!done']
    available_formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'ordered-list', 'unordered-list']
    special_commands = ['!help', '!done']
    markdown_text = []
    
    while True:
        user_input = input('- Choose a formatter: ')
        
        if user_input in formatters:
            if user_input == '!help':
                print(f"Available formatters: {' '.join(available_formatters)}"
                      f"\nSpecial commands: {' '.join(special_commands)}")
            else:
                save_results(markdown_text)
                break
                
        elif user_input in available_formatters:
            if user_input == 'plain':
                plain(markdown_text)
            elif user_input == 'bold':
                bold(markdown_text)
            elif user_input == 'italic':
                italic(markdown_text)
            elif user_input == 'header':
                header(markdown_text)
            elif user_input == 'link':
                link(markdown_text)
            elif user_input == 'inline-code':
                inline_code(markdown_text)
            elif user_input == 'new-line':
                new_line(markdown_text)
            elif user_input == 'ordered-list' or user_input == 'unordered-list':
                lists(markdown_text, user_input)
            print(''.join(markdown_text))
            
        else:
            print('Unknown formatting type or command')
            
 
def plain(whole_text):
    text = input('Text:')
    whole_text.append(text)
    return whole_text


def bold(whole_text):
    text = input('Text:')
    whole_text.append(f"**{text}**")
    return whole_text


def italic(whole_text):
    text = input('Text:')
    whole_text.append(f"*{text}*")
    return whole_text


def header(whole_text):
    while True:
        try:
            level = int(input('Level:'))
            if level in range(1, 7):
                text = input('Text:')
                whole_text.append(f"{level * '#'} {text}\n")
                return whole_text
                break
            else:
                raise ValueError
        except ValueError:
            print("The level should be within the range of 1 to 6")
        
    
def link(whole_text):
    label = input("Label:")
    url = input("URL:")
    whole_text.append(f"[{label}]({url})")
    return whole_text


def inline_code(whole_text):
    text = input('Text:')
    whole_text.append(f"`{text}`")
    return whole_text


def new_line(whole_text):
    whole_text.append(f"\n")
    return whole_text


def lists(whole_text, list_type):
    while True:
        try:
            rows = int(input("Number of rows:"))
            if rows > 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("The number of rows should be greater than zero")
            
    for x in range(1, rows + 1):
        row = input(f"Row #{x}:")
        whole_text.append(f"{x if list_type == 'ordered-list' else '*'}"
                          f"{'.' if list_type == 'ordered-list' else ''} "
                          f"{row}\n")


def save_results(text):
    file = open('output.md', 'w', encoding='utf-8')
    file.writelines(text)
    file.close()


help_editor()
