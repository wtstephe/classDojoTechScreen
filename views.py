from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from pathfinder import *

@csrf_exempt
def receiveRequest(request):
	response = ""
	status = 200
	if request.method != "POST":
		response = ("Error: Server only accepts requests of "
			    "method POST")
		status = 400
	else:
		try:
			mtx = json.loads(request.POST["matrix"])
			if not ( checkMatrixFormat(mtx) ):
				response = "Error: could not decode matrix format"
				status = 400
			else:
				response = "The shortest path is %d" \
				    % findPath(mtx)
		except KeyError:
			response = ("Error: key \"matrix\" not found in the "
				    "POST parameters")
			status = 400
		except ValueError:
			response = ("Error: could not decode matrix format")
			status = 400
	return HttpResponse(response, status = status)



