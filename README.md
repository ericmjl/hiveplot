# hiveplot
Hive Plots in using Python &amp; matplotlib!

# How to use hiveplot

Hive Plots are used for visualizing large network data in a rational way. Hive Plots are non-trivial to create, but I have made this Python package to help boil it down to the essentials. 

The original creator of Hive Plots is Martin Krzywinski of the BCGSC. His website is at: http://mkweb.bcgsc.ca

An example graph is available in the `test` folder. Alternatively, you can view the IPython notebook online: http://nbviewer.ipython.org/github/ericmjl/hiveplot/blob/master/test/Tests.ipynb

To start, I assume that you have some network data. In your network data, you will have nodes and edges.

Firstly, decide how you will group your nodes. Hive plots work best with up to 3 groups. Secondly, decide how you will order your nodes along each group. A common ordering is by degree centrality, which is how hiveplot currently does it automatically. Together, you can put together the first parameter put into hiveplot, which is a dictionary of `{group:[list_of_nodes]}`.

Example code:

    ## assume that you have a graph called G
    nodes = dict()
    nodes['group1'] = [n for n, d in G.nodes(data=True) if d == some_criteria()]
    nodes['group2'] = [n for n, d in G.nodes(data=True) if d == other_criteria()]
    nodes['group3'] = [n for n, d in G.nodes(data=True) if d == third_criteria()]
    
Next, you will need to group your edges. Do this in a similar fashion as nodes.

    edges = dict()
    edges['group1'] = [(u,v,d) for u,v,d in G.edges(data=True) if d == some_criteria()]
    ...
    

    
Finally, you will need a color map for the nodes and edges respectively.

    nodes_cmap = dict()
    nodes_cmap['group1'] = 'green'
    nodes_cmap['group2'] = 'red'
    nodes_cmap['group3'] = 'blue'

	edges_cmap = dict()
	edges_cmap['group1'] = 'green'
	...
	
    
Once all of this is setup, you can plot the Hive Plot!

    h = HivePlot(nodes, edges, nodes_camp, edges_cmap)
    h.draw()
    
All contributions to improve the package are welcome!
