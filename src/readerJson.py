import json
import os
import infoPlant

PATH = os.path.dirname(os.path.realpath(__file__))

class ReadorJSON():
	instPlants = []
	pathJSON = ""
	def __init__(self, pathJSON):
		self.pathJSON = pathJSON 
		
	def readFromJson(self):
		with open(PATH + "/../" + self.pathJSON, 'r') as openfile:
			plant_obj = json.load(openfile)

		listPlants = plant_obj
		print("Lectura INICI: " + str(len(listPlants)))
		for i in range(0,len(listPlants)):
			self.instPlants.append(infoPlant.Plant(listPlants[i]['name'], listPlants[i]['date'], listPlants[i]['seasonActive'], listPlants[i]['timeBtwWater']))

	def getPlantsJson(self):
		return self.instPlants

	def savePlantsToJson(self, listPlantsEdited):
		
		listJsonAble = []
		print(listPlantsEdited)
		for i in range(0,len(listPlantsEdited)):
			listJsonAble.append({
				'name' : listPlantsEdited[i].getName(),
				'date':listPlantsEdited[i].getDate(),
				'timeBtwWater':listPlantsEdited[i].getTimeWater(),
				'seasonActive':listPlantsEdited[i].getSeasonActive()
				})

		open(PATH + "/../" + self.pathJSON, 'w').close()

		with open(PATH + "/../" + self.pathJSON, 'w') as f:
			json.dump(listJsonAble, f)
