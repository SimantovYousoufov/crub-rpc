from concurrent import futures
import time

import grpc
import json

from models.models import Location, Point
import crub_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Crub(crub_pb2.CrubServicer):
	def GetLocation(self, request, context):
		with open('./database/locations.json') as data_file:
			data = json.load(data_file)

		location = data['locations'][0]
		return crub_pb2.Location(label=location['label'])

	def ListLocations(self, request, context):
		with open('./database/locations.json') as data_file:
			data = json.load(data_file)

		for location in data['locations']:
			time.sleep(3)
			point = crub_pb2.Point(latitude=location['latitude'], longitude=location['longitude'])
			yield crub_pb2.Location(label=location['label'], point=point)


def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	crub_pb2.add_CrubServicer_to_server(Crub(), server)
	server.add_insecure_port('[::]:50051')
	server.start()
	try:
		while True:
			time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		server.stop(0)


if __name__ == '__main__':
	serve()
