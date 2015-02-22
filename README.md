# hiveplot
Hive Plots in using Python &amp; matplotlib!

# How to use hiveplot

Hive plots are non-trivial to create, but I have made this Python package to help boil it down to the essentials.

To start, I assume that you have some network data. In your network data, you will have nodes and edges.

Firstly, decide how you will group your nodes. Hive plots work best with up to 3 groups. Secondly, decide how you will order your nodes along each group. A common ordering is by degree centrality. Together, you can put together the first parameter put into hiveplot, which is a dictionary of `{group:[list_of_nodes]}`.

Example code:

    ## assume that you have a graph called G
    nodes = dict()
    nodes['group1'] = [n for n, d in G.nodes(data=True) if d == some_criteria()]
    nodes['group2'] = [n for n, d in G.nodes(data=True) if d == other_criteria()]
    nodes['group3'] = [n for n, d in G.nodes(data=True) if d == third_criteria()]
    
Next, you will need your list of edges. Typically, you can just use the edge list from `G`.

    edges = [(u, v, d) for u, v, d in G.edges(data=True)]
    
Finally, you will need a color map for the nodes.

    cmap = dict()
    cmap['group1'] = 'green'
    cmap['group2'] = 'red'
    cmap['group3'] = 'blue'
    
Once all of this is setup, you can plot the Hive Plot!

    h = HivePlot(nodes, edges, cmap)
    h.draw()
    
All contributions to improve the package are welcome!
