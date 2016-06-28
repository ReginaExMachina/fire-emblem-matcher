#Public: Imports the appropriate dictionary for matching.
#
#
# EXAMPLE:
#
#
# 

########################################################################

choice = raw_input('...')
if choice == 'a':
    from awakening_list import *
elif choice == 'b':
    from birthright_list import *
elif choice == 'c':
    from conquest_list import *
elif choice == 'r':
    from relevations_list import *
else:        
    print('NA') 
