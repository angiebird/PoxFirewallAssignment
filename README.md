# PoxFirewallAssignment
mininet> pingall 
*** Ping: testing ping reachability
h1 -> h2 h3 h4 h5 h6 h7 X 
h2 -> h1 h3 h4 h5 h6 X h8 
h3 -> h1 h2 h4 h5 X h7 h8 
h4 -> h1 h2 h3 X h6 h7 h8 
h5 -> h1 h2 h3 X h6 h7 h8 
h6 -> h1 h2 X h4 h5 h7 h8 
h7 -> h1 X h3 h4 h5 h6 h8 
h8 -> X h2 h3 h4 h5 h6 h7 
*** Results: 14% dropped (48/56 received)
