cupcakes = np.array([2, 0.75, 2, 1, 0.5])
recipes = np.genfromtxt('recipes.csv', delimiter=',')
print (recipes)
eggs = recipes[:,2]
one_egg = recipes[(eggs)]
print (one_egg)
cookies = recipes[2,:]
double_batch = cupcakes * 2
grocery_list = cookies, double_batch
print(grocery_list)