def branching()
  #Test, need input/error handling
	choice = raw_input('Which game?')
	if choice == 'a':
		from awakening import *
	elif choice == 'b':
		from birthright import *
	elif choice == 'c':
		from conquest import *
	elif choice == 'r':
		from relevations import *
	else:
		print('NA') 

title = 'Fire Emblem Matchmaker\n\n'
options = 'Fates Conquest [C] | Birthright [B] | Relevations [R] or Awakening [A]'

menu_text = title + options

print(menu_text.center(800))

#branching()
#printout_results()
