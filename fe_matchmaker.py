# Public: Program for match-making Fire Emblem characters.
#
# 
# Returns a list of matched characters.

########################################################################

import copy
import logging
import os
from sys import platform as _platform

from help import *

########################################################################

# CONFIGURING LOG

LOG_FILENAME = 'fe_matchmaker_log.out'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG
                    )
logging.info('\n Program Begins \n')

########################################################################

# DECLARING VARIABLES

title = 'Fire Emblem Matchmaker\n\n'
options = 'Fates Conquest [C] | Birthright [B] | Relevations [R] or Awakening [A]'
menu_text = title + options

# DEFAULTS
results = '\n  Anarchy\n'
engaged = {}
parent_prefs = {}
partner_prefs = {}
default_file = 'matchmaker_results'
no_load_msg = 'What have you done???\n:O'

run_program = True

########################################################################

# MAIN FUNCTIONS
    
def matchmaker(players_fiance):
    ''' Matches characters using the Gale-Shapley algorithm.

    parent - Character proposing - a sorted list of keys.
    partner - Character evaluating proposals - a sorted list of keys.
    engaged - Dictionary of match-mated characters.

    Returns engaged with all parent characters matched.
    
    '''
    parentfree = parent[:]
    engaged  = {}
    parent_prefs_list = copy.deepcopy(parent_prefs)
    partner_prefs_list = copy.deepcopy(partner_prefs)
    
    # Makes sure the player's fiance is taken off the field
    if players_fiance:
        engaged[players_fiance] = 'Player'
        logging.info('  %s marries the player\'s unit.' %(players_fiance))
        
    while parentfree:
        parent_unit = parentfree.pop(0)
        parent_list = parent_prefs_list[parent_unit]
        partner_unit = parent_list.pop(0)
        fiance = engaged.get(partner_unit)
        
        logging.info('  %s is single and looking...' % (parent_unit))

        # Proposed to character is free
        if not fiance:
            engaged[partner_unit] = parent_unit
            logging.info("  %s and %s" % (parent_unit, partner_unit))
        
        else:
            # Proposing to an engaged character
            partnerlist = partner_prefs_list[partner_unit]
            try: 
                if partnerlist.index(fiance) > partnerlist.index(parent_unit):
                    # Another proposer is prefered
                    engaged[partner_unit] = parent_unit
                    logging.info("  %s ditched %s for %s" % (partner_unit, fiance, parent_unit))
                    
                    if parent_prefs_list[fiance]:
                        # Ex-fiance has more choices to ask
                        parentfree.append(fiance)
                        
                else:
                # The unit proposed to stays with fiancee
                    logging.debug(' %s is rejected by %s.' % (parent_unit, partner_unit))

                    if parent_list:
                        # Proposer has more choices to ask...
                        logging.debug(' ...but %s has more options.' % (parent_unit))
                        parentfree.append(parent_unit)
                        
            except ValueError:
                logging.debug(" No match possible for %s" % (parent_unit))
                
    return engaged
    
    
def save_file(user_input, player_fiance):
    '''Creates save file for matchmaker results.
    
    new_file_name - Textified file name provided by user.
    results - Dictionary of paired matches.
    
    '''
    new_file_name = textify(user_input)
    
    save_file = open(new_file_name, "w")
    save_file.write('Fire Emblem Matchmaker Results:\n\n')
    save_file.write(str(results))
    save_file.write('\n\nPlayer\'s unit is engaged to %s' % player_fiance)
    save_file.close()


def display_results():
    ''' Displays humanized results of matchmaker
    
    '''
    if not all_loaded():
        print(no_load_msg)
        
    else:
        print('\nMatches:')
        print(results)    
    
    
def open_help():
    ''' Open help information ***Not fully written up yet***
    
    '''
    clear_screen()
    print(help_file)


########################################################################

# HELPER FUNCTIONS
    
def handle_input(user_input):
    ''' Makes logical assumptions to cover for user input errors
    
    '''
    if user_input:
        return (user_input[0].capitalize())
    else:
        logging.debug(' Invalid player input')
        return "E"

    
def all_loaded():
    ''' Checks if character preference lists are properly loaded
    
    '''
    if parent_prefs and partner_prefs:
        return True

    
def valid_choice(choice):
    ''' Checks if user has entered a valid option or not
    
    '''
    if choice in 'ABCR':
        return True
    else:
        return False

    
def textify(user_input):
    ''' Adds .txt to user-inputed file name
    
    '''
    return str(user_input) + '.txt'


def clear_screen():
    ''' Clears terminal screen
    
    '''
    # Checks for Windows
    if _platform == "win32":
        clear = lambda : os.system('cls')
        
    # Otherwise for Mac/Linux
    else:
        clear = lambda : os.system('clear')
    clear()
    
        
########################################################################

# MAIN MENU

while run_program == True:
    clear_screen()
    print(menu_text.center(50))
    

########################################################################

# BRANCHING

    choice = handle_input(raw_input(' '))

    # Loads character preferences unless files are missing
    try:
        if choice == 'H':
            open_help()
        if choice == 'A':
            from awakening_list import *
        elif choice == 'B':
            from birthright_list import *
        elif choice == 'C':
            from conquest_list import *
        elif choice == 'R':
            from relevations_list import *
        else:
            logging.debug(' Do I ever run?')
        
        # Character preferences    
        parent = sorted(parent_prefs.keys())
        partner = sorted(partner_prefs.keys())
        

########################################################################

# MATCHMAKING

        # Account for player unit's choice
        if valid_choice(choice):
            players_fiance = raw_input('\nPlayer unit is engaged to: ')
            
            if players_fiance:
                logging.info('  Player is engaged to %s' % players_fiance)
                
                # Taking the player's fiance off the field if a parent unit
                if players_fiance in parent:
                    logging.info('  %s accepts the player\'s unit' %(players_fiance))
                    parent.pop(parent.index(players_fiance))
                    
            # Performs the matchmaking
            engaged = matchmaker(players_fiance)
        
        else:
            logging.error(' Player entered invalid option.')
         
         
        #Humanizing results 
        results = ('  ' + '\n  '.join('%s is engaged to %s' % couple
                            for couple in sorted(engaged.items()))) 
        display_results()
    
    
    #[branch]_list.py file(s) can't be located
    except ImportError:
    
        logging.error(' Character preference list is not in directory.')
        print('\nImport Error. Please check to make sure that all \'branch\' lists are in the same directory as the main program file.')
  
########################################################################

    # FINISHING UP

    print('\nPress [R] to Reload or [S] to Save results as a text file.')
    save = handle_input(raw_input('\nPress [E] to end program.'))

    # SAVING RESULTS
    if save == 'S':
        new_file = raw_input('\nPlease enter new file name: \n')
        if not new_file:
            new_file = default_file
        save_file(new_file, players_fiance)
        
        run_program = False
    
    # RELOADING PROGRAM        
    elif save == 'R':
        logging.info('  Program reloaded by player.\n')
        engaged = {}
        clear_screen()
    
    # ENDING PROGRAM    
    else:
        run_program = False

logging.info('\n\n  End Results: \n%s\n' %(results))

########################################################################

    # WRITING LOG
    
new_log = open(LOG_FILENAME, 'rt')
try:
    body = new_log.read()
finally:
    new_log.close()
