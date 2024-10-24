#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class testUI:
    def __init__(self, master=None):
        # build ui
        self.monster_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.monster_window.configure(height=200, width=200)
        self.monster_window.geometry("1422x735")
        self.monster_window.resizable(False, False)
        self.monster_window.title("Creature Creator")
        self.gameplay_frame = ttk.Frame(
            self.monster_window, name="gameplay_frame")
        self.gameplay_frame.configure(height=200, width=200)
        self.gameplay_label = ttk.Label(
            self.gameplay_frame, name="gameplay_label")
        self.gameplay_label.configure(
            font="{DejaVu Sans} 12 {bold}",
            text='Creature Creator by Laughing Skull Games')
        self.gameplay_label.grid(column=0, columnspan=5, pady="15 0", row=0)
        self.basic_info_frame = ttk.Frame(
            self.gameplay_frame, name="basic_info_frame")
        self.basic_info_frame.configure(height=200, width=200)
        self.name_label = ttk.Label(self.basic_info_frame, name="name_label")
        self.name_label.configure(text='Name:')
        self.name_label.grid(column=0, padx="0 5", row=0, sticky="e")
        self.type_label = ttk.Label(self.basic_info_frame, name="type_label")
        self.type_label.configure(text='          Type:')
        self.type_label.grid(column=0, padx="0 5", row=1, sticky="e")
        self.size_label = ttk.Label(self.basic_info_frame, name="size_label")
        self.size_label.configure(text='Size:')
        self.size_label.grid(column=0, padx="0 5", row=2, sticky="e")
        self.habitat_label = ttk.Label(
            self.basic_info_frame, name="habitat_label")
        self.habitat_label.configure(text='Habitat:')
        self.habitat_label.grid(column=0, padx="0 5", row=3, sticky="e")
        self.name_entry = tk.Entry(self.basic_info_frame, name="name_entry")
        self.name_var = tk.StringVar()
        self.name_entry.configure(textvariable=self.name_var, width=30)
        self.name_entry.grid(column=1, row=0, sticky="w")
        self.type_entry = tk.Entry(self.basic_info_frame, name="type_entry")
        self.type_var = tk.StringVar()
        self.type_entry.configure(textvariable=self.type_var, width=15)
        self.type_entry.grid(column=1, pady=10, row=1, sticky="w")
        self.size_entry = ttk.Combobox(
            self.basic_info_frame, name="size_entry")
        self.size_var = tk.StringVar()
        self.size_entry.configure(
            textvariable=self.size_var,
            values='"" Infinitesimal Miniscule Tiny Small Medium Large Huge Gargantuan Colossal Titanic Astronomical',
            width=10)
        self.size_entry.grid(column=1, row=2, sticky="w")
        self.habitat_entry = tk.Entry(
            self.basic_info_frame, name="habitat_entry")
        self.habitat_var = tk.StringVar()
        self.habitat_entry.configure(textvariable=self.habitat_var, width=15)
        self.habitat_entry.grid(column=1, pady=10, row=3, sticky="w")
        self.ac_label = ttk.Label(self.basic_info_frame, name="ac_label")
        self.ac_label.configure(text='AC: ')
        self.ac_label.grid(column=0, row=4, sticky="e")
        self.armor_type_frame = ttk.Frame(
            self.basic_info_frame, name="armor_type_frame")
        self.armor_type_frame.configure(height=200, width=200)
        self.armor_type_label = ttk.Label(
            self.armor_type_frame, name="armor_type_label")
        self.armor_type_label.configure(text='Armor Type: ')
        self.armor_type_label.grid(column=2, padx="15 0", row=0)
        self.armor_type_entry = tk.Entry(
            self.armor_type_frame, name="armor_type_entry")
        self.armor_type_var = tk.StringVar()
        self.armor_type_entry.configure(
            exportselection=True,
            font="TkDefaultFont",
            textvariable=self.armor_type_var,
            width=16)
        self.armor_type_entry.grid(column=3, row=0)
        self.armor_type_frame.grid(
            column=1,
            columnspan=2,
            padx="8 0",
            pady=0,
            row=4,
            sticky="e")
        self.ac_entry = tk.Entry(self.basic_info_frame, name="ac_entry")
        self.ac_var = tk.StringVar()
        self.ac_entry.configure(textvariable=self.ac_var, width=2)
        self.ac_entry.grid(column=1, row=4, sticky="w")
        self.hp_label = ttk.Label(self.basic_info_frame, name="hp_label")
        self.hp_label.configure(text='HP: ')
        self.hp_label.grid(column=0, row=5, sticky="e")
        self.hp_entry = tk.Entry(self.basic_info_frame, name="hp_entry")
        self.hp_var = tk.StringVar()
        self.hp_entry.configure(textvariable=self.hp_var, width=5)
        self.hp_entry.grid(column=1, pady=10, row=5, sticky="w")
        self.hit_dice_frame = ttk.Frame(
            self.basic_info_frame, name="hit_dice_frame")
        self.hit_dice_frame.configure(height=200, width=200)
        self.hitdice_label = ttk.Label(
            self.hit_dice_frame, name="hitdice_label")
        self.hitdice_label.configure(text='Hit Dice: ')
        self.hitdice_label.grid(column=0, row=0)
        self.hitdice_entry = tk.Entry(
            self.hit_dice_frame, name="hitdice_entry")
        self.hit_dice_var = tk.StringVar()
        self.hitdice_entry.configure(textvariable=self.hit_dice_var, width=11)
        self.hitdice_entry.grid(column=1, row=0)
        self.hit_dice_frame.grid(column=1, row=5)
        self.proficiency_frame = ttk.Frame(
            self.basic_info_frame, name="proficiency_frame")
        self.proficiency_frame.configure(height=200, width=200)
        self.proficiency_label = ttk.Label(
            self.proficiency_frame, name="proficiency_label")
        self.proficiency_label.configure(text='Proficiency Bonus: ')
        self.proficiency_label.grid(column=0, row=0)
        self.proficiency_entry = tk.Entry(
            self.proficiency_frame, name="proficiency_entry")
        self.prof_var = tk.StringVar()
        self.proficiency_entry.configure(textvariable=self.prof_var, width=2)
        self.proficiency_entry.grid(column=1, row=0)
        self.proficiency_frame.grid(column=3, padx="55 0", row=5, sticky="e")
        self.combat_role_frame = ttk.Labelframe(
            self.basic_info_frame, name="combat_role_frame")
        self.combat_role_frame.configure(
            height=200, text='Combat Role', width=200)
        self.artillery_radio = tk.Radiobutton(
            self.combat_role_frame, name="artillery_radio")
        self.combat_role = tk.StringVar(value='artillery')
        self.artillery_radio.configure(
            text='Artillery',
            value="artillery",
            variable=self.combat_role)
        self.artillery_radio.grid(column=0, row=0, sticky="w")
        self.brute_radio = tk.Radiobutton(
            self.combat_role_frame, name="brute_radio")
        self.brute_radio.configure(
            text='Brute',
            value="brute",
            variable=self.combat_role)
        self.brute_radio.grid(column=0, row=1, sticky="w")
        self.controller_radio = tk.Radiobutton(
            self.combat_role_frame, name="controller_radio")
        self.controller_radio.configure(
            text='Controller',
            value="controller",
            variable=self.combat_role)
        self.controller_radio.grid(column=0, row=2, sticky="w")
        self.no_role_radio = tk.Radiobutton(
            self.combat_role_frame, name="no_role_radio")
        self.no_role_radio.configure(
            overrelief="flat",
            text='None',
            value="no_role",
            variable=self.combat_role)
        self.no_role_radio.grid(column=0, row=3, sticky="w")
        self.lurker_radio = tk.Radiobutton(
            self.combat_role_frame, name="lurker_radio")
        self.lurker_radio.configure(
            text='Lurker',
            value="lurker",
            variable=self.combat_role)
        self.lurker_radio.grid(column=1, pady="3 0", row=0, sticky="w")
        self.skirmisher_radio = tk.Radiobutton(
            self.combat_role_frame, name="skirmisher_radio")
        self.skirmisher_radio.configure(
            text='Skirmisher',
            value="skirmisher",
            variable=self.combat_role)
        self.skirmisher_radio.grid(column=1, row=1, sticky="w")
        self.soldier_radio = tk.Radiobutton(
            self.combat_role_frame, name="soldier_radio")
        self.soldier_radio.configure(
            text='Soldier',
            value="soldier",
            variable=self.combat_role)
        self.soldier_radio.grid(column=1, row=2, sticky="w")
        self.combat_role_frame.grid(
            column=0,
            columnspan=2,
            ipadx=3,
            ipady=2,
            padx="0 5",
            pady="0 10",
            row=6,
            sticky="sw")
        self.speed_frame = ttk.Labelframe(
            self.basic_info_frame, name="speed_frame")
        self.speed_frame.configure(height=200, text='Speeds', width=200)
        self.speed_run_label = ttk.Label(
            self.speed_frame, name="speed_run_label")
        self.speed_run_label.configure(text='Run: ')
        self.speed_run_label.grid(column=0, row=0, sticky="e")
        self.speed_swim_label = ttk.Label(
            self.speed_frame, name="speed_swim_label")
        self.speed_swim_label.configure(text='Swim: ')
        self.speed_swim_label.grid(column=0, row=1, sticky="e")
        self.speed_fly_label = ttk.Label(
            self.speed_frame, name="speed_fly_label")
        self.speed_fly_label.configure(text='Fly: ')
        self.speed_fly_label.grid(column=0, row=2, sticky="e")
        self.speed_burrow_label = ttk.Label(
            self.speed_frame, name="speed_burrow_label")
        self.speed_burrow_label.configure(text='Burrow: ')
        self.speed_burrow_label.grid(column=0, padx="10 0", row=3, sticky="e")
        self.speed_run_entry = tk.Entry(
            self.speed_frame, name="speed_run_entry")
        self.run_var = tk.StringVar()
        self.speed_run_entry.configure(textvariable=self.run_var, width=5)
        self.speed_run_entry.grid(
            column=1,
            padx="0 10",
            pady="0 9",
            row=0,
            sticky="w")
        self.speed_swim_entry = tk.Entry(
            self.speed_frame, name="speed_swim_entry")
        self.swim_var = tk.StringVar()
        self.speed_swim_entry.configure(textvariable=self.swim_var, width=5)
        self.speed_swim_entry.grid(column=1, row=1, sticky="w")
        self.speed_fly_entry = tk.Entry(
            self.speed_frame, name="speed_fly_entry")
        self.fly_var = tk.StringVar()
        self.speed_fly_entry.configure(textvariable=self.fly_var, width=5)
        self.speed_fly_entry.grid(column=1, pady=9, row=2, sticky="w")
        self.speed_burrow_entry = tk.Entry(
            self.speed_frame, name="speed_burrow_entry")
        self.burrow_var = tk.StringVar()
        self.speed_burrow_entry.configure(
            textvariable=self.burrow_var, width=5)
        self.speed_burrow_entry.grid(column=1, row=3, sticky="w")
        self.speed_frame.grid(
            column=1,
            columnspan=3,
            ipady=2,
            padx="0 33",
            pady="0 10",
            row=6,
            sticky="s")
        self.basic_info_frame.grid(
            column=0,
            columnspan=2,
            padx=0,
            pady="14 0",
            row=1,
            rowspan=2,
            sticky="w")
        self.ability_save_frame = ttk.Frame(
            self.gameplay_frame, name="ability_save_frame")
        self.ability_save_frame.configure(height=200, width=200)
        self.abilities_frame = ttk.Labelframe(
            self.ability_save_frame, name="abilities_frame")
        self.abilities_frame.configure(height=200, text='Abilities', width=200)
        self.str_label = ttk.Label(self.abilities_frame, name="str_label")
        self.str_label.configure(font="{DejaVu Sans} 7 {}", text='STR')
        self.str_label.grid(column=0, padx="7 0", row=0)
        self.dex_label = ttk.Label(self.abilities_frame, name="dex_label")
        self.dex_label.configure(font="{DejaVu Sans} 7 {}", text='DEX')
        self.dex_label.grid(column=1, padx=7, row=0)
        self.con_label = ttk.Label(self.abilities_frame, name="con_label")
        self.con_label.configure(font="{DejaVu Sans} 7 {}", text='CON')
        self.con_label.grid(column=2, row=0)
        self.int_label = ttk.Label(self.abilities_frame, name="int_label")
        self.int_label.configure(font="{DejaVu Sans} 7 {}", text='INT')
        self.int_label.grid(column=4, row=0)
        self.wis_label = ttk.Label(self.abilities_frame, name="wis_label")
        self.wis_label.configure(font="{DejaVu Sans} 7 {}", text='WIS')
        self.wis_label.grid(column=3, padx=7, row=0)
        self.cha_label = ttk.Label(self.abilities_frame, name="cha_label")
        self.cha_label.configure(font="{DejaVu Sans} 7 {}", text='CHA')
        self.cha_label.grid(column=5, padx=7, row=0)
        self.str_entry = tk.Entry(self.abilities_frame, name="str_entry")
        self.str_var = tk.StringVar()
        self.str_entry.configure(textvariable=self.str_var, width=2)
        self.str_entry.grid(column=0, pady="0 5", row=1)
        self.dex_entry = tk.Entry(self.abilities_frame, name="dex_entry")
        self.dex_var = tk.StringVar()
        self.dex_entry.configure(textvariable=self.dex_var, width=2)
        self.dex_entry.grid(column=1, row=1, sticky="n")
        self.con_entry = tk.Entry(self.abilities_frame, name="con_entry")
        self.con_var = tk.StringVar()
        self.con_entry.configure(textvariable=self.con_var, width=2)
        self.con_entry.grid(column=2, row=1, sticky="n")
        self.wis_entry = tk.Entry(self.abilities_frame, name="wis_entry")
        self.wis_var = tk.StringVar()
        self.wis_entry.configure(textvariable=self.wis_var, width=2)
        self.wis_entry.grid(column=3, row=1, sticky="n")
        self.int_entry = tk.Entry(self.abilities_frame, name="int_entry")
        self.int_var = tk.StringVar()
        self.int_entry.configure(textvariable=self.int_var, width=2)
        self.int_entry.grid(column=4, row=1, sticky="n")
        self.cha_entry = tk.Entry(self.abilities_frame, name="cha_entry")
        self.cha_var = tk.StringVar()
        self.cha_entry.configure(textvariable=self.cha_var, width=2)
        self.cha_entry.grid(column=5, row=1, sticky="n")
        self.abilities_frame.grid(column=0, row=0)
        self.saving_throw_frame = ttk.Labelframe(
            self.ability_save_frame, name="saving_throw_frame")
        self.saving_throw_frame.configure(
            height=200, text='Saving Throws', width=200)
        self.str_save_label = ttk.Label(
            self.saving_throw_frame, name="str_save_label")
        self.str_save_label.configure(font="{DejaVu Sans} 7 {}", text='STR')
        self.str_save_label.grid(column=0, padx="10 0", row=0)
        self.dex_save_label = ttk.Label(
            self.saving_throw_frame, name="dex_save_label")
        self.dex_save_label.configure(font="{DejaVu Sans} 7 {}", text='DEX')
        self.dex_save_label.grid(column=1, row=0)
        self.con_save_label = ttk.Label(
            self.saving_throw_frame, name="con_save_label")
        self.con_save_label.configure(font="{DejaVu Sans} 7 {}", text='CON')
        self.con_save_label.grid(column=2, row=0)
        self.int_save_label = ttk.Label(
            self.saving_throw_frame, name="int_save_label")
        self.int_save_label.configure(font="{DejaVu Sans} 7 {}", text='INT')
        self.int_save_label.grid(column=3, row=0)
        self.wis_save_label = ttk.Label(
            self.saving_throw_frame, name="wis_save_label")
        self.wis_save_label.configure(font="{DejaVu Sans} 7 {}", text='WIS')
        self.wis_save_label.grid(column=4, row=0)
        self.cha_save_label = ttk.Label(
            self.saving_throw_frame, name="cha_save_label")
        self.cha_save_label.configure(font="{DejaVu Sans} 7 {}", text='CHA')
        self.cha_save_label.grid(column=5, row=0)
        self.str_save_check_box = tk.Checkbutton(
            self.saving_throw_frame, name="str_save_check_box")
        self.str_save_var = tk.BooleanVar()
        self.str_save_check_box.configure(variable=self.str_save_var)
        self.str_save_check_box.grid(column=0, row=1)
        self.dex_save_check_box = tk.Checkbutton(
            self.saving_throw_frame, name="dex_save_check_box")
        self.dex_save_var = tk.BooleanVar()
        self.dex_save_check_box.configure(
            compound="top", state="normal", variable=self.dex_save_var)
        self.dex_save_check_box.grid(column=1, row=1)
        self.con_save_check_box = tk.Checkbutton(
            self.saving_throw_frame, name="con_save_check_box")
        self.con_save_var = tk.BooleanVar()
        self.con_save_check_box.configure(variable=self.con_save_var)
        self.con_save_check_box.grid(column=2, row=1)
        self.int_save_check_box = tk.Checkbutton(
            self.saving_throw_frame, name="int_save_check_box")
        self.int_save_var = tk.BooleanVar()
        self.int_save_check_box.configure(
            justify="center", variable=self.int_save_var)
        self.int_save_check_box.grid(column=3, row=1)
        self.wis_save_check_box = tk.Checkbutton(
            self.saving_throw_frame, name="wis_save_check_box")
        self.wis_save_var = tk.BooleanVar()
        self.wis_save_check_box.configure(variable=self.wis_save_var)
        self.wis_save_check_box.grid(column=4, row=1)
        self.cha_save_check_box = tk.Checkbutton(
            self.saving_throw_frame, name="cha_save_check_box")
        self.cha_save_var = tk.BooleanVar()
        self.cha_save_check_box.configure(variable=self.cha_save_var)
        self.cha_save_check_box.grid(column=5, row=1)
        self.saving_throw_frame.grid(
            column=0, ipadx=5, pady="20 0", row=2, sticky="s")
        self.ability_save_frame.grid(column=1, row=1, sticky="ne")
        self.unit_type_frame = ttk.Labelframe(
            self.gameplay_frame, name="unit_type_frame")
        self.unit_type_frame.configure(height=200, text='Unit Type', width=200)
        self.noncombatant_radio = tk.Radiobutton(
            self.unit_type_frame, name="noncombatant_radio")
        self.unit_type = tk.StringVar(value='non-combatant')
        self.noncombatant_radio.configure(
            text='Non-Combat',
            value="non-combatant",
            variable=self.unit_type)
        self.noncombatant_radio.grid(
            column=0, padx=5, pady="0 3", row=0, sticky="w")
        self.minion_radio = tk.Radiobutton(
            self.unit_type_frame, name="minion_radio")
        self.minion_radio.configure(
            text='Minion',
            value="minion",
            variable=self.unit_type)
        self.minion_radio.grid(column=0, padx=5, row=1, sticky="w")
        self.normal_enemy_radio = tk.Radiobutton(
            self.unit_type_frame, name="normal_enemy_radio")
        self.normal_enemy_radio.configure(
            text='Standard',
            value="normal_enemy",
            variable=self.unit_type)
        self.normal_enemy_radio.grid(column=0, padx=5, row=2, sticky="w")
        self.elite_radio = tk.Radiobutton(
            self.unit_type_frame, name="elite_radio")
        self.elite_radio.configure(
            text='Elite',
            value="elite",
            variable=self.unit_type)
        self.elite_radio.grid(column=0, padx=5, row=3, sticky="w")
        self.mini_boss_radio = tk.Radiobutton(
            self.unit_type_frame, name="mini_boss_radio")
        self.mini_boss_radio.configure(
            text='Mini-Boss',
            value="mini_boss",
            variable=self.unit_type)
        self.mini_boss_radio.grid(column=1, row=0, sticky="w")
        self.boss_radio = tk.Radiobutton(
            self.unit_type_frame, name="boss_radio")
        self.boss_radio.configure(
            state="normal",
            text='Boss',
            value="boss",
            variable=self.unit_type)
        self.boss_radio.grid(column=1, row=1, sticky="w")
        self.epic_boss_radio = tk.Radiobutton(
            self.unit_type_frame, name="epic_boss_radio")
        self.epic_boss_radio.configure(
            text='Epic Boss',
            value="epic_boss",
            variable=self.unit_type)
        self.epic_boss_radio.grid(column=1, row=2, sticky="w")
        self.legendary_boss_radio = tk.Radiobutton(
            self.unit_type_frame, name="legendary_boss_radio")
        self.legendary_boss_radio.configure(
            text='Legendary',
            value="legendary_boss",
            variable=self.unit_type)
        self.legendary_boss_radio.grid(column=1, padx="0 5", row=3, sticky="w")
        self.unit_type_frame.grid(
            column=1,
            ipady=2,
            padx="6 0",
            pady=10,
            row=2,
            sticky="s")
        self.vuln_resist_immune_frame = ttk.Labelframe(
            self.gameplay_frame, name="vuln_resist_immune_frame")
        self.vuln_resist_immune_frame.configure(
            height=200, text='Damage Tuning', width=200)
        self.std_tuning_frame = ttk.Frame(
            self.vuln_resist_immune_frame,
            name="std_tuning_frame")
        self.std_tuning_frame.configure(height=200, width=200)
        self.std_tuning_label = ttk.Label(
            self.std_tuning_frame, name="std_tuning_label")
        self.std_tuning_label.configure(
            font="{DejaVu Sans} 8 {bold}", text='Standard')
        self.std_tuning_label.grid(column=0, padx="10 0", row=0)
        self.std_tuning_radio_frame = ttk.Frame(
            self.std_tuning_frame, name="std_tuning_radio_frame")
        self.std_tuning_radio_frame.configure(height=200, width=200)
        self.bludgeon_std_radio = tk.Radiobutton(
            self.std_tuning_radio_frame, name="bludgeon_std_radio")
        self.bludgeon_tuning = tk.IntVar(value=0)
        self.bludgeon_std_radio.configure(
            value=0, variable=self.bludgeon_tuning)
        self.bludgeon_std_radio.grid(column=0, row=0)
        self.piercing_std_radio = tk.Radiobutton(
            self.std_tuning_radio_frame, name="piercing_std_radio")
        self.piercing_tuning = tk.IntVar(value=0)
        self.piercing_std_radio.configure(
            value=0, variable=self.piercing_tuning)
        self.piercing_std_radio.grid(column=0, row=1)
        self.slashing_std_radio = tk.Radiobutton(
            self.std_tuning_radio_frame, name="slashing_std_radio")
        self.slashing_tuning = tk.IntVar(value=0)
        self.slashing_std_radio.configure(
            value=0, variable=self.slashing_tuning)
        self.slashing_std_radio.grid(column=0, row=2)
        self.acid_std_radio = tk.Radiobutton(
            self.std_tuning_radio_frame, name="acid_std_radio")
        self.acid_tuning = tk.IntVar(value=0)
        self.acid_std_radio.configure(value=0, variable=self.acid_tuning)
        self.acid_std_radio.grid(column=0, row=3)
        self.cold_std_radio = tk.Radiobutton(
            self.std_tuning_radio_frame, name="cold_std_radio")
        self.cold_tuning = tk.IntVar(value=0)
        self.cold_std_radio.configure(value=0, variable=self.cold_tuning)
        self.cold_std_radio.grid(column=0, row=4)
        self.fire_std_radio = tk.Radiobutton(
            self.std_tuning_radio_frame, name="fire_std_radio")
        self.fire_tuning = tk.IntVar(value=0)
        self.fire_std_radio.configure(value=0, variable=self.fire_tuning)
        self.fire_std_radio.grid(column=0, row=5)
        self.lightning_std_radio = tk.Radiobutton(
            self.std_tuning_radio_frame, name="lightning_std_radio")
        self.lightining_tuning = tk.IntVar(value=0)
        self.lightning_std_radio.configure(
            value=0, variable=self.lightining_tuning)
        self.lightning_std_radio.grid(column=0, row=6)
        self.poison_std_tuning = tk.Radiobutton(
            self.std_tuning_radio_frame, name="poison_std_tuning")
        self.poison_tuning = tk.IntVar(value=0)
        self.poison_std_tuning.configure(value=0, variable=self.poison_tuning)
        self.poison_std_tuning.grid(column=0, row=7)
        self.thunder_std_radio = tk.Radiobutton(
            self.std_tuning_radio_frame, name="thunder_std_radio")
        self.thunder_tuning = tk.IntVar(value=0)
        self.thunder_std_radio.configure(value=0, variable=self.thunder_tuning)
        self.thunder_std_radio.grid(column=0, row=8)
        self.force_std_radio = tk.Radiobutton(
            self.std_tuning_radio_frame, name="force_std_radio")
        self.force_tuning = tk.IntVar(value=0)
        self.force_std_radio.configure(value=0, variable=self.force_tuning)
        self.force_std_radio.grid(column=0, row=9)
        self.necrotic_std_radio = tk.Radiobutton(
            self.std_tuning_radio_frame, name="necrotic_std_radio")
        self.necrotic_tuning = tk.IntVar(value=0)
        self.necrotic_std_radio.configure(
            value=0, variable=self.necrotic_tuning)
        self.necrotic_std_radio.grid(column=0, row=10)
        self.radiant_std_radio = tk.Radiobutton(
            self.std_tuning_radio_frame, name="radiant_std_radio")
        self.radiant_tuning = tk.IntVar(value=0)
        self.radiant_std_radio.configure(value=0, variable=self.radiant_tuning)
        self.radiant_std_radio.grid(column=0, row=11)
        self.psychic_std_radio = tk.Radiobutton(
            self.std_tuning_radio_frame, name="psychic_std_radio")
        self.psychic_tuning = tk.StringVar(value='0')
        self.psychic_std_radio.configure(value=0, variable=self.psychic_tuning)
        self.psychic_std_radio.grid(column=0, row=12)
        self.std_tuning_radio_frame.grid(column=0, row=1)
        self.std_tuning_frame.grid(column=0, row=0)
        self.vuln_tuning_frame = ttk.Frame(
            self.vuln_resist_immune_frame,
            name="vuln_tuning_frame")
        self.vuln_tuning_frame.configure(height=200, width=200)
        self.vuln_tuning_label = ttk.Label(
            self.vuln_tuning_frame, name="vuln_tuning_label")
        self.vuln_tuning_label.configure(
            font="{DejaVu Sans} 8 {bold}", text='Vuln')
        self.vuln_tuning_label.grid(column=0, padx="10 0", row=0)
        self.vuln_tuning_radio_frame = ttk.Frame(
            self.vuln_tuning_frame, name="vuln_tuning_radio_frame")
        self.vuln_tuning_radio_frame.configure(height=200, width=200)
        self.bludgeon_vuln_radio = tk.Radiobutton(
            self.vuln_tuning_radio_frame, name="bludgeon_vuln_radio")
        self.bludgeon_vuln_radio.configure(
            value=1, variable=self.bludgeon_tuning)
        self.bludgeon_vuln_radio.grid(column=0, row=0)
        self.piercing_vuln_radio = tk.Radiobutton(
            self.vuln_tuning_radio_frame, name="piercing_vuln_radio")
        self.piercing_vuln_radio.configure(
            value=1, variable=self.piercing_tuning)
        self.piercing_vuln_radio.grid(column=0, row=1)
        self.slashing_vuln_radio = tk.Radiobutton(
            self.vuln_tuning_radio_frame, name="slashing_vuln_radio")
        self.slashing_vuln_radio.configure(
            value=1, variable=self.slashing_tuning)
        self.slashing_vuln_radio.grid(column=0, row=2)
        self.acid_vuln_radio = tk.Radiobutton(
            self.vuln_tuning_radio_frame, name="acid_vuln_radio")
        self.acid_vuln_radio.configure(value=1, variable=self.acid_tuning)
        self.acid_vuln_radio.grid(column=0, row=3)
        self.cold_vuln_radio = tk.Radiobutton(
            self.vuln_tuning_radio_frame, name="cold_vuln_radio")
        self.cold_vuln_radio.configure(value=1, variable=self.cold_tuning)
        self.cold_vuln_radio.grid(column=0, row=4)
        self.fire_vuln_radio = tk.Radiobutton(
            self.vuln_tuning_radio_frame, name="fire_vuln_radio")
        self.fire_vuln_radio.configure(value=1, variable=self.fire_tuning)
        self.fire_vuln_radio.grid(column=0, row=5)
        self.lightning_vuln_radio = tk.Radiobutton(
            self.vuln_tuning_radio_frame, name="lightning_vuln_radio")
        self.lightning_vuln_radio.configure(
            value=1, variable=self.lightining_tuning)
        self.lightning_vuln_radio.grid(column=0, row=6)
        self.poison_vuln_tuning = tk.Radiobutton(
            self.vuln_tuning_radio_frame, name="poison_vuln_tuning")
        self.poison_vuln_tuning.configure(value=1, variable=self.poison_tuning)
        self.poison_vuln_tuning.grid(column=0, row=7)
        self.thunder_vuln_radio = tk.Radiobutton(
            self.vuln_tuning_radio_frame, name="thunder_vuln_radio")
        self.thunder_vuln_radio.configure(
            value=1, variable=self.thunder_tuning)
        self.thunder_vuln_radio.grid(column=0, row=8)
        self.force_vuln_radio = tk.Radiobutton(
            self.vuln_tuning_radio_frame, name="force_vuln_radio")
        self.force_vuln_radio.configure(value=1, variable=self.force_tuning)
        self.force_vuln_radio.grid(column=0, row=9)
        self.necrotic_vuln_radio = tk.Radiobutton(
            self.vuln_tuning_radio_frame, name="necrotic_vuln_radio")
        self.necrotic_vuln_radio.configure(
            value=1, variable=self.necrotic_tuning)
        self.necrotic_vuln_radio.grid(column=0, row=10)
        self.radiant_vuln_radio = tk.Radiobutton(
            self.vuln_tuning_radio_frame, name="radiant_vuln_radio")
        self.radiant_vuln_radio.configure(
            value=1, variable=self.radiant_tuning)
        self.radiant_vuln_radio.grid(column=0, row=11)
        self.psychic_vuln_radio = tk.Radiobutton(
            self.vuln_tuning_radio_frame, name="psychic_vuln_radio")
        self.psychic_vuln_radio.configure(
            value=1, variable=self.psychic_tuning)
        self.psychic_vuln_radio.grid(column=0, row=12)
        self.vuln_tuning_radio_frame.grid(column=0, padx="5 0", row=1)
        self.vuln_tuning_frame.grid(column=1, row=0)
        self.resist_tuning_frame = ttk.Frame(
            self.vuln_resist_immune_frame,
            name="resist_tuning_frame")
        self.resist_tuning_frame.configure(height=200, width=200)
        self.resist_tuning_label = ttk.Label(
            self.resist_tuning_frame, name="resist_tuning_label")
        self.resist_tuning_label.configure(
            font="{DejaVu Sans} 8 {bold}", text='Resist')
        self.resist_tuning_label.grid(column=0, padx="10 0", row=0)
        self.resist_tuning_vuln_frame = ttk.Frame(
            self.resist_tuning_frame, name="resist_tuning_vuln_frame")
        self.resist_tuning_vuln_frame.configure(height=200, width=200)
        self.bludgeon_resist_radio = tk.Radiobutton(
            self.resist_tuning_vuln_frame, name="bludgeon_resist_radio")
        self.bludgeon_resist_radio.configure(
            value=2, variable=self.bludgeon_tuning)
        self.bludgeon_resist_radio.grid(column=0, row=0)
        self.piercing_resist_radio = tk.Radiobutton(
            self.resist_tuning_vuln_frame, name="piercing_resist_radio")
        self.piercing_resist_radio.configure(
            value=2, variable=self.piercing_tuning)
        self.piercing_resist_radio.grid(column=0, row=1)
        self.slashing_resist_radio = tk.Radiobutton(
            self.resist_tuning_vuln_frame, name="slashing_resist_radio")
        self.slashing_resist_radio.configure(
            value=2, variable=self.slashing_tuning)
        self.slashing_resist_radio.grid(column=0, row=2)
        self.acid_resist_radio = tk.Radiobutton(
            self.resist_tuning_vuln_frame, name="acid_resist_radio")
        self.acid_resist_radio.configure(value=2, variable=self.acid_tuning)
        self.acid_resist_radio.grid(column=0, row=3)
        self.cold_resist_radio = tk.Radiobutton(
            self.resist_tuning_vuln_frame, name="cold_resist_radio")
        self.cold_resist_radio.configure(value=2, variable=self.cold_tuning)
        self.cold_resist_radio.grid(column=0, row=4)
        self.fire_resist_radio = tk.Radiobutton(
            self.resist_tuning_vuln_frame, name="fire_resist_radio")
        self.fire_resist_radio.configure(value=2, variable=self.fire_tuning)
        self.fire_resist_radio.grid(column=0, row=5)
        self.lightning_resist_radio = tk.Radiobutton(
            self.resist_tuning_vuln_frame, name="lightning_resist_radio")
        self.lightning_resist_radio.configure(
            value=2, variable=self.lightining_tuning)
        self.lightning_resist_radio.grid(column=0, row=6)
        self.poison_resist_tuning = tk.Radiobutton(
            self.resist_tuning_vuln_frame, name="poison_resist_tuning")
        self.poison_resist_tuning.configure(
            value=2, variable=self.poison_tuning)
        self.poison_resist_tuning.grid(column=0, row=7)
        self.thunder_resist_radio = tk.Radiobutton(
            self.resist_tuning_vuln_frame, name="thunder_resist_radio")
        self.thunder_resist_radio.configure(
            value=2, variable=self.thunder_tuning)
        self.thunder_resist_radio.grid(column=0, row=8)
        self.force_resist_radio = tk.Radiobutton(
            self.resist_tuning_vuln_frame, name="force_resist_radio")
        self.force_resist_radio.configure(value=2, variable=self.force_tuning)
        self.force_resist_radio.grid(column=0, row=9)
        self.necrotic_resist_radio = tk.Radiobutton(
            self.resist_tuning_vuln_frame, name="necrotic_resist_radio")
        self.necrotic_resist_radio.configure(
            value=2, variable=self.necrotic_tuning)
        self.necrotic_resist_radio.grid(column=0, row=10)
        self.radiantresistn_radio = tk.Radiobutton(
            self.resist_tuning_vuln_frame, name="radiantresistn_radio")
        self.radiantresistn_radio.configure(
            value=2, variable=self.radiant_tuning)
        self.radiantresistn_radio.grid(column=0, row=11)
        self.psychic_resist_radio = tk.Radiobutton(
            self.resist_tuning_vuln_frame, name="psychic_resist_radio")
        self.psychic_resist_radio.configure(
            value=2, variable=self.psychic_tuning)
        self.psychic_resist_radio.grid(column=0, row=12)
        self.resist_tuning_vuln_frame.grid(column=0, padx="10 0", row=1)
        self.resist_tuning_frame.grid(column=2, row=0)
        self.immune_tuning_frame = ttk.Frame(
            self.vuln_resist_immune_frame,
            name="immune_tuning_frame")
        self.immune_tuning_frame.configure(height=200, width=200)
        self.immune_tuning_label = ttk.Label(
            self.immune_tuning_frame, name="immune_tuning_label")
        self.immune_tuning_label.configure(
            font="{DejaVu Sans} 8 {bold}", text='Immune')
        self.immune_tuning_label.grid(column=0, padx=10, row=0, sticky="w")
        self.immune_tuning_radio_frame = ttk.Frame(
            self.immune_tuning_frame, name="immune_tuning_radio_frame")
        self.immune_tuning_radio_frame.configure(height=200, width=200)
        self.bludgeon_immune_radio = tk.Radiobutton(
            self.immune_tuning_radio_frame, name="bludgeon_immune_radio")
        self.bludgeon_immune_radio.configure(
            justify="center",
            text='Bludgeoning',
            value=3,
            variable=self.bludgeon_tuning)
        self.bludgeon_immune_radio.grid(column=0, row=0, sticky="w")
        self.piercing_immune_radio = tk.Radiobutton(
            self.immune_tuning_radio_frame, name="piercing_immune_radio")
        self.piercing_immune_radio.configure(
            text='Piercing', value=3, variable=self.piercing_tuning)
        self.piercing_immune_radio.grid(column=0, row=1, sticky="w")
        self.slashing_immune_radio = tk.Radiobutton(
            self.immune_tuning_radio_frame, name="slashing_immune_radio")
        self.slashing_immune_radio.configure(
            text='Slashing', value=3, variable=self.slashing_tuning)
        self.slashing_immune_radio.grid(column=0, row=2, sticky="w")
        self.acid_immune_radio = tk.Radiobutton(
            self.immune_tuning_radio_frame, name="acid_immune_radio")
        self.acid_immune_radio.configure(
            text='Acid', value=3, variable=self.acid_tuning)
        self.acid_immune_radio.grid(column=0, row=3, sticky="w")
        self.cold_immune_radio = tk.Radiobutton(
            self.immune_tuning_radio_frame, name="cold_immune_radio")
        self.cold_immune_radio.configure(
            text='Cold', value=3, variable=self.cold_tuning)
        self.cold_immune_radio.grid(column=0, row=4, sticky="w")
        self.fire_immune_radio = tk.Radiobutton(
            self.immune_tuning_radio_frame, name="fire_immune_radio")
        self.fire_immune_radio.configure(
            text='Fire', value=3, variable=self.fire_tuning)
        self.fire_immune_radio.grid(column=0, row=5, sticky="w")
        self.lightning_immune_radio = tk.Radiobutton(
            self.immune_tuning_radio_frame, name="lightning_immune_radio")
        self.lightning_immune_radio.configure(
            text='Lightning', value=3, variable=self.lightining_tuning)
        self.lightning_immune_radio.grid(column=0, row=6, sticky="w")
        self.poison_immune_tuning = tk.Radiobutton(
            self.immune_tuning_radio_frame, name="poison_immune_tuning")
        self.poison_immune_tuning.configure(
            text='Poison', value=3, variable=self.poison_tuning)
        self.poison_immune_tuning.grid(column=0, row=7, sticky="w")
        self.thunder_immune_radio = tk.Radiobutton(
            self.immune_tuning_radio_frame, name="thunder_immune_radio")
        self.thunder_immune_radio.configure(
            text='Thunder', value=3, variable=self.thunder_tuning)
        self.thunder_immune_radio.grid(column=0, row=8, sticky="w")
        self.force_immune_radio = tk.Radiobutton(
            self.immune_tuning_radio_frame, name="force_immune_radio")
        self.force_immune_radio.configure(
            text='Force', value=3, variable=self.force_tuning)
        self.force_immune_radio.grid(column=0, row=9, sticky="w")
        self.necrotic_immune_radio = tk.Radiobutton(
            self.immune_tuning_radio_frame, name="necrotic_immune_radio")
        self.necrotic_immune_radio.configure(
            text='Necrotic', value=3, variable=self.necrotic_tuning)
        self.necrotic_immune_radio.grid(column=0, row=10, sticky="w")
        self.radiant_immune_radio = tk.Radiobutton(
            self.immune_tuning_radio_frame, name="radiant_immune_radio")
        self.radiant_immune_radio.configure(
            text='Radiant', value=3, variable=self.radiant_tuning)
        self.radiant_immune_radio.grid(column=0, row=11, sticky="w")
        self.psychic_immune_radio = tk.Radiobutton(
            self.immune_tuning_radio_frame, name="psychic_immune_radio")
        self.psychic_immune_radio.configure(
            text='Psychic', value=3, variable=self.psychic_tuning)
        self.psychic_immune_radio.grid(column=0, row=12, sticky="w")
        self.immune_tuning_radio_frame.grid(column=0, padx=10, row=1)
        self.immune_tuning_frame.grid(column=3, row=0)
        self.vuln_resist_immune_frame.grid(
            column=0, padx="0 5", pady=0, row=3, sticky="ns")
        self.language_frame = ttk.Labelframe(
            self.gameplay_frame, name="language_frame")
        self.language_frame.configure(height=200, text='Languages', width=200)
        self.language_std_label = tk.Label(
            self.language_frame, name="language_std_label")
        self.language_std_label.configure(
            font="{DejaVu Sans} 8 {bold}", text='Standard')
        self.language_std_label.grid(column=0, padx="20 0", row=0, sticky="w")
        self.language_common_check_box = tk.Checkbutton(
            self.language_frame, name="language_common_check_box")
        self.common_var = tk.BooleanVar()
        self.language_common_check_box.configure(
            text='Common', variable=self.common_var)
        self.language_common_check_box.grid(column=0, row=1, sticky="w")
        self.langauge_dwarvish_check_box = tk.Checkbutton(
            self.language_frame, name="langauge_dwarvish_check_box")
        self.dwarvish_var = tk.BooleanVar()
        self.langauge_dwarvish_check_box.configure(
            text='Dwarvish', variable=self.dwarvish_var)
        self.langauge_dwarvish_check_box.grid(column=0, row=2, sticky="w")
        self.language_elvish_check_box = tk.Checkbutton(
            self.language_frame, name="language_elvish_check_box")
        self.elvish_var = tk.BooleanVar()
        self.language_elvish_check_box.configure(
            text='Elvish', variable=self.elvish_var)
        self.language_elvish_check_box.grid(column=0, row=3, sticky="w")
        self.language_giant_check_box = tk.Checkbutton(
            self.language_frame, name="language_giant_check_box")
        self.giant_var = tk.BooleanVar()
        self.language_giant_check_box.configure(
            text='Giant', variable=self.giant_var)
        self.language_giant_check_box.grid(column=0, row=4, sticky="w")
        self.language_gnomish_check_box = tk.Checkbutton(
            self.language_frame, name="language_gnomish_check_box")
        self.gnomish_var = tk.BooleanVar()
        self.language_gnomish_check_box.configure(
            text='Gnomish', variable=self.gnomish_var)
        self.language_gnomish_check_box.grid(column=0, row=5, sticky="w")
        self.language_goblin_check_box = tk.Checkbutton(
            self.language_frame, name="language_goblin_check_box")
        self.goblin_var = tk.BooleanVar()
        self.language_goblin_check_box.configure(
            text='Goblin', variable=self.goblin_var)
        self.language_goblin_check_box.grid(column=0, row=6, sticky="w")
        self.language_halfling_check_box = tk.Checkbutton(
            self.language_frame, name="language_halfling_check_box")
        self.halfling_var = tk.BooleanVar()
        self.language_halfling_check_box.configure(
            text='Halfing', variable=self.halfling_var)
        self.language_halfling_check_box.grid(column=0, row=7, sticky="w")
        self.language_orc_check_box = tk.Checkbutton(
            self.language_frame, name="language_orc_check_box")
        self.orc_var = tk.BooleanVar()
        self.language_orc_check_box.configure(
            text='Orc', variable=self.orc_var)
        self.language_orc_check_box.grid(column=0, row=8, sticky="w")
        self.language_exotic_label = tk.Label(
            self.language_frame, name="language_exotic_label")
        self.language_exotic_label.configure(
            font="{DejaVu Sans} 8 {bold}", text='Exotic')
        self.language_exotic_label.grid(
            column=1, padx="25 0", row=0, sticky="w")
        self.language_abyssal_check_box = tk.Checkbutton(
            self.language_frame, name="language_abyssal_check_box")
        self.abyssal_var = tk.BooleanVar()
        self.language_abyssal_check_box.configure(
            text='Abyssal', variable=self.abyssal_var)
        self.language_abyssal_check_box.grid(column=1, row=1, sticky="w")
        self.language_celestial_check_box = tk.Checkbutton(
            self.language_frame, name="language_celestial_check_box")
        self.celestial_var = tk.BooleanVar()
        self.language_celestial_check_box.configure(
            text='Celestial', variable=self.celestial_var)
        self.language_celestial_check_box.grid(column=1, row=2, sticky="w")
        self.language_draconic_check_box = tk.Checkbutton(
            self.language_frame, name="language_draconic_check_box")
        self.draconic_var = tk.BooleanVar()
        self.language_draconic_check_box.configure(
            text='Draconic', variable=self.draconic_var)
        self.language_draconic_check_box.grid(column=1, row=3, sticky="w")
        self.language_deepspeech_check_box = tk.Checkbutton(
            self.language_frame, name="language_deepspeech_check_box")
        self.deep_speech_var = tk.BooleanVar()
        self.language_deepspeech_check_box.configure(
            text='Deep Speech', variable=self.deep_speech_var)
        self.language_deepspeech_check_box.grid(column=1, row=4, sticky="w")
        self.language_infernal_check_box = tk.Checkbutton(
            self.language_frame, name="language_infernal_check_box")
        self.infernal_var = tk.BooleanVar()
        self.language_infernal_check_box.configure(
            text='Infernal', variable=self.infernal_var)
        self.language_infernal_check_box.grid(column=1, row=5, sticky="w")
        self.language_sylvan_check_box = tk.Checkbutton(
            self.language_frame, name="language_sylvan_check_box")
        self.sylvan_var = tk.BooleanVar()
        self.language_sylvan_check_box.configure(
            text='Sylvan', variable=self.sylvan_var)
        self.language_sylvan_check_box.grid(column=1, row=6, sticky="w")
        self.language_undercommon_check_box = tk.Checkbutton(
            self.language_frame, name="language_undercommon_check_box")
        self.undercommon_var = tk.BooleanVar()
        self.language_undercommon_check_box.configure(
            text='Undercommon', variable=self.undercommon_var)
        self.language_undercommon_check_box.grid(column=1, row=7, sticky="w")
        self.language_auran_check_box = tk.Checkbutton(
            self.language_frame, name="language_auran_check_box")
        self.auran_var = tk.BooleanVar()
        self.language_auran_check_box.configure(
            text='Auran', variable=self.auran_var)
        self.language_auran_check_box.grid(column=1, row=8, sticky="w")
        self.language_terran_check_box = tk.Checkbutton(
            self.language_frame, name="language_terran_check_box")
        self.terran_var = tk.BooleanVar()
        self.language_terran_check_box.configure(
            text='Terran', variable=self.terran_var)
        self.language_terran_check_box.grid(column=1, row=9, sticky="w")
        self.language_aquan_check_box = tk.Checkbutton(
            self.language_frame, name="language_aquan_check_box")
        self.aquan_var = tk.BooleanVar()
        self.language_aquan_check_box.configure(
            text='Aquan', variable=self.aquan_var)
        self.language_aquan_check_box.grid(column=1, row=10, sticky="w")
        self.language_ignan_check_box = tk.Checkbutton(
            self.language_frame, name="language_ignan_check_box")
        self.ignan_var = tk.BooleanVar()
        self.language_ignan_check_box.configure(
            text='Ignan', variable=self.ignan_var)
        self.language_ignan_check_box.grid(column=1, row=11, sticky="w")
        self.language_secret_label = tk.Label(
            self.language_frame, name="language_secret_label")
        self.language_secret_label.configure(
            font="{DejaVu Sans} 8 {bold}", text='Secret')
        self.language_secret_label.grid(
            column=0, padx="25 0", row=14, sticky="w")
        self.language_druidic_check_box = tk.Checkbutton(
            self.language_frame, name="language_druidic_check_box")
        self.druidic_var = tk.BooleanVar()
        self.language_druidic_check_box.configure(
            text='Druidic', variable=self.druidic_var)
        self.language_druidic_check_box.grid(column=0, row=15, sticky="w")
        self.language_thievescant_check_button = tk.Checkbutton(
            self.language_frame, name="language_thievescant_check_button")
        self.thieves_cant_var = tk.BooleanVar()
        self.language_thievescant_check_button.configure(
            text="Thieve's Cant", variable=self.thieves_cant_var)
        self.language_thievescant_check_button.grid(
            column=1, row=15, sticky="w")
        self.language_frame.grid(
            column=1, ipadx=5, ipady=3, row=3, sticky="ns")
        self.skills_frame = ttk.Labelframe(
            self.gameplay_frame, name="skills_frame")
        self.skills_frame.configure(height=200, text='Skills', width=200)
        self.skill_acrobatics_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_acrobatics_check_box")
        self.acrobatics_var = tk.BooleanVar()
        self.skill_acrobatics_check_box.configure(
            offrelief="flat",
            relief="flat",
            text='Acrobatics (DEX)',
            variable=self.acrobatics_var)
        self.skill_acrobatics_check_box.grid(
            column=0, padx="11 12", row=0, sticky="w")
        self.skill_animal_handling_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_animal_handling_check_box")
        self.animal_handling_var = tk.BooleanVar()
        self.skill_animal_handling_check_box.configure(
            text='Animal Handling (WIS)', variable=self.animal_handling_var)
        self.skill_animal_handling_check_box.grid(
            column=0, padx="11 12", pady=1, row=1, sticky="w")
        self.skill_arcana_chieck_box = tk.Checkbutton(
            self.skills_frame, name="skill_arcana_chieck_box")
        self.arcana_var = tk.BooleanVar()
        self.skill_arcana_chieck_box.configure(
            text='Arcanca (INT)', variable=self.arcana_var)
        self.skill_arcana_chieck_box.grid(
            column=0, padx="11 12", row=2, sticky="w")
        self.skill_athletics_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_athletics_check_box")
        self.athletics_var = tk.BooleanVar()
        self.skill_athletics_check_box.configure(
            text='Athletics (STR)', variable=self.athletics_var)
        self.skill_athletics_check_box.grid(
            column=0, padx="11 12", pady=1, row=3, sticky="w")
        self.skill_deception_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_deception_check_box")
        self.deception_var = tk.BooleanVar()
        self.skill_deception_check_box.configure(
            text='Deception (CHA)', variable=self.deception_var)
        self.skill_deception_check_box.grid(
            column=0, padx="11 12", row=4, sticky="w")
        self.skill_history_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_history_check_box")
        self.history_var = tk.BooleanVar()
        self.skill_history_check_box.configure(
            text='History (INT)', variable=self.history_var)
        self.skill_history_check_box.grid(
            column=0, padx="11 12", pady=1, row=5, sticky="w")
        self.skill_insight_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_insight_check_box")
        self.insight_var = tk.BooleanVar()
        self.skill_insight_check_box.configure(
            text='Insight (WIS)', variable=self.insight_var)
        self.skill_insight_check_box.grid(
            column=0, padx="11 12", row=6, sticky="w")
        self.skill_intimidation_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_intimidation_check_box")
        self.intimidation_var = tk.BooleanVar()
        self.skill_intimidation_check_box.configure(
            text='Intimidation (CHA)', variable=self.intimidation_var)
        self.skill_intimidation_check_box.grid(
            column=0, padx="11 12", pady=1, row=7, sticky="w")
        self.skill_investigation_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_investigation_check_box")
        self.investigation_var = tk.BooleanVar()
        self.skill_investigation_check_box.configure(
            text='Investigation (INT)', variable=self.investigation_var)
        self.skill_investigation_check_box.grid(
            column=0, padx="11 12", row=8, sticky="w")
        self.skill_medicine_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_medicine_check_box")
        self.medicine_var = tk.BooleanVar()
        self.skill_medicine_check_box.configure(
            text='Medicine (WIS)', variable=self.medicine_var)
        self.skill_medicine_check_box.grid(
            column=0, padx="11 12", pady=1, row=9, sticky="w")
        self.skill_mechanica_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_mechanica_check_box")
        self.mechanica_var = tk.BooleanVar()
        self.skill_mechanica_check_box.configure(
            text='Mechanica (INT)', variable=self.mechanica_var)
        self.skill_mechanica_check_box.grid(
            column=0, padx="11 12", row=10, sticky="w")
        self.skill_nature_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_nature_check_box")
        self.nature_var = tk.BooleanVar()
        self.skill_nature_check_box.configure(
            text='Nature (INT)', variable=self.nature_var)
        self.skill_nature_check_box.grid(
            column=0, padx="11 12", pady=1, row=11, sticky="w")
        self.skill_perception_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_perception_check_box")
        self.perception_var = tk.BooleanVar()
        self.skill_perception_check_box.configure(
            text='Perception (WIS)', variable=self.perception_var)
        self.skill_perception_check_box.grid(
            column=0, padx="11 12", row=12, sticky="w")
        self.skill_performance_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_performance_check_box")
        self.performance_var = tk.BooleanVar()
        self.skill_performance_check_box.configure(
            text='Performance (CHA)', variable=self.performance_var)
        self.skill_performance_check_box.grid(
            column=0, padx="11 12", pady=1, row=13, sticky="w")
        self.skill_persuasion_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_persuasion_check_box")
        self.persuasion_var = tk.BooleanVar()
        self.skill_persuasion_check_box.configure(
            text='Persuasion (CHA)', variable=self.persuasion_var)
        self.skill_persuasion_check_box.grid(
            column=0, padx="11 12", row=14, sticky="w")
        self.skill_religion_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_religion_check_box")
        self.religion_var = tk.BooleanVar()
        self.skill_religion_check_box.configure(
            text='Religion (INT)', variable=self.religion_var)
        self.skill_religion_check_box.grid(
            column=0, padx="11 12", pady=1, row=15, sticky="w")
        self.skill_sleight_of_hand_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_sleight_of_hand_check_box")
        self.sleight_of_hand_var = tk.BooleanVar()
        self.skill_sleight_of_hand_check_box.configure(
            text='Sleight of Hand (DEX)', variable=self.sleight_of_hand_var)
        self.skill_sleight_of_hand_check_box.grid(
            column=0, padx="11 12", row=16, sticky="w")
        self.skill_stealth_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_stealth_check_box")
        self.stealth_var = tk.BooleanVar()
        self.skill_stealth_check_box.configure(
            text='Stealth (DEX)', variable=self.stealth_var)
        self.skill_stealth_check_box.grid(
            column=0, padx="11 12", row=18, sticky="w")
        self.skill_spiritualism_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_spiritualism_check_box")
        self.spiritualism_var = tk.BooleanVar()
        self.skill_spiritualism_check_box.configure(
            text='Spiritualism (WIS)', variable=self.spiritualism_var)
        self.skill_spiritualism_check_box.grid(
            column=0, padx="11 12", pady=1, row=17, sticky="w")
        self.skill_survival_check_box = tk.Checkbutton(
            self.skills_frame, name="skill_survival_check_box")
        self.survival_var = tk.BooleanVar()
        self.skill_survival_check_box.configure(
            text='Survival (WIS)', variable=self.survival_var)
        self.skill_survival_check_box.grid(
            column=0, padx="11 12", pady=1, row=19, sticky="w")
        self.skills_frame.grid(
            column=2,
            ipady=0,
            padx=5,
            row=1,
            rowspan=3,
            sticky="nw")
        self.weapon_tuning_frame = ttk.Labelframe(
            self.gameplay_frame, name="weapon_tuning_frame")
        self.weapon_tuning_frame.configure(
            height=200, text='Weapon Tuning', width=200)
        self.weapon_tuning_silvered_check_box = tk.Checkbutton(
            self.weapon_tuning_frame, name="weapon_tuning_silvered_check_box")
        self.silvered_var = tk.BooleanVar()
        self.weapon_tuning_silvered_check_box.configure(
            text='Silvered', variable=self.silvered_var)
        self.weapon_tuning_silvered_check_box.grid(column=1, row=0, sticky="w")
        self.weapon_tuning_adamantine_check_box = tk.Checkbutton(
            self.weapon_tuning_frame, name="weapon_tuning_adamantine_check_box")
        self.adamantine_var = tk.BooleanVar()
        self.weapon_tuning_adamantine_check_box.configure(
            text='Adamantine', variable=self.adamantine_var)
        self.weapon_tuning_adamantine_check_box.grid(
            column=0, row=0, sticky="w")
        self.weapon_tuning_mithral_check_box = tk.Checkbutton(
            self.weapon_tuning_frame, name="weapon_tuning_mithral_check_box")
        self.mithral_var = tk.BooleanVar()
        self.weapon_tuning_mithral_check_box.configure(
            text='Mithral', variable=self.mithral_var)
        self.weapon_tuning_mithral_check_box.grid(column=1, row=1, sticky="w")
        self.weapon_tuning_cold_iron_check_box = tk.Checkbutton(
            self.weapon_tuning_frame, name="weapon_tuning_cold_iron_check_box")
        self.cold_iron_var = tk.BooleanVar()
        self.weapon_tuning_cold_iron_check_box.configure(
            text='Cold Iron', variable=self.cold_iron_var)
        self.weapon_tuning_cold_iron_check_box.grid(
            column=0, row=1, sticky="w")
        self.weapon_tuning_living_wood_check_box = tk.Checkbutton(
            self.weapon_tuning_frame, name="weapon_tuning_living_wood_check_box")
        self.living_wood_var = tk.BooleanVar()
        self.weapon_tuning_living_wood_check_box.configure(
            text='Living Wood', variable=self.living_wood_var)
        self.weapon_tuning_living_wood_check_box.grid(
            column=0, row=2, sticky="w")
        self.weapon_tuning_magical_check_box = tk.Checkbutton(
            self.weapon_tuning_frame, name="weapon_tuning_magical_check_box")
        self.magical_var = tk.BooleanVar()
        self.weapon_tuning_magical_check_box.configure(
            text='Magical', variable=self.magical_var)
        self.weapon_tuning_magical_check_box.grid(column=1, row=2, sticky="w")
        self.weapon_tuning_other_check_box = tk.Checkbutton(
            self.weapon_tuning_frame, name="weapon_tuning_other_check_box")
        self.other_var = tk.BooleanVar()
        self.weapon_tuning_other_check_box.configure(
            text='Other', variable=self.other_var)
        self.weapon_tuning_other_check_box.grid(column=0, row=3, sticky="w")
        self.weapon_tuning_other_entry = tk.Entry(
            self.weapon_tuning_frame, name="weapon_tuning_other_entry")
        self.other_def_var = tk.StringVar()
        self.weapon_tuning_other_entry.configure(
            textvariable=self.other_def_var, width=22)
        self.weapon_tuning_other_entry.grid(
            column=0, columnspan=2, padx=5, pady="0 5", row=4, sticky="w")
        self.weapon_tuning_frame.grid(
            column=2, padx=5, row=2, rowspan=2, sticky="sew")
        self.senses_frame = ttk.Labelframe(
            self.gameplay_frame, name="senses_frame")
        self.senses_frame.configure(
            height=200, padding=5, text='Senses', width=200)
        self.sense_darkvision_label = ttk.Label(
            self.senses_frame, name="sense_darkvision_label")
        self.sense_darkvision_label.configure(text='Darkvision: ')
        self.sense_darkvision_label.grid(column=0, row=0, sticky="e")
        self.sense_blindsight_label = ttk.Label(
            self.senses_frame, name="sense_blindsight_label")
        self.sense_blindsight_label.configure(text='Blindsight: ')
        self.sense_blindsight_label.grid(column=0, row=1, sticky="e")
        self.sense_truesight_label = ttk.Label(
            self.senses_frame, name="sense_truesight_label")
        self.sense_truesight_label.configure(text='Truesight: ')
        self.sense_truesight_label.grid(column=0, row=2, sticky="e")
        self.sense_tremorsense_label = ttk.Label(
            self.senses_frame, name="sense_tremorsense_label")
        self.sense_tremorsense_label.configure(text='Tremorsense: ')
        self.sense_tremorsense_label.grid(column=0, row=3, sticky="e")
        self.senses_darkvision_entry = tk.Entry(
            self.senses_frame, name="senses_darkvision_entry")
        self.darkvision_var = tk.StringVar()
        self.senses_darkvision_entry.configure(
            textvariable=self.darkvision_var, width=5)
        self.senses_darkvision_entry.grid(column=1, padx=5, pady="0 5", row=0)
        self.senses_blindsight_check_box = tk.Entry(
            self.senses_frame, name="senses_blindsight_check_box")
        self.blindsight_var = tk.StringVar()
        self.senses_blindsight_check_box.configure(
            textvariable=self.blindsight_var, width=5)
        self.senses_blindsight_check_box.grid(column=1, pady="0 5", row=1)
        self.senses_truesight_entry = tk.Entry(
            self.senses_frame, name="senses_truesight_entry")
        self.truesight_var = tk.StringVar()
        self.senses_truesight_entry.configure(
            textvariable=self.truesight_var, width=5)
        self.senses_truesight_entry.grid(column=1, pady="0 5", row=2)
        self.senses_tremorsense_entry = tk.Entry(
            self.senses_frame, name="senses_tremorsense_entry")
        self.tremorsense_var = tk.StringVar()
        self.senses_tremorsense_entry.configure(
            textvariable=self.tremorsense_var, width=5)
        self.senses_tremorsense_entry.grid(column=1, pady="0 5", row=3)
        self.senses_frame.grid(column=3, row=3)
        self.condition_immunities_frame = ttk.Labelframe(
            self.gameplay_frame, name="condition_immunities_frame")
        self.condition_immunities_frame.configure(
            height=200, text='Condition Immunities', width=200)
        self.condition_immunity_blinded_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_blinded_check_box")
        self.blinded_var = tk.BooleanVar()
        self.condition_immunity_blinded_check_box.configure(
            text='Blinded', variable=self.blinded_var)
        self.condition_immunity_blinded_check_box.grid(
            column=0, row=0, sticky="w")
        self.condition_immunity_charmed_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_charmed_check_box")
        self.charmed_var = tk.BooleanVar()
        self.condition_immunity_charmed_check_box.configure(
            text='Charmed', variable=self.charmed_var)
        self.condition_immunity_charmed_check_box.grid(
            column=0, pady=2, row=1, sticky="w")
        self.condition_immunity_deafened_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_deafened_check_box")
        self.deafened_var = tk.BooleanVar()
        self.condition_immunity_deafened_check_box.configure(
            text='Deafened', variable=self.deafened_var)
        self.condition_immunity_deafened_check_box.grid(
            column=0, row=2, sticky="w")
        self.condition_immunity_frightened_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_frightened_check_box")
        self.frightened_var = tk.BooleanVar()
        self.condition_immunity_frightened_check_box.configure(
            text='Frightened', variable=self.frightened_var)
        self.condition_immunity_frightened_check_box.grid(
            column=0, pady=2, row=3, sticky="w")
        self.condition_immunity_grappled_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_grappled_check_box")
        self.grappled_var = tk.BooleanVar()
        self.condition_immunity_grappled_check_box.configure(
            text='Grappled', variable=self.grappled_var)
        self.condition_immunity_grappled_check_box.grid(
            column=0, row=4, sticky="w")
        self.condition_immunity_incapacitated_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_incapacitated_check_box")
        self.incapacitated_var = tk.BooleanVar()
        self.condition_immunity_incapacitated_check_box.configure(
            text='Incapacitated', variable=self.incapacitated_var)
        self.condition_immunity_incapacitated_check_box.grid(
            column=0, pady=2, row=5, sticky="w")
        self.condition_immunity_paralyzed_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_paralyzed_check_box")
        self.paralyzed_var = tk.BooleanVar()
        self.condition_immunity_paralyzed_check_box.configure(
            text='Paralyzed', variable=self.paralyzed_var)
        self.condition_immunity_paralyzed_check_box.grid(
            column=0, row=6, sticky="w")
        self.condition_immunity_petrified_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_petrified_check_box")
        self.petrified_var = tk.BooleanVar()
        self.condition_immunity_petrified_check_box.configure(
            text='Petrified', variable=self.petrified_var)
        self.condition_immunity_petrified_check_box.grid(
            column=0, pady=2, row=7, sticky="w")
        self.condition_immunity_poisoned_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_poisoned_check_box")
        self.poison_var = tk.BooleanVar()
        self.condition_immunity_poisoned_check_box.configure(
            text='Poison', variable=self.poison_var)
        self.condition_immunity_poisoned_check_box.grid(
            column=0, row=8, sticky="w")
        self.condition_immunity_prone_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_prone_check_box")
        self.prone_var = tk.BooleanVar()
        self.condition_immunity_prone_check_box.configure(
            text='Prone', variable=self.prone_var)
        self.condition_immunity_prone_check_box.grid(
            column=0, pady=2, row=9, sticky="w")
        self.condition_immunity_restrained_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_restrained_check_box")
        self.restrained_var = tk.BooleanVar()
        self.condition_immunity_restrained_check_box.configure(
            text='Restrained', variable=self.restrained_var)
        self.condition_immunity_restrained_check_box.grid(
            column=0, row=10, sticky="w")
        self.condition_immunity_stunned_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_stunned_check_box")
        self.stunned_var = tk.BooleanVar()
        self.condition_immunity_stunned_check_box.configure(
            text='Stunned', variable=self.stunned_var)
        self.condition_immunity_stunned_check_box.grid(
            column=0, pady=2, row=11, sticky="w")
        self.condition_immunity_unconscious_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_unconscious_check_box")
        self.unconcious_var = tk.BooleanVar()
        self.condition_immunity_unconscious_check_box.configure(
            text='Unconscious', variable=self.unconcious_var)
        self.condition_immunity_unconscious_check_box.grid(
            column=0, row=12, sticky="w")
        self.condition_immunity_bleeding_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_bleeding_check_box")
        self.bleeding_var = tk.BooleanVar()
        self.condition_immunity_bleeding_check_box.configure(
            text='Bleeding', variable=self.bleeding_var)
        self.condition_immunity_bleeding_check_box.grid(
            column=0, pady=2, row=13, sticky="w")
        self.condition_immunity_confused_check_box = tk.Checkbutton(
            self.condition_immunities_frame, name="condition_immunity_confused_check_box")
        self.confused_var = tk.BooleanVar()
        self.condition_immunity_confused_check_box.configure(
            text='Confused', variable=self.confused_var)
        self.condition_immunity_confused_check_box.grid(
            column=0, row=14, sticky="w")
        self.condition_immunities_frame.grid(
            column=3, ipady=2, row=1, rowspan=3, sticky="n")
        self.abilities_and_actions_frame = ttk.Labelframe(
            self.gameplay_frame, name="abilities_and_actions_frame")
        self.abilities_and_actions_frame.configure(
            height=200, padding=5, text='Abilities & Actions', width=200)
        self.abilities_label = ttk.Label(
            self.abilities_and_actions_frame,
            name="abilities_label")
        self.abilities_label.configure(text='Abilities:')
        self.abilities_label.grid(column=0, pady=5, row=0, sticky="w")
        self.abilities_entry = tk.Text(
            self.abilities_and_actions_frame,
            name="abilities_entry")
        self.abilities_entry.configure(
            height=8, undo=True, width=35, wrap="word")
        self.abilities_entry.grid(column=0, padx="0 5", row=1, sticky="w")
        self.actions_label = ttk.Label(
            self.abilities_and_actions_frame,
            name="actions_label")
        self.actions_label.configure(text='Actions:')
        self.actions_label.grid(column=0, pady=5, row=2, sticky="w")
        self.actions_entry = tk.Text(
            self.abilities_and_actions_frame,
            name="actions_entry")
        self.actions_entry.configure(
            height=8,
            insertunfocussed="none",
            tabstyle="tabular",
            takefocus=True,
            width=35,
            wrap="word")
        self.actions_entry.grid(column=0, padx="0 5", row=3, sticky="w")
        self.bonus_actions_label = ttk.Label(
            self.abilities_and_actions_frame,
            name="bonus_actions_label")
        self.bonus_actions_label.configure(text='Bonus Actions:')
        self.bonus_actions_label.grid(
            column=0, pady=5, row=4, sticky="w")
        self.bonus_actions_entry = tk.Text(
            self.abilities_and_actions_frame,
            name="bonus_actions_entry")
        self.bonus_actions_entry.configure(height=8, width=35, wrap="word")
        self.bonus_actions_entry.grid(
            column=0, padx="0 5", pady="0 10", row=5, sticky="w")
        self.reactions_label = ttk.Label(
            self.abilities_and_actions_frame,
            name="reactions_label")
        self.reactions_label.configure(text='Reactions:')
        self.reactions_label.grid(column=1, pady=5, row=0, sticky="w")
        self.reactions_entry = tk.Text(
            self.abilities_and_actions_frame,
            name="reactions_entry")
        self.reactions_entry.configure(height=8, width=35, wrap="word")
        self.reactions_entry.grid(column=1, row=1)
        self.legendary_actions_label = ttk.Label(
            self.abilities_and_actions_frame,
            name="legendary_actions_label")
        self.legendary_actions_label.configure(text='Legendary Actions:')
        self.legendary_actions_label.grid(column=1, row=2, sticky="w")
        self.legendary_actions_entry = tk.Text(
            self.abilities_and_actions_frame,
            name="legendary_actions_entry")
        self.legendary_actions_entry.configure(height=8, width=35, wrap="word")
        self.legendary_actions_entry.grid(column=1, row=3, sticky="w")
        self.mythic_actions_label = ttk.Label(
            self.abilities_and_actions_frame,
            name="mythic_actions_label")
        self.mythic_actions_label.configure(text='Mythic Actions:')
        self.mythic_actions_label.grid(column=1, row=4, sticky="w")
        self.mythic_actions_entry = tk.Text(
            self.abilities_and_actions_frame,
            name="mythic_actions_entry")
        self.mythic_actions_entry.configure(height=8, width=35, wrap="word")
        self.mythic_actions_entry.grid(
            column=1, pady="0 10", row=5, sticky="w")
        self.abilities_scrollbar = ttk.Scrollbar(
            self.abilities_and_actions_frame,
            name="abilities_scrollbar")
        self.abilities_scrollbar.configure(orient="vertical")
        self.abilities_scrollbar.grid(
            column=0, padx="0 5", row=1, sticky="nse")
        self.actions_scrollbar = ttk.Scrollbar(
            self.abilities_and_actions_frame,
            name="actions_scrollbar")
        self.actions_scrollbar.configure(orient="vertical")
        self.actions_scrollbar.grid(column=0, padx="0 5", row=3, sticky="nse")
        self.bonus_actions_scrollbar = ttk.Scrollbar(
            self.abilities_and_actions_frame, name="bonus_actions_scrollbar")
        self.bonus_actions_scrollbar.configure(orient="vertical")
        self.bonus_actions_scrollbar.grid(
            column=0, padx="0 5", pady="0 10", row=5, sticky="nse")
        self.reactions_scrollbar = ttk.Scrollbar(
            self.abilities_and_actions_frame,
            name="reactions_scrollbar")
        self.reactions_scrollbar.configure(orient="vertical")
        self.reactions_scrollbar.grid(column=1, row=1, sticky="nse")
        self.legendary_actions_scrollbar = ttk.Scrollbar(
            self.abilities_and_actions_frame, name="legendary_actions_scrollbar")
        self.legendary_actions_scrollbar.configure(orient="vertical")
        self.legendary_actions_scrollbar.grid(column=1, row=3, sticky="nse")
        self.mythic_actions_scrollbar = ttk.Scrollbar(
            self.abilities_and_actions_frame, name="mythic_actions_scrollbar")
        self.mythic_actions_scrollbar.configure(orient="vertical")
        self.mythic_actions_scrollbar.grid(
            column=1, pady="0 10", row=5, sticky="nse")
        self.abilities_and_actions_frame.grid(
            column=4, padx="5", pady=0, row=2, rowspan=2, sticky="sew")
        self.description_frame = ttk.Frame(
            self.gameplay_frame, name="description_frame")
        self.description_frame.configure(height=200, width=200)
        self.description_label = ttk.Label(
            self.description_frame, name="description_label")
        self.description_label.configure(text='Description:')
        self.description_label.grid(column=0, pady="0 10", row=0, sticky="w")
        self.description_entry = tk.Text(
            self.description_frame, name="description_entry")
        self.description_entry.configure(
            height=8, setgrid=False, width=71, wrap="word")
        self.description_entry.grid(column=0, padx=5, row=1)
        self.description_scrollbar = ttk.Scrollbar(
            self.description_frame, name="description_scrollbar")
        self.description_scrollbar.configure(orient="vertical")
        self.description_scrollbar.grid(column=0, row=1, sticky="nse")
        self.description_frame.grid(column=4, padx="5", row=1, sticky="nsw")
        self.button__frame = ttk.Frame(
            self.gameplay_frame, name="button__frame")
        self.button__frame.configure(height=200, width=200)
        self.generate_button = ttk.Button(
            self.button__frame, name="generate_button")
        self.generate_button.configure(text='Generate Creature', width=18)
        self.generate_button.grid(column=0, row=3)
        self.save_button = ttk.Button(self.button__frame, name="save_button")
        self.save_button.configure(text='Save Creature', width=18)
        self.save_button.grid(column=0, pady=10, row=4)
        self.load_button = ttk.Button(self.button__frame, name="load_button")
        self.load_button.configure(text='Load Creature', width=18)
        self.load_button.grid(column=0, row=5)
        self.logo_label = ttk.Label(self.button__frame, name="logo_label")
        self.logo_label.grid(column=0, row=0)
        self.button__frame.grid(column=3, row=3, sticky="s")
        self.gameplay_frame.grid(column=5, padx=5, row=5)
        self.monster_window.columnconfigure(5, minsize=200)

        # Main widget
        self.mainwindow = self.monster_window

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = testUI()
    app.run()
