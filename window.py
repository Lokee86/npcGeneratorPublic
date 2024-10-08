import tkinter as tk
from screeninfo import get_monitors
from classes import *
from constants import *
import gui_functions as gfn
import functionality as fn


class CreatureCreatorApp:
    def __init__(self, width, height, title):
        self.random_names: dict = {"firsts": [], "lasts": []}
        self.width = width
        self.height = height        
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE(title))
        self.create_screen()

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
        self.root.resizable(width=False, height=False)

    def run(self):
        self.root.mainloop()

class ChooseCreature(CreatureCreatorApp):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
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
        creature = fn.creature_type("monster")
        app = MonsterWindow(CREATURE_WIDTH_FACTOR, CREATURE_HEIGHT_FACTOR, MONSTER_TITLE, creature)
        app.run()

    def npc(self):
        self.root.destroy()
        creature = fn.creature_type("npc")
        app = NPCWindow(NPC_WIDTH_FACTOR, NPC_HEIGHT_FACTOR, NPC_TITLE)
        app.run()

class MonsterWindow(CreatureCreatorApp):
    def __init__(self, width, height, title, creature):
        super().__init__(width, height, title)
        self.creature = creature 
        # Register validation functions for input fields
        validate_lngth = self.root.register(gfn.validate_length)
        validate_alpha = self.root.register(gfn.validate_alphabetic)

        # Create Master frame
        self.master_frame = tk.Frame(self.root)
        self.master_frame.pack()
        
        # Generate Basics frames
        self.basics_frame = tk.Frame(self.master_frame)
        self.basics_frame.grid(column=3, row=0)
        self.basics_frame.columnconfigure(2, minsize=25)

        # Create Genre input
        self.genre_var = tk.StringVar()
        self.genre_label = tk.Label(self.basics_frame, padx='5', text='Genre: ', font=(DISPLAY_FONT, 14))
        self.genre_entry = tk.Entry(self.basics_frame,
                                    width=14,
                                    validate='key',
                                    validatecommand=(validate_alpha, '%S'),
                                    textvariable=self.genre_var)
        self.genre_gen_check = tk.BooleanVar()
        self.genre_gen_check_box = tk.Checkbutton(self.basics_frame, text="Generate Genre", variable=self.genre_gen_check)
        self.genre_label.grid(column=0, row=0, sticky=tk.E)
        self.genre_entry.grid(column=1, row=0, sticky=tk.W)
        self.genre_gen_check_box.grid(column=3, row=0, sticky=tk.W)

        # Generate Name input
        self.name_var = tk.StringVar()
        self.name_label = tk.Label(self.basics_frame, padx='5', text='Name: ', font=(DISPLAY_FONT, 14))
        self.name_entry = tk.Entry(self.basics_frame, width=30,
                                   validate='key',
                                   validatecommand=(validate_lngth, '%P', 40),
                                   textvariable=self.name_var)
        self.name_gen_check = tk.BooleanVar()
        self.name_gen_check_box = tk.Checkbutton(self.basics_frame, text="Generate Name", variable=self.name_gen_check)
        self.name_label.grid(column=0, row=1, sticky=tk.E)
        self.name_entry.grid(column=1, row=1, sticky=tk.W)
        self.name_gen_check_box.grid(column=3, row=1, sticky=tk.W)

        # Generate Category input
        self.category_var = tk.StringVar()
        self.category_label = tk.Label(self.basics_frame, padx='5', text='Category: ', font=(DISPLAY_FONT, 14))
        self.category_entry = tk.Entry(self.basics_frame, width=12, textvariable=self.category_var)
        self.category_gen_check = tk.BooleanVar()
        self.category_gen_check_box = tk.Checkbutton(self.basics_frame, text="Generate Category", variable=self.category_gen_check)
        self.category_label.grid(column=0, row=3, sticky=tk.E)
        self.category_entry.grid(column=1, row=3, sticky=tk.W)
        self.category_gen_check_box.grid(column=3, row=3, sticky=tk.W)

        # Generate Size input
        self.size_var = tk.StringVar()
        self.size_label = tk.Label(self.basics_frame, padx='5', text='Size: ', font=(DISPLAY_FONT, 14))
        self.size_entry = tk.Entry(self.basics_frame, width=12, textvariable=self.size_var)
        self.size_gen_check = tk.BooleanVar()
        self.size_gen_check_box = tk.Checkbutton(self.basics_frame, text="Generate Size", variable=self.size_gen_check)
        self.size_label.grid(column=0, row=4, sticky=tk.E)
        self.size_entry.grid(column=1, row=4, sticky=tk.W)
        self.size_gen_check_box.grid(column=3, row=4, sticky=tk.W)

        # Generate Habitat input
        self.habitat_var = tk.StringVar()
        self.habitat_label = tk.Label(self.basics_frame, padx='5', text='Habitat: ', font=(DISPLAY_FONT, 14))
        self.habitat_entry = tk.Entry(self.basics_frame, width=12, textvariable=self.habitat_var)
        self.habitat_gen_check = tk.BooleanVar()
        self.habitat_gen_check_box = tk.Checkbutton(self.basics_frame, text="Generate Habitat", variable=self.habitat_gen_check)
        self.habitat_label.grid(column=0, row=5, sticky=tk.E)
        self.habitat_entry.grid(column=1, row=5, sticky=tk.W)
        self.habitat_gen_check_box.grid(column=3, row=5, sticky=tk.W)

        # Generate Skills input
        self.skills_var = tk.StringVar()
        self.skills_label = tk.Label(self.basics_frame, padx='5', text='Skills: ', font=(DISPLAY_FONT, 14))
        self.skills_entry = tk.Text(self.basics_frame, wrap='word', width=30, height=3)
        self.skills_gen_check = tk.BooleanVar()
        self.skills_gen_check_box = tk.Checkbutton(self.basics_frame, text="Generate Skills", variable=self.skills_gen_check)
        self.skills_label.grid(column=0, row=6, sticky=tk.E)
        self.skills_entry.grid(column=1, row=6, sticky=tk.W, pady="8")
        self.skills_gen_check_box.grid(column=3, row=6, sticky=tk.W)
        self.skills_entry.bind("<<Modified>>", lambda event: gfn.update_variable_from_widget(self.skills_var, event))
        self.skills_var.trace_add("write", lambda *args: gfn.update_widget_from_variable(self.skills_var, self.skills_entry))


        # Generate Scrollbar for skills, display when necessary

        self.skills_scroll_bar = tk.Scrollbar(self.basics_frame, command=self.skills_entry.yview)
        self.skills_scroll_bar.grid(column=2, row=6, sticky=tk.NS)
        self.skills_entry.config(yscrollcommand=self.skills_scroll_bar.set)
        gfn.check_scrollbar_visibility(self.skills_entry, self.skills_scroll_bar, 3, 30, 2, 6)

        # Create Stat line labels & inputs
        # Frames for stats and Stat buttons
        self.stats = tk.Frame(self.master_frame)
        self.stats.grid(column=3, row=1)

        self.stats_values = tk.Frame(self.stats)
        self.stats_values.grid(column=0, row=0)


        # Create a list to track entry widgets for generation and input gathering
        self.stat_entries = []
        # Create the label and input widgets for stats
        for stat in range(0, len(GSTATS)):
            var = tk.StringVar()
            lbl = tk.Label(self.stats_values, padx='5', text=GSTATS[stat], font=(DISPLAY_FONT, 14))
            lbl.grid(column=stat, row=0)
            entry = tk.Entry(self.stats_values,
                                width=2,
                                validate='key',
                                validatecommand=(validate_lngth, '%P', 2),
                                textvariable=var)
            entry.grid(column=stat, row=1)
            self.stat_entries.append((GSTATS[stat], entry, var))

        self.stat_gen_check = tk.BooleanVar()
        self.stat_gen_check_box = tk.Checkbutton(self.stats, text="Generate Stats", variable=self.stat_gen_check)
        self.stat_gen_check_box.grid(column=0, row=1)
        
        # Frame for how-to-play information
        self.play_info_frame = tk.Frame(self.master_frame)
        self.play_info_frame.grid(column=3, row=2)
        self.play_info_frame.columnconfigure(2, minsize=30)
        
        # Create Abilities input
        
        self.abilities_var = tk.StringVar()
        self.abilities_label = tk.Label(self.play_info_frame, padx='5', text='Abilities: ', font=(DISPLAY_FONT, 14))
        self.abilities_entry = tk.Text(self.play_info_frame, wrap='word', width=45, height=7)
        self.abilities_gen_check = tk.BooleanVar()
        self.abilities_gen_check_box = tk.Checkbutton(self.play_info_frame, text="Generate Abilities", variable=self.abilities_gen_check)
        self.abilities_label.grid(column=0, row=0, sticky=tk.NE)
        self.abilities_entry.grid(column=1, row=0, sticky=tk.W, pady='5')
        self.abilities_gen_check_box.grid(column=3, row=0, sticky=tk.W)
        self.abilities_entry.bind("<<Modified>>", lambda event: gfn.update_variable_from_widget(self.abilities_var, event))
        self.abilities_var.trace_add("write", lambda *args: gfn.update_widget_from_variable(self.abilities_var, self.abilities_entry))

        # Generate Scrollbar for abilities, display when necessary
        self.abilities_scroll_bar = tk.Scrollbar(self.play_info_frame, command=self.abilities_entry.yview)
        self.abilities_scroll_bar.grid(column=2, row=0, sticky=tk.NS)
        self.abilities_entry.config(yscrollcommand=self.abilities_scroll_bar.set)
        gfn.check_scrollbar_visibility(self.abilities_entry, self.abilities_scroll_bar, 7, 45, 2, 0)  

        # Create Motivations input
        self.motivations_var = tk.StringVar()
        self.motivations_label = tk.Label(self.play_info_frame, padx='5', text='Motivations: ', font=(DISPLAY_FONT, 14))
        self.motivations_entry = tk.Text(self.play_info_frame, wrap='word', width=45, height=7)
        self.motivations_gen_check = tk.BooleanVar()
        self.motivations_gen_check_box = tk.Checkbutton(self.play_info_frame, text="Generate Motivations", variable=self.motivations_gen_check)
        self.motivations_label.grid(column=0, row=1, sticky=tk.NE)
        self.motivations_entry.grid(column=1, row=1, sticky=tk.W, pady='5')
        self.motivations_gen_check_box.grid(column=3, row=1, sticky=tk.W, padx=(0, 20))
        self.motivations_entry.bind("<<Modified>>", lambda event: gfn.update_variable_from_widget(self.motivations_var, event))
        self.motivations_var.trace_add("write", lambda *args: gfn.update_widget_from_variable(self.motivations_var, self.motivations_entry))


        # Generate Scrollbar for motivations, display when necessary
        self.motivations_scroll_bar = tk.Scrollbar(self.play_info_frame, command=self.motivations_entry.yview)
        self.motivations_scroll_bar.grid(column=2, row=0, sticky=tk.NS)
        self.motivations_entry.config(yscrollcommand=self.motivations_scroll_bar.set)
        gfn.check_scrollbar_visibility(self.motivations_entry, self.motivations_scroll_bar, 7, 45, 2, 1)  

        # Create Tactics input
        self.tactics_var = tk.StringVar()
        self.tactics_label = tk.Label(self.play_info_frame, padx='5', text='Tactics: ', font=(DISPLAY_FONT, 14))
        self.tactics_entry = tk.Text(self.play_info_frame, wrap='word', width=45, height=7)
        self.tactics_gen_check = tk.BooleanVar()
        self.tactics_gen_check_box = tk.Checkbutton(self.play_info_frame, text="Generate Tactics", variable=self.tactics_gen_check)
        self.tactics_label.grid(column=0, row=2, sticky=tk.NE)
        self.tactics_entry.grid(column=1, row=2, sticky=tk.W, pady='5')
        self.tactics_gen_check_box.grid(column=3, row=2, sticky=tk.W)
        self.tactics_entry.bind("<<Modified>>", lambda event: gfn.update_variable_from_widget(self.tactics_var, event))
        self.tactics_var.trace_add("write", lambda *args: gfn.update_widget_from_variable(self.tactics_var, self.tactics_entry))

        # Generate Scrollbar for tactics, display when necessary
        self.tactics_scroll_bar = tk.Scrollbar(self.play_info_frame, command=self.tactics_entry.yview)
        self.tactics_scroll_bar.grid(column=2, row=1, sticky=tk.NS)
        self.tactics_entry.config(yscrollcommand=self.tactics_scroll_bar.set)
        gfn.check_scrollbar_visibility(self.tactics_entry, self.tactics_scroll_bar, 7, 45, 2, 2)

        # Radio button frames
        self.select_enemy_frame = tk.Frame(self.master_frame)
        self.select_enemy_frame.grid(column=3, row=3, pady='5')
        
        # Creature style selection
        self.select_enemy_var = tk.StringVar()
        self.select_non_combatant = tk.Radiobutton(self.select_enemy_frame, text="Non-Combatant", variable=self.select_enemy_var, value="non_combatant")
        self.select_minions = tk.Radiobutton(self.select_enemy_frame, text="Minion", variable=self.select_enemy_var, value="minions")
        self.select_normal_enemy = tk.Radiobutton(self.select_enemy_frame, text="Normal Enemy", variable=self.select_enemy_var, value="normal_enemy")
        self.select_elite_enemy = tk.Radiobutton(self.select_enemy_frame, text="Elite Enemy", variable=self.select_enemy_var, value="elite_enemy")
        self.select_super_elites = tk.Radiobutton(self.select_enemy_frame, text="Super Elite", variable=self.select_enemy_var, value="super_elite")
        self.select_boss_enemy = tk.Radiobutton(self.select_enemy_frame, text="Boss Enemy", variable=self.select_enemy_var, value="boss_enemy")
        self.select_epic_boss = tk.Radiobutton(self.select_enemy_frame, text="Epic Boss", variable=self.select_enemy_var, value="epic_boss")
        self.select_legendary_boss = tk.Radiobutton(self.select_enemy_frame, text="Legendary Boss", variable=self.select_enemy_var, value="legendary_boss")
        self.select_enemy_gen_check = tk.BooleanVar()
        self.select_enemy_gen_check_box = tk.Checkbutton(self.select_enemy_frame, text="Generate Creature Type", variable=self.select_enemy_gen_check)

        self.select_non_combatant.grid(column=1, row=1, pady='5', padx='5')
        self.select_minions.grid(column=1, row=2, pady='5', padx='5')
        self.select_normal_enemy.grid(column=2, row=1, pady='5', padx='5')
        self.select_elite_enemy.grid(column=2, row=2, pady='5', padx='5')
        self.select_super_elites.grid(column=3, row=1, pady='5', padx='5')
        self.select_boss_enemy.grid(column=3, row=2, pady='5', padx='5')
        self.select_epic_boss.grid(column=4, row=1, pady='5', padx='5')
        self.select_legendary_boss.grid(column=4, row=2, pady='5', padx='5')
        self.select_enemy_gen_check_box.grid(column=1, row=3, pady='5', columnspan=4, sticky=tk.EW)


        # Frame for buttons
        self.button_frame = tk.Frame(self.master_frame)
        self.button_frame.grid(column=3, row=4, pady='5')

        # Save and Generate buttons
        self.generate_button = tk.Button(self.button_frame, text="Generate", font=(DISPLAY_FONT, 14), width=10, height=1, command=lambda: fn.main(self.creature, self))
        self.save_button = tk.Button(self.button_frame, text="Save", font=(DISPLAY_FONT, 14), width=10, height=1, command=lambda: fn.state_check(self.creature, self))
        self.generate_button.grid(column=0, row=1, padx='5')
        self.save_button.grid(column=1, row=1, padx='5')

        self.name_list_flag = False

    def add_name_list_check(self):
        if self.random_names["firsts"]:
            if self.name_list_flag == False:
                self.name_list_gen_check = tk.BooleanVar()
                self.name_list_gen_check_box = tk.Checkbutton(self.button_frame, text="Generate New Name List", variable=self.name_list_gen_check)
                self.name_list_gen_check_box.grid(column=0, row=0, columnspan=2, sticky=tk.EW)
                self.name_list_flag = True



class NPCWindow(CreatureCreatorApp): # This will inherit from the MonsterWindow when released
    def __init__(self, width, height, title):
        
        super().__init__(width, height, title)
        self.label = tk.Label(self.root, text="Under Development.", font=(DISPLAY_FONT, 30, "bold"))
        self.label.pack(pady="30")
        # validate_lngth = self.root.register(gfn.validate_length)
        # validate_alpha = self.root.register(gfn.validate_alphabetic)

        # self.npc_basics = {}        
        
        # for i in range(7, (7 + len(NPC_BASICS))):
        #     self.label = tk.Label(self.basics_frame, padx='5', text=f"{NPC_BASICS[i-7]}: ", font=(DISPLAY_FONT, 14))
        #     self.entry = tk.Entry(self.basics_frame, width=12,
        #                         validate='key',
        #                         validatecommand=(validate_lngth, '%P', 12))
        #     self.gen_check = tk.BooleanVar()
        #     self.check_box = tk.Checkbutton(self.basics_frame, text=f"Generate {NPC_BASICS[i-7]}", variable=self.gen_check)
        #     self.label.grid(column=0, row=i, sticky=tk.E)
        #     self.entry.grid(column=1, row=i, sticky=tk.W)
        #     self.check_box.grid(column=3, row=i, sticky=tk.W)
        #     self.npc_basics[NPC_BASICS[i-7]] = self.entry, self.gen_check

        # # Generate Species input
        # self.species_label = tk.Label(self.basics_frame, padx='5', text='Species: ', font=(DISPLAY_FONT, 14))
        # self.species_entry = tk.Entry(self.basics_frame, width=12)
        # self.species_gen_check = tk.BooleanVar()
        # self.species_gen_check_box = tk.Checkbutton(self.basics_frame, text="Generate Species", variable=self.species_gen_check)
        # self.species_label.grid(column=0, row=2, sticky=tk.E)
        # self.species_entry.grid(column=1, row=2, sticky=tk.W)
        # self.species_gen_check_box.grid(column=3, row=2, sticky=tk.W)

        

if __name__ == "__main__":
    app = ChooseCreature(DIALOG_WIDTH_FACTOR, DIALOG_HEIGHT_FACTOR, INTRO_TITLE)
    app.run()
