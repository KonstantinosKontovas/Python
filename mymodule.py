def intersect (a,b):
    set1 = set(a)
    set2 = set(b)
    set3 = set1.intersection(set2)
    return set3

#Each time you import a function you have to use :
# from filename (in this case is mymodule) import functionname (in this case the name is intersect)

# after from          import         
# just call the respective function . ex :

#from mymodule import intersect
#listone =[1,2,3,4,5,6]
#listtwo =1,3,5,7,9]
#intersect(listone,listtwo)