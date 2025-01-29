def unique(mylist):
    new_list=[]
    for elem in mylist:
        if elem not in new_list:
            new_list.append(elem)
    return new_list
