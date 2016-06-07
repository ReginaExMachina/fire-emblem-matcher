# Public: Program for match-making Fire Emblem characters.
#
# Returns a list of matched characters.


########################################################################

import copy
import logging, sys

########################################################################

# INITIALIZE THE CHARACTERS' DATA

parent_prefs = {
    'laslow': ['femui', 'azura', 'peri', 'camilla', 'luna', 'felicia'],
    'keaton': ['camilla', 'effie', 'hana'],
    'xander': ['femui', 'charlotte', 'hinoka', 'luna', 'sakura'],
    'leo' :['felicia', 'hinoka', 'sakura'],
    'tsubaki': ['femui', 'luna', 'hinoka', 'azura', 'felicia', 'hana', 'oboro'],
    'nishiki': ['femui', 'azura', 'sakura', 'hana', 'mozu'],
    'jakob': ['femui', 'azura', 'sakura', 'nyx'],
    'niles': ['camilla', 'mozu'],
    'odin': ['elise', 'nyx', 'orochi'],
    'silas': ['luna', 'effie', 'hinoka'],
    'kaze': ['mozu', 'beruka', 'rinkah'],
    'benny': ['peri', 'charlotte', 'camilla'],
    'arthur': ['effie', 'beruka', 'camilla', 'nyx'],
    'ryoma': ['kagero', 'orochi', 'camilla'],
    'takumi': ['azura', 'felicia', 'elise'],
    'saizo': ['orochi', 'beruka', 'mozu'],
    'hinata': ['hana', 'hinoka', 'setsuna'],
    'azama': ['effie', 'felicia', 'setsuna', 'beruka'],
    'hayato': ['nyx', 'sakura', 'oboro']
}

partner_prefs = {
    'azura': ['mamui', 'laslow', 'jakob', 'nishiki', 'takumi'],
    'femui': ['laslow', 'tsubaki', 'xander', 'jakob', 'nishiki', 'shigure', 'leo'],
    'camilla': ['keaton', 'niles', 'jakob'],
    'elise': ['odin', 'takumi', 'laslow'],
    'felicia': ['leo', 'takumi', 'jakob', 'azama'],
    'luna': ['tsubaki', 'silas', 'laslow', 'niles', 'xander'],
    'hinoka': ['leo', 'xander', 'hinata', 'silas'],
    'sakura': ['xander', 'jakob', 'leo', 'hayato', 'nishiki'],
    'effie': ['keaton', 'silas', 'arthur'],
    'beruka': ['saizo', 'azama', 'niles', 'arthur'],
    'kagero': ['ryoma', 'saizo', 'jakob'],
    'peri': ['laslow', 'benny', 'xander'],
    'hana': ['ryoma', 'keaton', 'hinata', 'tsubaki'],
    'oboro': ['takumi', 'tsubaki', 'hayato'],
    'setsuna': ['hinata', 'jakob', 'azama'],
    'rinkah': ['silas', 'kaze', 'nishiki', 'ryoma'],
    'charlotte': ['xander', 'jakob', 'keaton', 'laslow'],
    'mozu': ['nishiki', 'niles', 'kaze'],
    'orochi': ['saizo', 'ryoma', 'silas', 'jakob'],
    'nyx': ['hayato', 'niles', 'odin']
    }

# This part is where the data can be seperated based on games 
parent = sorted(parent_prefs.keys())
partner = sorted(partner_prefs.keys())


########################################################################

# MATCH MAKING FUNCTION

def matchmaker():
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
                logging.debug("Matching...")
    return engaged

########################################################################

# PROGRAM START MENU

print('Fire Emblem Match Maker')

# PERFORMS THE MATCH-MAKING
engaged = matchmaker()

# PRINT OUT RESULTS 
print('\nCouples:')
print('  ' + '\n  '.join('%s is engaged to %s' % couple
                          for couple in sorted(engaged.items())))
# EXIT
end_program = raw_input('\nPress any key to end program.')