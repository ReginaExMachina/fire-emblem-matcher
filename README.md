# fire-emblem-matcher
Optimizing character pairings.

###Contents
    * <a href ="https://github.com/ReginaExMachina/fire-emblem-matcher/blob/master/README.md#description">Description</a>
    * <a href = "https://github.com/ReginaExMachina/fire-emblem-matcher/blob/master/README.md#description">Getting Started</a>
    * <a href = "https://github.com/ReginaExMachina/fire-emblem-matcher/blob/master/README.md#description">Gale-Shapley algorithm</a></li>
    * <a href = "https://github.com/ReginaExMachina/fire-emblem-matcher/blob/master/README.md#authour">Author</a></li>
    * <a href = "https://github.com/ReginaExMachina/fire-emblem-matcher/blob/master/README.md#license>License</a></li>
    * <a href = "https://github.com/ReginaExMachina/fire-emblem-matcher/blob/master/README.md#acknowl">Acknowledgement</a></li>
  
###Description

Matching Fire Emblem characters can be complicated. And it doesn't get any easier if you care about good supports, the child's hair colour AND making the best possible child unit for combat.

This program is designed to help players out.

##Getting Started

TBA.

###Gale–Shapley algorithm

<code>fire-emblem-matcher</code> uses the Gale-Shapley algorithm to make matches.

With this algorithm the 'men' (or the group proposing) typically ends up with a matches that are higher up in their preference list than the 'women' (aka the group being proposed to).

Thefore in Awakening the proposer group is the <b>female characters</b>, but in Fates it's the <b>males</b>. This prioritizes the child-bearing units (so to speak) so that they get the best possible matches.

For more info check out the <a href = "https://en.wikipedia.org/wiki/Stable_marriage_problem">Wiki</a>.

###Issues

Cannot handle Fire Emblem list:

  <ol>
  <li>For multiple branches of fates <code>propose_to</code> and <code>respond_to</code> methods need to be able to handle non-existent preferences.</li>
  
  <li>Requires full range of preferences but this does not reflect reality where some characters cannot match (ie. Laslow-Sakura or any siblings). May fixed with change to above</li>
  </ol>

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
  * Gamefaqs message boards</li>
  * <a href ="https://www.reddit.com/r/fireemblem/comments/48u8b4/fe14_optimal_fates_pairings_birthright_conquest/">This fantastic MatLab program </a> created by <a href = "https://www.reddit.com/user/DoctorBandage">DoctorBandage</a> using <a href = "https://www.reddit.com/u/Shephen">Shephen</a>'s pairing guide.
