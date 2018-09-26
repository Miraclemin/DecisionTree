import trees
import treePlotter

myDat, labels = trees.createDataSet()
myTree = trees.createTree(myDat, labels)
print(myTree)
treePlotter.createPlot(myTree)

trees.classify(myTree, labels, [1, 0])
