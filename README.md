# fire-emblem-matcher
Optimizing character pairings.


##Gale–Shapley algorithm

<a href = "https://en.wikipedia.org/wiki/Stable_marriage_problem">Wiki</a>

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
    
###Acknowledgements
 
 In addition to my own game-play experience, data on optimizing pairings gleaned from :
 
 <ul>
    <li>Fire Emblem Wikia</li>
    <li>Serene Forest support conversation database</li>
    <li>Gamefaqs message boards</li>
    <li>this</li>
 </ul>
