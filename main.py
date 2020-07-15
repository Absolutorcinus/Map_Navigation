import csv

"""
transform map into dataset:(Origine_Node, Direction, Destination_node) 
for flexibility in manupilation (in case the solution for some tasks
 can be handeled in a database management system)
example: a1 e:a2 s:a3   -> a1, e, a2 
                           a1, s, a3 

"""
file_in=open("maptxt.txt","rt") # the text file with the description of the map
file_out = open("out.csv", "wt") # the csv file  which will contain the processed data

# replacing " : ' and " \s " with "," and save as csv file 
for line in file_in:
	file_out.write(line.replace(':',',').replace(' ',','))
    
file_in.close()
file_out.close()


# putting every row from out.csv into list form ("origin node""relation""neighbour node")
list_list_relations= list() # list that will contain out data [["origin node","relation","neighbour node"]...]

with open('out.csv', mode='r') as infile:
    reader = csv.reader(infile)
    
    for i in reader:
        
        for j in range(1,len(i),2):
            list_list_relations.append([i[0],i[j], i[j+1]])



"""
function that returns list of indexes where 
the first value of the element of the list
equals to the value inserted (Occurences)

"""              

def getIndexes(listOfLists,origineNode):

    index_list=list()
    
    for i in range(len(listOfLists)):
        if origineNode == listOfLists[i][0]:
            index_list.append(i)

    return index_list


"""
Function that returns all the possible directions for a given node
"""    

def getPossibleDirections(listOfLists, origineNode):
    
    listIndexes = getIndexes(listOfLists, origineNode)
    listPossibleDrct = list()
    
    for idx in listIndexes:
        
        listPossibleDrct.append(listOfLists[idx][1])
        
    return listPossibleDrct
    


"""
Function that returns the index of an element in the list
""" 
def getDirectionIndex(listOfelements, directionChoice):
    
    return listOfelements.index(directionChoice)

"""
function to display the available diretions Ex: nsw
"""
def displayList(lista):
    return (''.join(lista))
    

    


count=0
i='a0'
print("------------------------------")
while (count < 3):
   
    
    print("you are in room: ", i)

    index_of_matches = getIndexes(list_list_relations,i)
#print(index_of_matches)
    directions = getPossibleDirections(list_list_relations,i )
#print(directions)
    print("you can move: ",displayList(directions))
    
    while True:
       user_choice = input()

       if user_choice in directions:
           break
       print("type the corect direction")
        
       
    

    index_of_direction_choice = getDirectionIndex(directions,user_choice)
#print(index_of_direction_choice)
    corresponace = getIndexes(list_list_relations,i)[index_of_direction_choice]

    print("your choice", user_choice)
    print("------------------------------")
   
    i = list_list_relations[corresponace][2]   
    count+=1




