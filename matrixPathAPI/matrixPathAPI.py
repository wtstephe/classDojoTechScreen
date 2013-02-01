import urllib
import urllib2
from urllib2 import HTTPError

class MatrixPathAPI:
    def __init__(self, serverURL):
        self.serverURL = serverURL

    #findMatrixPath()
    #Takes in a list of lits representing a matrix, and asks the server to 
      #compute the shortest path through it. 
    #Returns a file-like object (that may be an HTTPError) that responds to
      #.read() and .code
    def findMatrixPath(self, mtx):
        data = {'matrix' : str(mtx)}
        encodedData = urllib.urlencode(data)
        request = urllib2.Request(self.serverURL)

        response = ""
        try:
            response = urllib2.urlopen(request, encodedData)
        except HTTPError as e:
            response = e
        return response
