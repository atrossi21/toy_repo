from tristate_CA import *
from matplotlib import pyplot as plt
rule_number = 110
length = 100
time = 100


# create the lookup table dictionary and neighbors

init_cond, neighbor = initi(rule_number,length, time)

lookup_table=vocabulary(rule_number, neighbor)

# Create space-time field and current configuration.

spacetime_field=space_time(time,length, init_cond,lookup_table)


#plot_graph

plt.figure(figsize=(12,12))
plt.imshow(spacetime_field, cmap=plt.cm.Greys, interpolation='nearest')
plt.show()



