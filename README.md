# fire-emblem-sorting
Optimizing character pairings.


##Gale–Shapley algorithm

<a href = "https://en.wikipedia.org/wiki/Stable_marriage_problem">Wiki</a>

###Issues

Cannot handle Fire Emblem list:

  1) For managing  multpile branches of fates <code>propose_to</code> and <code>respond_to</code> methods need to be able to handle non-existent preferences
  2) Requires full range of preferences but this does not reflect reality where some characters cannot match (ie. Laslow-Sakura or any siblings). May fixed with change to above.
