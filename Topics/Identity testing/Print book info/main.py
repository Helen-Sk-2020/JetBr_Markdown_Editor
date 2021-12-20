def print_book_info(title, author=None, year=None):
    # print(f'"{title}" '
    #       f'{"was written" if author is not None or year is not None else ""} '
    #       f'{"by " if author is not None else ""}{author if author is not None else ""}'
    #       f'{"in " if year is not None else ""}{year if year is not None else ""}')
    text = [f'"{title}"']
    if author or year:
        text.append("was written")
    if author:
        text.append(f'by {author}')
    if year:
        text.append(f'in {year}')
    print(' '.join(text))
    pass

name = None
print(bool(name))
name = "ishfxn"
print(bool(name))

