# Name:  - Musayeroh Bah
# Peers:  - names of CSC252 students who you consulted or ``N/A'' <br>
# References:  - URL of resources used <br>
import math
import time
import csv          # Used to read a .csv file.

### DO NOT EDIT ###
def new_array(size: int):
    """ Creates a new array of a given size.
    :param size: (int) the number of 0s you want in the array
    :return : (list) the array with zeros 
    >>> new_array(3)
    [0,0,0]
    """
    L = [0] * size
    return L

class HashNode:
    """Class to instantiate linked list node objects, with both a key and a value.
    >>> node = HashNode(7, "Matt Damon")
    >>> print(node)
    {key:7, value:Matt Damon}
    """
    
    def __init__(self, key:int, value:str) -> None:
        """ Constructor of new node with a key and value. Initially nodes do not have a next value.
        :param key: (int) the key that will be added to the node
        :param value: (str) the value that will be added to the node
        :return : (HashNode) a pointer to the object
        """
        self.key = key
        self.value = value
        self.next = None
        
    def __str__(self) -> str:
        """ Returns a string representation of the object.
        :return : (str) a string description of the HashNode object.
        """
        return "{key:" + str(self.key) + ", value:" + self.value + "}"     
### END OF DO NOT EDIT###



# Hint: create a linked list class here...

class SLL: 
    def __init__(self, head):
        self.head = None
    
    def insert(self, key, value):
        new_node = HashNode(key, value)
        
        if self.head == None:
            self.head = new_node
        else:
            last = self.head
            while (last.next != None):
                last = last.next
            last.next = new_node # type: ignore


    # def delete(self, HashNode):
    #     j = 1
    #     current = L
    #     previous = NIL
    #     while current.next != NIL
    #     if j != i
# 6 previous = current
# 7 current = current.next
# 8 j = j + 1
# 9 else
# 10 if previous == NIL
# 11 L = L.next
# 12 else
# 13 previous.next = current.next.next
# 14 current.next = NIL
# 15 break

    def getValue(self, HashNode): pass

def new_object_array(size: int) -> list[SLL]:
    """ Creates a new array of a given size.
    :param size: (int) the number of 0s you want in the array
    :return : (list) the array with zeros 
    >>> new_array(3)
    [None,None,None]
    """
    L:list[SLL] = [SLL(None)] * size
    return L
    

    


class HashTable:
    
    def __init__(self, size:int, hash_choice:int) -> None:
        self.size = size
        self.hash_choice = hash_choice                  # Which hash function you will use.
        #TODO Finish constructor...

        self.table = new_object_array(size)
        
        for i in range(len(self.table)):
            self.table[i] = SLL(None)  #never return anything in constructors btw
        
        
        
    
    def __str__(self) -> str:
        table_contents = ""

        for i in range(len(self.table)):
            curr = self.table[i].head
            if curr == None:
                return ""
            
            while (curr.next != None):
                table_contents += str(curr.key) + ": " + str(curr.value) + ", "
                curr = curr.next
            
        return "Hash Table: " + table_contents
        
    def hashFunc(self, key:int) -> int:
        if type(key) != int:
            return None
        if self.hash_choice == 0:
            return hash(key) % self.size    #Embedded Python hash function.
        elif self.hash_choice == 1:
            return 0    #Everything in the has ia stored in a single linked list.
        elif self.hash_choice == 2:
            pass #TODO Implement your has functions here.
        elif self.hash_choice == 3:
            pass #TODO Implement your has functions here.
        elif self.hash_choice == 4:
            pass #TODO Implement your has functions here.
        return None
    
    def insert(self, key:int, val:str) -> bool:
        #access the linked list at the index (given by the key) in the array.
        #index given by hashing the key
        new_node = HashNode(key, val)
        current = self.table[self.hashFunc(key)].head
        
        if current == None:
            self.table[self.hashFunc(key)].head = new_node
            return False
                
        # #go through the linkedlist and find the key
        while (current.next != None) : 
            #shouldn't you check if the value isn't already there? can i return true here or is it supposed to return false?
            if current.key == key:
                current.value = val
                return True
            current = current.next
        
        #should i make an addLast function for SLLs? nahh insert kinda works like that anyway
        
        if (current.next == None):
            self.table[self.hashFunc(current.key)].next = HashNode(key, val)
        
        
        return False

    def getValue(self, key:int) -> str:
        current = self.table[self.hashFunc(key)].head

        if current == None:
            return "No value found"

        #go through the linkedlist and find the key
        while (current.next != None) : 
            if current.key == key:
                return str(current.value);

        #uhm, should I have a getNode function? How do I get the node that the linkedlist is pointing to? 
        

        return None

    def remove(self, key:int) -> bool:
        current = self.table[self.hashFunc(key)].head

        if current == None:
            return False
        
        while (current.next != None): 
            if current.key == key:
                current.delete(key);

        return False
    
    def isOverLoadFactor(self) -> bool:
        return False
    
    def reHash(self) -> bool:
        return False
            
                    
def main():
    # You should update these three values as you test your implementation.
    hash_to_test = 0    
    initial_bucket_size = 10 
    initial_num_to_add = 100

    hash_table = HashTable(initial_bucket_size, hash_to_test)
    with open('hwk4-people.csv') as csv_file:    
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = csv_reader.__next__()
        for row_iterator in range(initial_num_to_add):
            row = csv_reader.__next__()
            hash_table.insert(int(row[0]),row[1])
        print("Hash Map Initialized")
                
        option = ""
        while option != "QUIT":
            option = input("Select an option (ADD, GET, REMOVE, PRINT, CHECK, REHASH, QUIT): ").upper()        

            if option == "ADD":
                row = csv_reader.__next__()
                hash_table.insert(int(row[0]),row[1])
                print("Added - Key:", int(row[0]), "\tValue:", row[1])
            elif option == "GET":
                key = int(input("Which # would you like to get the value of? "))
                val = hash_table.getValue(key)
                if val is None:
                    print("Error,", key, "not found.")
                else:
                    print(val)
            elif option == "REMOVE":
                key = int(input("Which # would you like to remove? "))
                suc = hash_table.remove(key)
                if suc:
                    print(key, "was removed.")
                else:
                    print("Error,", key, "was not removed.")                    
            elif option == "PRINT":
                print(hash_table)   # calls the __str__ method.  
            elif option == "CHECK":
                isOver = hash_table.isOverLoadFactor()
                if isOver:
                    print("Your load factor is over 0.7, it's time to rehash.")
                else:
                    print("Load factor is ok.")
            elif option == "REHASH":
                suc = hash_table.reHash()
                if suc:
                    print("Rehash was successful.")
                else:
                    print("ERROR: rehash failed.")
            elif option == "QUIT" or option == "Q":
                break 
            else:
                print("Error: invalid input, please try again.")
                
        print("Goodbye!")
            

def profilerMain():    
    # You should update these three values as you profile your implementation.
    num_hash_implemented = 2    
    initial_bucket_size = 10 
    initial_num_to_add = 100

    for i in range(0, num_hash_implemented):        
        hash_table = HashTable(initial_bucket_size, i)
        with open('hwk4-people.csv') as csv_file:    
            csv_reader = csv.reader(csv_file, delimiter=',')
            header = csv_reader.__next__()
            for row_iterator in range(initial_num_to_add):
                row = csv_reader.__next__()
                hash_table.insert(int(row[0]),row[1])
            print("Hash Map", i, "Initialized")
            start_time_create = time.time()    # Get start Time.
            #### Start of code you want to profile ####
            
            # Add/Edit code to profile
            row = csv_reader.__next__() 
            hash_table.insert(int(row[0]),row[1])
            
            #### End of code you want to profile ####
            end_time_create = time.time()      # Get end Time. 
            calc = end_time_create - start_time_create  
            print("Hash Map", i, "Test \tTime:", calc, "seconds.")
        
    

if __name__ == "__main__":
    # Swap these options to profile or test your code.
    #profilerMain()     
    main()
    
