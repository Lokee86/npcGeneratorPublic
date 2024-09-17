import tkinter as tk


def validate_length(current_text, max_length):
    return len(current_text) <= int(max_length)

def validate_alphabetic(current_letter):
    return current_letter.isalpha()


## Function not working properly, reason unkown.
def check_scrollbar_visibility(text_widget, scrollbar, bar_column, bar_row, interval=100):
    text_widget.update_idletasks()
    
    # Calculate the content height of the Text widget
    text_widget_height = text_widget.winfo_height()
    content_height = text_widget.dlineinfo(tk.END)[1] if text_widget.dlineinfo(tk.END) else 0

    if content_height > text_widget_height:
        if not scrollbar.winfo_ismapped():
            scrollbar.grid(column=bar_column, row=bar_row, sticky=tk.W)
    else:
        if scrollbar.winfo_ismapped():
            scrollbar.grid_remove()

    text_widget.after(interval, check_scrollbar_visibility, text_widget, scrollbar, bar_column, bar_row, interval)