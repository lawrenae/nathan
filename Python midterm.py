#choices for classes and races

Race_Choices = ['Human', 'Half-Elf', 'Elf', 'Dwarf', 'Half-Orc', 'Halfing', 'Tiefling', 'Dragonborn', 'Gnome']
Class_Choices = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']


Race_Choices.sort(key=len)
Class_Choices.sort(key=len)

firstname = input('Please enter the first name of your character. ')
lastnmae = input('Please enter the last name of your character. ')
print()

print("|Select a Race.")
for race in Race_Choices:
	print()
	print(race)

Race = input("Enter a Race name. ")
print("You have selected", Race)
print()

print("|Select a Class.")
for klass in Class_Choices:
	print()
	print(klass)

Klass = input('Enter a Class name. ')
print("you have selected", Klass)


def get_roll(current):
    roll = int(input("Enter the numbers for your %s dice roll. " % current))
    if roll > 24:
        print("Number can't be higher than 24.")

    return roll


def rolling_stats():
	roll_1 = get_roll("1st")
	roll_2 = get_roll("2nd")
	roll_3 = get_roll("3rd")
	roll_4 = get_roll("4th")
	roll_5 = get_roll("5th")
	roll_6 = get_roll("6th")
        
	return print('Your highest roll is ', max(roll_1, roll_2, roll_3, roll_4, roll_5, roll_6))
	
	
print()
print("ROLL FOR STRENGTH:")
print(18 * "-")
print(rolling_stats())


print()
print("ROLL FOR DEXTERITY:")
print(20 * "-")
rolling_stats()

print()
print("ROLL FOR CONSTITUTION:")
print(25 * "-")
rolling_stats()

print()
print("ROLL FOR INTELLIGENCE")
print(25 * "-")
rolling_stats()

print()
print("ROLL FOR WISDOM:")
print(15 * "-")
rolling_stats()

print()
print("ROLL FOR CHARISMA:")
print(20 * "-")
rolling_stats()

