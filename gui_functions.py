import tkinter as tk


def validate_length(current_text, max_length):
    return len(current_text) <= int(max_length)

def validate_alphabetic(current_letter):
    return current_letter.isalpha()


## Function not working properly, reason unkown.
def check_scrollbar_visibility(text_widget, scrollbar, bar_column, bar_row, interval=100):
    text_widget.update_idletasks()

    info = text_widget.dlineinfo("1.0")

    if info:
        if scrollbar.winfo_ismapped():
            scrollbar.grid_remove()
    else:
        if not scrollbar.winfo_ismapped():
            scrollbar.grid(column=bar_column, row=bar_row, sticky=tk.W)

    text_widget.after(interval, check_scrollbar_visibility, text_widget, scrollbar, bar_column, bar_row, interval)