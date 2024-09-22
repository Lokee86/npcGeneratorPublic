import tkinter as tk


def validate_length(current_text, max_length):
    return len(current_text) <= int(max_length)

def validate_alphabetic(current_letter):
    return current_letter.isalpha()

def update_variable_from_widget(string_var, event):
    content = event.widget.get("1.0", tk.END)
    string_var.set(content)

def update_widget_from_variable(string_var, widget, *args):
    widget.delete("1.0", tk.END)
    widget.insert("1.0", string_var.get())

def check_scrollbar_visibility(text_widget, scrollbar, widget_height, bar_column, bar_row, interval=100):
    content_height = int(float(text_widget.index(tk.END)))

    if content_height > (widget_height + 1):
        if not scrollbar.winfo_ismapped():
            scrollbar.grid(column=bar_column, row=bar_row, sticky=tk.W)
    else:
        if scrollbar.winfo_ismapped():
            scrollbar.grid_remove()

    text_widget.after(interval, check_scrollbar_visibility, text_widget, scrollbar, widget_height, bar_column, bar_row, interval)

