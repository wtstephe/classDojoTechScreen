import sys

#checkMatrixFormat()
#Checks that a list of lists is a matrix of integers; that is, that it is 
  #rectangular and contains only ints
def checkMatrixFormat(mtx):
    lenFirstRow = len(mtx[0])

    for row in range( len(mtx) ):
        if ( len(mtx[row]) != lenFirstRow ):
            return False

        for col in range( len(mtx[0]) ):
            if not ( type(mtx[row][col]) is int ):
                return False
            
    return True
                      


#findPath()
#Takes a matrix as input and returns the minimum path from the top to the bottom
  #of it
#Algorithm goes along each row, selecting whichever entry above it gives the shortest
  #path.
def findPath(mtx):
    pathWeightMtx = [[ 0 for j in range(len(mtx[0]))] for i in range(len(mtx))]
    for a in range(len(mtx[0])):
        pathWeightMtx[0][a] = mtx[0][a]

    for row in range(1, len(mtx)):
        for col in range(len(mtx[0])):

            #Find the predecessor with the shortest path to it
            minPred = sys.maxint
            for i in range(-1, 2):
                if ( i+col >= len(mtx[0]) or i+col <= -1 ):
                    continue
                curPathWeight = mtx[row][col] + pathWeightMtx[row-1][col+i]
                if ( curPathWeight < minPred ):
                    minPred = curPathWeight
            pathWeightMtx[row][col] = minPred

    return min( pathWeightMtx[len(mtx)-1] )
                
    
