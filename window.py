import tkinter
from screeninfo import get_monitors

root = tkinter.Tk()
root.title("Creature Creator")

# Get the primary monitor's screen size
monitors = get_monitors()
for monitor in monitors:
    if monitor.is_primary:
        screen_width = monitor.width
        screen_height = monitor.height
        break

# Set the window size to half the screen's hieght and width, center it on screen, and apply the geometry
window_width = int(screen_width * 0.5)
window_height = int(screen_height * 0.5)
x_position = (screen_width + window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")



root.mainloop()