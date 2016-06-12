#Public: Prints out 
#
#
#
# EXAMPLE:
# Azura is engaged to Laslow
# Beruka is engaged to Kaze
# Camilla is engaged to Keaton
# Charlotte is engaged to Xander
# ...
#
# Prints out alphabetized list of paired couples.


########################################################################


def print_results():
	
	print('\nMatched Pairs:\n')
	print('  ' + '\n  '.join('%s is engaged to %s' % couple
                          for couple in sorted(engaged.items())))
