
class Plant():

	plt_name = ""
	plt_date = "12/12/1990"
	plt_seasonActive = [True,True,True,True]
	plt_timeBtwWater = 2

	def __init__(self, name, date, datesActive, waterTime):
		self.plt_name = name
		self.plt_date = date
		self.plt_seasonActive = datesActive
		self.plt_timeBtwWater = waterTime
	def getName(self):
		return self.plt_name

	def getDate(self):
		return self.plt_date

	def getSeasonActive(self):
		return self.plt_seasonActive

	def getTimeWater(self):
		return self.plt_timeBtwWater