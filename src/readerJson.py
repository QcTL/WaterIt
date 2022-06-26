import json
import os
import infoPlant

PATH = os.path.dirname(os.path.realpath(__file__))

class ReadorJSON():
	instPlants = []

	def __init__(self, pathJSON):
		with open(PATH + "/../" + pathJSON, 'r') as openfile:
			plant_obj = json.load(openfile)

		listPlants = json.loads(plant_obj)

		for i in range(0,len(listPlants)):
			self.instPlants.append(infoPlant.Plant(listPlants[i]['name'], listPlants[i]['date'], listPlants[i]['seasonActive'], listPlants[i]['timeBtwWater']))

		print(self.instPlants)

		#listPlants.insert(0,{"name":"MACARON","deparment":"PLANTERA"})

		listPlantsjson = json.dumps(listPlants)
			
		#with open(PATH + "/../" + pathJSON, 'w') as f:
		#	json.dump(listPlantsjson, f)
		print(listPlantsjson)

	def getPlantsJson(self):
		return self.instPlants