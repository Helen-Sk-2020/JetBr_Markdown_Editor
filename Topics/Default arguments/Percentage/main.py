def get_percentage(number, round_digits=None):
    percentage = round(number * 100, round_digits)
    return f'{percentage}%'
