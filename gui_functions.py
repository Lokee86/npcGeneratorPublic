

def validate_stat_length(current_text, max_length):
    return len(current_text) <= int(max_length)

def validate_alphabetic(current_letter):
    return current_letter.isalpha()
