from __future__ import print_function

import grpc
import json
from pprint import pprint as pp
from datetime import datetime

from models.models import Location, Point
import crub_pb2


def run():
	channel = grpc.insecure_channel('localhost:50051')
	stub = crub_pb2.CrubStub(channel)

	point = crub_pb2.Point(latitude=45.042000, longitude=-75.005454)

	response = stub.GetLocation(point)
	print("===================================")
	print("Crub client received (simple rpc): ")
	pp(response)
	print("===================================")

	for location in stub.ListLocations(point):
		time = datetime.now().time()
		print("Crub client received (stream) at " + str(time) + ": ")
		pp(location)
		print("===================================")


if __name__ == '__main__':
	run()
