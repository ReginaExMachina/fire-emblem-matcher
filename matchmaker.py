#Public: Matchmaking function for Fire Emblem characters.
#
# parent: Unit associated with the child unit, not including exceptional characters like Azura, Chrom or the player's unit.
# partner: Pairable unit.
# engaged: Dictionary of engaged pairs.
#
# EXAMPLE:
# {'orochi': 'saizo', 'nyx': 'hayato', 'felicia': 'leo'...}
# ...
#
# Returns a dictionary of matched pairs.

########################################################################


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
                    logging.debug("  %s released %s for %s" % (partner_unit, fiance, parent_unit))
                    
                    if parent_prefs_list[fiance]:
                        # Ex-fiance has more choices to ask
                        parentfree.append(fiance)
                        
                else:
                # The unit proposed to stays with fiancee
                    if parent_list:
                        # Proposer has more choices to ask...
                        parentfree.append(parent_unit)
            except ValueError:
                logging.debug("No match possible.")
    return engaged


    # PERFORMS THE MATCH-MAKING
#engaged = matchmaker()
