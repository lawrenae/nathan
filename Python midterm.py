def pick_one(title, choices):
    print("|Select a %s." % title)
    for choice in choices:
        print()
        print(choice)

    choice = input("Enter a %s name. " % title)
    print("You have selected", choice)
    print()
    return choice

def get_roll(current):
    return int(input("Enter the numbers for your %s dice roll. " % current))


def rolling_stats():
    too_big = 24 #dont like magic numbers
    max_role = too_big

    while (max_role >= too_big):
        roll_1 = get_roll("1st")
        roll_2 = get_roll("2nd")
        roll_3 = get_roll("3rd")
        roll_4 = get_roll("4th")
        roll_5 = get_roll("5th")
        roll_6 = get_roll("6th")
        
        max_role = max(roll_1, roll_2, roll_3, roll_4, roll_5, roll_6)

        if max_role > too_big:
            print("No rolls can be higher than %i." % too_big)
            print("Retrying...")

    return max_role
	
def roll_section(title):
    print()
    print("ROLL FOR %s:" % title)
    print('-' * len(title))
    print("Your highest roll is %d " % rolling_stats())


firstname = input('Please enter the first name of your character. ')
lastnmae = input('Please enter the last name of your character. ')
print()

#choices for classes and races
Race_Choices = sorted(['Human', 'Half-Elf', 'Elf', 'Dwarf', 'Half-Orc', 'Halfing', 'Tiefling', 'Dragonborn', 'Gnome'], key=len)
Class_Choices = sorted(['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard'], key=len)
pick_one("Race", Race_Choices)
pick_one("Class", Class_Choices)

	
roll_section("STRENGTH")
roll_section("DEXTERITY")
roll_section("CONSTITUTION")
roll_section("INTELLIGENCE")
roll_section("WISDOM")
roll_section("CHARISMA")
