import trees
import treePlotter

# reference: machine learning in action
fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = trees.createTree(lenses, lensesLabels)
print(lensesTree)
treePlotter.createPlot(lensesTree)
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
test_vec = ["young", "myope", "no", "reduced", "no"]
result = trees.classify(lensesTree, lensesLabels, test_vec)
print(result)
