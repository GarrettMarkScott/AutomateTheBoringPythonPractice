import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie','Pooka','Simon']
shelfFile['cats'] = cats
shelfFile.close()

Cats = shelve.open('mydata')

Cats['cats']