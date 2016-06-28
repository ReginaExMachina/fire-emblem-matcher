# Public: Program for match-making Fire Emblem characters.
#
# Returns a list of matched characters.

########################################################################

import copy
import logging, sys

########################################################################

# MATCH MAKING FUNCTION

def matchmaker():
    ''' Matches characters using the Gale-Shapley algorithm.

    parent - Character proposing.
    partner - Character evaluating proposals.
    engaged - Dictionary of match-mated characters.

    Returns engaged with all parent characters matched. 
    '''
    parentfree = parent[:]
    engaged  = {}
    parent_prefs_list = copy.deepcopy(parent_prefs)
    partner_prefs_list = copy.deepcopy(partner_prefs)
    while parentfree:
        parent_unit = parentfree.pop(0)
        parent_list = parent_prefs_list[parent_unit]
        partner_unit = parent_list.pop(0)
        fiance = engaged.get(partner_unit)
        if not fiance:
            # Proposed to character is free
            engaged[partner_unit] = parent_unit
            logging.debug("  %s and %s" % (parent_unit, partner_unit))
        else:
            # Proposing to an engaged character
            partnerlist = partner_prefs_list[partner_unit]
            
            try: 
                if partnerlist.index(fiance) > partnerlist.index(parent_unit):
                    # Another proposer is prefered
                    engaged[partner_unit] = parent_unit
                    logging.debug("  %s dumped %s for %s" % (partner_unit, fiance, parent_unit))
                    
                    if parent_prefs_list[fiance]:
                        # Ex-fiance has more choices to ask
                        parentfree.append(fiance)
                        
                else:
                # The unit proposed to stays with fiancee
                    if parent_list:
                        # Proposer has more choices to ask...
                        parentfree.append(parent_unit)
            except ValueError:
                logging.debug("No match possible...")
    return engaged

########################################################################

# MAIN MENU

title = 'Fire Emblem Matchmaker\n\n'
options = 'Fates Conquest [C] | Birthright [B] | Relevations [R] or Awakening [A]'
menu_text = title + options

print(menu_text.center(50))

########################################################################

# BRANCHING

choice = raw_input(' ')
if choice == 'A':
    from awakening_list import *
elif choice == 'B':
    from birthright_list import *
elif choice == 'C':
    from conquest_list import *
elif choice == 'R':
    from relevations_list import *
else:
    logging.debug("Invalid user input.")
    print("N/A")

parent = sorted(parent_prefs.keys())
partner = sorted(partner_prefs.keys())


########################################################################

# PERFORMS THE MATCH-MAKING

engaged = matchmaker()

########################################################################

# DISPLAYS RESULTS 

print('\nMatches:')
print('  ' + '\n  '.join('%s is engaged to %s' % couple
                          for couple in sorted(engaged.items())))
 
 
########################################################################

# EXIT
end_program = raw_input('\nPress any key to end program.')
