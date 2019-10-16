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



def rolling_stats():
	roll_1 = int(input("Enter the numbers for your 1st dice roll. "))
	if roll_1 > 24:
		print("Number can't be higher than 24.")
	roll_2 = int(input("Enter the numbers for your 2nd dice roll. "))
	if roll_2 > 24:
		print("Number can't be higher than 24.")
	roll_3 = int(input("Enter the numbers for your 3rd dice roll. "))
	if roll_3 > 24:
		print("Number can't be higher than 24.")
	roll_4 = int(input("Enter the numbers for your 4th dice roll. "))
	if roll_4 > 24:
		print("Number can't be higher than 24.")
	roll_5 = int(input("Enter the numbers for your 5th dice roll. "))
	if roll_5 > 24:
		print("Number can't be higher than 24.")
	roll_6 = int(input("Enter the numbers for your 6th dice roll. "))
	if roll_6 > 24:
		print("Number can't be higher than 24.")
	else:
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

