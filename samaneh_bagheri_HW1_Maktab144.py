guild = {
"warriors": {
"Arman": {"level": 12, "hp": 340, "inventory": ["sword", "shield", "potion"]},
"Sara": {"level": 15, "hp": 410, "inventory": ["axe", "potion", "potion"]},
},
"mages": {
"Reza": {"level": 10, "hp": 220, "inventory": ["staff", "scroll", "potion"]},
},
}
for class_name,players in guild.items():
    print(class_name)
    for player_name,info in players.items():
        print(player_name, info["level"])

potion_count = 0
for players in guild.values():
    for info in players.values():
        potion_count += info["inventory"].count("potion")

print("Total potions:", potion_count)


highest_hp = -1
highest_player = None
highest_class = None

for class_name, players in guild.items():
    for player_name, info in players.items():
        if info["hp"] > highest_hp:
            highest_hp = info["hp"]
            highest_player = player_name
            highest_class = class_name
print('Highest HP', highest_player,highest_class)

guild['mages']['Niki'] = {'level':8,'hp':150,'inventory':['staff}']}
print(guild)
for data in guild['warriors'].values():
    data['level']+=1