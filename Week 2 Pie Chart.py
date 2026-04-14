#got it, Caleb
import matplotlib.pyplot as plot

# set up your lists

numlist = [8, 6, 5, 3]

namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']

colorlist = ['blue', 'green', 'pink', 'white' ]

explodelist = [0.5, 0.1, 0.0, 0.0]

# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%d%%', colors=colorlist, explode = explodelist, startangle = 200)
plot.axis('equal')
plot.savefig('piechart3.png')
