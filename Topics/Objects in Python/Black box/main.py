# use the function blackbox(lst) that is already defined
names = ['Ann', 'Max']
my_list = blackbox(names)
if id(names) == id(my_list):
    print("same")
else:
    print("new")
