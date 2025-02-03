def spam():
    global eggs
    eggs = 'spam'  # this is the global

def bacon():
    eggs = 'bacon'  # this is a local var

def ham():
    print (eggs)


eggs = 42
spam()
print(eggs)
