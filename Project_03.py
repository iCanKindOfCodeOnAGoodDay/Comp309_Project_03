"""
    Scott Quashen
    CSC 309 SFSU Spring 2024
    Project #3
    Created on Wednesday Feb 21 02:07 2024  
    Last Updated Friday Feb 23 00:30

    Description: 
        The program requests N, and S to create a list of random numbers. 
        A custom sort function orders those numbers low to high, 
        Checks to see if List is sorted before and after sorting func, incrementally printing status.
        
    
    Inputs: 
        S: int (seed value)
        N: int (amount of items in L)
        M: int (amount of items to print per row)
        Minimum & Maximum: int values for creating random number range
        prompt:  String (message requesting user input for S and N)
        size: Int (local variable for number generating func)
        seed: Int (local variable for number gen func)

    Returns: 
        L: List of random numbers
        Num: int which is the value of the user input used for seed and size
        boolean value: checkIfListIsInAscendingOrder() returns true or false
        

    Dependencies: random, time

    Assumptions: developed and tested using Spyder 5.4.3, Python version 3.11.5 on macOS 14.3.1
"""

#--------------------------project imports section

import random
import time




#--------------------------function definitions section


def createRandomNumbersList( size, seed, minimum, maximum ):
    """
    
    Description
    ----------
    createRandomNumbersList() returns a list of size N containing pseudo-random numbers based on seed value

    Parameters
    ----------
    size : 
        int
        Amount of random numbers to create and add to our list
    seed : 
        int
        Used for creating the same random numbers each time program is run
    minimum : 
        int
        Minimum value that a random number could be
    maximum : 
        int
        Maximum value that a random number could be

    Returns
    -------
    L : 
        List
        Contains the random integers  

    """
    # create local list
    L = []
    random.seed( seed, int )
    for i in range( size ):
        L.append( random.randint( minimum, maximum ) )
    # export local list
    return L

# end of randomNumber() function


def findAndSwapByOnePosition( someList ):
    """
    
    Description
    ----------
    findAndSwapByOnePosition() checks each item in list and swaps it with the next if the next is smaller.
    
    Parameters
    ----------
    someList : 
        List
        We keep passing in the same list that keeps updating each iteration
   
    Returns
    -------
    None.
    

    """
    for i in range( 0, len( someList ) - 1 ):
         if someList[ i + 1 ] <= someList[ i ]:        
             # then we found an item that needs to be swapped
             # swap items, holding one value in a new var
             c = someList [ i ]
             # swap right
             someList [ i ] = someList [ i + 1 ]
             # swap left
             someList [ i + 1 ] = c

# end of findAndSwapByOnePosition() function            

                    
def callSwapAsManyTimesAsNeededUntilFinished( someList ):
    """
    
    Description
    ----------
    callSwapAsManyTimesAsNeededUntilFinished() does not stop calling our swap func until 
    all items in our list is 100% completely in ascending order, 
    at which point finished = true and the loop bails.
   
    Parameters
    ----------
    someList : 
        List  
        The List of random numbers we will be sorting
    
    Returns
    -------
    None.
   

    """
    finished = False
    while not finished:
        for i in range( len( someList ) ):
            # run through list one time, swapping values if needed
            if someList[ i - 1 ] > someList[ i ]:
                findAndSwapByOnePosition( someList )                
            else:
                # above, items were only swapped one time each, may need to move further left or right
                for i in range(len( someList )):
                    if i > 0:
                        if someList[ i - 1 ] > someList[ i ]:
                            # then we found an item out of order, sort again
                            findAndSwapByOnePosition( someList )
                        if i == len( someList ) - 1:
                            # we've reached the end of the list and all previous numberss in order
                            finished = True 
                                
# end of callSwapAsManyTimesAsNeededUntilFinished() function      
      

def checkIfListIsInAscendingOrder( someList ):
    
    """
    
    Description
    ----------
    checkIfListIsInAscendingOrder() he loop can end in 2 ways. 1) return failure 2) return success
   
    Parameters
    ----------
    someList : 
        List  
        The List of random numbers we will be sorting
    
    Returns
    -------
    True or False
        True if the list is ascending order, else the return is False.
   

    """
    print( "Is the List sorted?" )
    for i in range( len( someList ) ): 
        if i > 0:
            if someList[ i - 1 ] > someList[ i ]:
            # search for values that are out of order
                return False
            if i == len( someList ) - 1:
            # We've reached the end of list, all previous numbers in order 
                return True
            
# end of checkIfListIsInAscendingOrder() function


def getInteger( prompt ):
    """
    
    Description
    ----------
    getInteger() requests input, asks user to try again IF they don't input an int.

    Parameters
    ----------
    prompt : 
        String
        The message presented to the user when requesting an int in the console.

    Returns
    -------
    num :
        int
        The function returns the integer that the user provides via the console

    """
    
    while True:
        # prompt user
        try:
            num = int( input( prompt ) )
        except ValueError:
            # only accept int values
            print( "That is not an integer -- please try again" )
            # restart the loop if needed
            continue
        return num
    
# end of getInteger() function


def printList( someList, M ):
    """
    
    Description
    ----------  
    printList() prints a list of integers with M items per row.
    Parameters
    ----------
    someList : 
        List
        The random numbers.
    M : 
        int
        Amount of items per row to print in console.

    Returns
    -------
    None.

    """
    for i in range( len( someList ) ):
        # don't print an extra space at the begininng 
        if i > 0:
            if i % M == 0:
                # new line of numbers (M items per row)
                print( "" )
        # print each number one at a time, on the same line        
        print( someList[ i ], end= ", " )    
        
# end of printList() function        




#--------------------------main code section
 
# print my name and time
print( "Scott Quashen..." + time.asctime() )

# prompt user
N, S = getInteger( "Size of list wanted? " ), getInteger( "Random number seed value? " )

# create the list
L1 = createRandomNumbersList( N, S, -99, 99 )

print( "Here is the unsorted list: " )
printList( L1, 8)

# run check
print( checkIfListIsInAscendingOrder( L1 ) )

# sort the list
callSwapAsManyTimesAsNeededUntilFinished( L1 )

print( "Here is the sorted list: " )
printList( L1, 10 )

# run check
print( checkIfListIsInAscendingOrder( L1 ) )

#-------------------------- end 










