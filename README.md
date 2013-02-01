classDojoTechScreen
===================

The server can be started with ./manage.py runserver ip:port.  It requires the django and json packages to run.

The python API for using the server is contained in the matrixPathAPI directory.  It can be used by:

from matrixPathAPI import MatrixPathAPI
mpa = MatrixPathResponse(serverAddress)
ret = mpa.findMatrixPath([[3,1,4],[1,5,8],[2,6,5]]
print ret.read()
