class Location:
	def __init__(self, attributes):
		self.label = attributes['label']
		self.point = Point(attributes)

	def get_point(self):
		return self.point


class Point:
	def __init__(self, attributes):
		self.latitude = attributes['latitude']
		self.longitude = attributes['longitude']
