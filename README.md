# fire-emblem-matchmaker
Optimizing character pairings.

###Contents
   <ul>
    <li><a href ="https://github.com/ReginaExMachina/fire-emblem-matcher/blob/master/README.md#description">Description</a></li>
    <li><a href = "https://github.com/ReginaExMachina/fire-emblem-matcher/blob/master/README.md#getting-started">Getting Started</a></li>
    <li><a href = "https://github.com/ReginaExMachina/fire-emblem-matcher/blob/master/README.md#galeshapley-algorithm">Gale-Shapley algorithm</a></li>
    <li><a href = "https://github.com/ReginaExMachina/fire-emblem-matcher/blob/master/README.md#authour">Author</a></li>
    <li><a href = "https://github.com/ReginaExMachina/fire-emblem-matcher/blob/master/README.md#issues">Isssues</a></li>
    <li><a href = "https://github.com/ReginaExMachina/fire-emblem-matcher/blob/master/README.md#license">License</a></li>
    <li><a href = "https://github.com/ReginaExMachina/fire-emblem-matcher/blob/master/README.md#acknowledgements">Acknowledgements</a></li>
   </ul>

###Description

Matching Fire Emblem characters can be complicated. It doesn't get any easier if you care about good supports AND making the best possible child unit for combat.

This program is designed to help players out.

##Getting Started

TBA.

###Gale–Shapley algorithm

<code>fire-emblem-matchmaker</code> uses the Gale-Shapley algorithm to make matches.

With this algorithm the 'men' (or the group of proposers) typically end up with matches higher up in their preference list than the 'women' (aka the group evaluating proposals.).

That means we can prioritize the child-bearing units (so to speak) ensuring that they get the best possible matches. Thus in Awakening the proposer group is the female characters, but in Fates it's the males.

For more info check out the <a href = "https://en.wikipedia.org/wiki/Stable_marriage_problem">Wiki</a>.

###Issues

**Major Issue** 07/06/16 Recording no match possible for some characters despite having free options available. Issue compounded when player picks a partner unit as a fiance. Currently looking into different algorithm options to resolve this issue...

* Conquest branch appears to be completely unaffected by this glitch, so long as the player picks a male or 'Kamui-sexual' as their fiance.

###Author

  <ul>
    <li>Rachel Day</li>
  </ul>

###License

  MIT.
  
##Acknowledgements
 
 Besides my own game-play experience, data on optimizing pairings gleaned from :
 
  * <a href ="http://fireemblem.wikia.com/wiki/Fire_Emblem_Wikia">Fire Emblem Wikia</a></li>
  * Serene Forest <a href = "https://serenesforest.net/wiki/index.php/Fates_Support_Conversations">support conversation database</a> for Fates</li>
  * <a href = "https://www.reddit.com/r/fireemblem/comments/1fle46/the_ideal_parent_day_14_recap/">Reddit</a>
  * Gamefaqs message boards</li>
  * <a href ="https://www.reddit.com/r/fireemblem/comments/48u8b4/fe14_optimal_fates_pairings_birthright_conquest/">This fantastic MatLab program </a> created by <a href = "https://www.reddit.com/user/DoctorBandage">DoctorBandage</a> using <a href = "https://www.reddit.com/u/Shephen">Shephen</a>'s pairing guide.
