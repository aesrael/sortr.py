def checkName(name):
    nameStore = []
    for i in range(3):
        nameInput = input('enter a name: ')
        nameStore.append(nameInput)
    print(nameStore)
    if name in nameStore:
        print (name, 'name here at position',
               nameStore.index(name), ' of list')
    else:
        print(name, 'not in list')


checkName('temi')
