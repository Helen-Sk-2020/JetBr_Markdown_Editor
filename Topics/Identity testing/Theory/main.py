# # print("""# John Lennon
# # or ***John Winston Ono Lennon*** was one of *The Beatles*.
# # Here are the songs he wrote I like the most:
# # * Imagine
# # * Norwegian Wood
# # * Come Together
# # * In My Life
# # * ~~Hey Jude~~ (that was *McCartney*)""")
#
#
# def help_editor():
#
#     formatters = ['!help', '!done']
#     available_formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line']
#     special_commands = ['!help', '!done']
#     markdown_text = []
#
#     while True:
#         user_input = input('- Choose a formatter: ')
#
#         if user_input in formatters:
#             if user_input == '!help':
#                 print(f"Available formatters: {' '.join(available_formatters)}"
#                       f"\nSpecial commands: {' '.join(special_commands)}")
#             else:
#                 break
#
#         elif user_input in available_formatters:
#             if user_input == 'plain':
#                 plain(markdown_text)
#             elif user_input == 'bold':
#                 bold(markdown_text)
#             elif user_input == 'italic':
#                 italic(markdown_text)
#             elif user_input == 'header':
#                 header(markdown_text)
#             elif user_input == 'link':
#                 link(markdown_text)
#             elif user_input == 'inline-code':
#                 inline_code(markdown_text)
#             elif user_input == 'new-line':
#                 new_line(markdown_text)
#             print(''.join(markdown_text))
#
#         else:
#             print('Unknown formatting type or command')
#
#
# def plain(whole_text):
#     text = input('Text:')
#     whole_text.append(text)
#     return whole_text
#
#
# def bold(whole_text):
#     text = input('Text:')
#     whole_text.append(f"**{text}**")
#     return whole_text
#
#
# def italic(whole_text):
#     text = input('Text:')
#     whole_text.append(f"*{text}*")
#     return whole_text
#
#
# def header(whole_text):
#     while True:
#         try:
#             level = int(input('Level:'))
#             if level in range(1, 7):
#                 text = input('Text:')
#                 whole_text.append(f"{level * '#'} {text}\n")
#                 return whole_text
#                 break
#             else:
#                 raise ValueError
#         except ValueError:
#             print("The level should be within the range of 1 to 6")
#
#
# def link(whole_text):
#     label = input("Label:")
#     url = input("URL:")
#     whole_text.append(f"[{label}]({url})")
#     return whole_text
#
#
# def inline_code(whole_text):
#     text = input('Text:')
#     whole_text.append(f"`{text}`")
#     return whole_text
#
#
# def new_line(whole_text):
#     whole_text.append(f"\n")
#     return whole_text
#
#
# help_editor()

class Editor:
    
    available_formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line']
    special_commands = ['!help', '!done']
    
    def __init__(self):
        self.markdown_text = []
        self.editor = ''
        
    def take_input(self):
        while True:
            formatter = input("Choose a formatter:")
            if formatter in Editor.special_commands:
                if formatter == '!help':
                    print(f"Available formatters: {' '.join(Editor.available_formatters)}"
                          f"\nSpecial commands: {' '.join(Editor.special_commands)}")
                else:
                    break
            elif formatter in Editor.available_formatters:
                if formatter == 'plain':
                    self.plain()
                elif formatter == 'bold':
                    self.bold()
                elif formatter == 'italic':
                    self.italic()
                elif formatter == 'header':
                    self.header()
                elif formatter == 'link':
                    self.link()
                elif formatter == 'inline-code':
                    self.inline_code()
                elif formatter == 'new-line':
                    self.new_line()
                print(''.join(self.markdown_text))
                
            else:
                print("Unknown formatting type or command")
 
    def plain(self):
        text = input('Text:')
        self.markdown_text.append(text)
        
    def bold(self):
        text = input('Text:')
        self.markdown_text.append(f"**{text}**")

    def italic(self):
        text = input('Text:')
        self.markdown_text.append(f"*{text}*")
        
    def header(self):
        while True:
            try:
                level = int(input('Level:'))
                if level in range(1, 7):
                    text = input('Text:')
                    self.markdown_text.append(f"{level * '#'} {text}\n")
                    break
                else:
                    raise ValueError
            except ValueError:
                print("The level should be within the range of 1 to 6")

    def link(self):
        label = input("Label:")
        url = input("URL:")
        self.markdown_text.append(f"[{label}]({url})")

    def inline_code(self):
        text = input('Text:')
        self.markdown_text.append(f"`{text}`")

    def new_line(self):
        self.markdown_text.append(f"\n")


def main():
    text = Editor()
    text.take_input()
    
if __name__ == "__main__":
    main()
    

