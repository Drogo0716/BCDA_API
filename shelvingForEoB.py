import shelve

shelfFile = shelve.open('shelf_For_EoB_Key_Separation')
shelfFile['init'] = True
shelfFile['write'] = False
print(list(shelfFile.values()))
print(list(shelfFile.keys()))
#print(shelfFile['init'])
shelfFile.close()
