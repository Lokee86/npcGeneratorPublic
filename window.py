import tkinter as tk
from screeninfo import get_monitors
from constants import *
import functionality as fn


class CreatureCreatorApp:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height        
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE(title))
        self.create_screen()    
        self.choose_creature_type()
        self.monster_window()
        self.npc_window()

    # Get the primary monitor's screen size
    def screen_parameters(self):
        monitors = get_monitors()
        for monitor in monitors:
            if monitor.is_primary:
                screen_width = monitor.width
                screen_height = monitor.height
                return screen_width, screen_height
        screen_width = monitors[0].width
        screen_height = monitors[0].height
        return screen_width, screen_height

    # Set the window size to half the screen's hieght and width, center it on screen, and apply the geometry
    def create_screen(self):
        screen_width, screen_height = self.screen_parameters()
        window_width = int(screen_width * self.width)
        window_height = int(screen_height * self.height)
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def choose_creature_type(self):
        pass

    def monster_window(self):
        pass

    def npc_window(self):
        pass
    
    def run(self):
        self.root.mainloop()

class ChooseCreature(CreatureCreatorApp):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def choose_creature_type(self):
        # Labels
        self.intro = tk.Label(self.root, text="Welcome to Creature Creator", font=(DISPLAY_FONT, 20))
        self.intro.pack(pady="20")
        self.choose_label = tk.Label(self.root, text="What kind of creature would you like to create?", font=(DISPLAY_FONT, 16))
        self.choose_label.pack(pady="10")
        
        # Buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()
        
        self.monster_button = tk.Button(self.button_frame, text="Monster", font=(DISPLAY_FONT, 13, "bold"), command=self.monster)
        self.monster_button.grid(column=0, row=0)
        self.npc_button = tk.Button(self.button_frame, text="NPC", font=(DISPLAY_FONT, 13, "bold"), command=self.npc)
        self.npc_button.grid(column=1, row=0)
    
    def monster(self):
        self.root.destroy()
        app = WindowMonster(CREATION_WIDTH_FACTOR, CREATION_HEIGHT_FACTOR, MONSTER_TITLE)
        app.run()

    def npc(self):
        self.root.destroy()
        app = WindowNPC(CREATION_WIDTH_FACTOR, CREATION_HEIGHT_FACTOR, NPC_TITLE)
        app.run()

class WindowMonster(CreatureCreatorApp):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def monster_window(self):
        # Create Stat line labels & inputs
        validate_cmd = self.root.register(fn.validate_stat_length)
        
        self.stats = tk.Frame(self.root)
        self.stats.pack(pady='10')

        self.stats_values = tk.Frame(self.stats)
        self.stats_values.grid(column=0, row=0)
        
        # Create a list to track entry widgets for generation and input gathering
        self.stat_entries = []
        # Create the label and input widgets for stats
        for stat in range(0, len(STATS)):
            lbl = tk.Label(self.stats_values, padx='5', text=STATS[stat], font=(DISPLAY_FONT, 14))
            lbl.grid(column=stat, row=0)
            entry = tk.Entry(self.stats_values,
                                width=2,
                                validate='key',
                                validatecommand=(validate_cmd, '%P', 2))
            entry.grid(column=stat, row=1)
            self.stat_entries.append((STATS[stat], entry))

        self.stat_gen_check = tk.Checkbutton(self.stats, text="Generate Stats")
        self.stat_gen_check.grid(column=1, row=0)
        

class WindowNPC(WindowMonster):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def npc_window(self):
        pass

if __name__ == "__main__":
    app = ChooseCreature(DIALOG_WIDTH_FACTOR, DIALOG_HEIGHT_FACTOR, INTRO_TITLE)
    app.run()
