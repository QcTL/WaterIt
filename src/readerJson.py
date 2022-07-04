import json
import os
import infoPlant

PATH = os.path.dirname(os.path.realpath(__file__))

class ReadorJSON():
	"""
    A class to save and extract the values of a json file and torn it into Plants

    ...

    Attributes
    ----------
    instPlants : list[Plants]
    	A list of plants extracted from the json
	pathJSON : str
		A path to the json file relative to the project folder
    Methods
    -------
		readFromJson(self):
			read a file from the path that ahs to had a least [{}], and save all the plants that can extract to instPlants
		getPlantsJson(self):
			return the list of plants extracted from json, have to be called after
		savePlantsToJson(self, listPlantsEdited):
			save the list of plants in the parameter and save it in a json file the same path of the reading functions, making that the file replace the old version
    """
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
			self.instPlants.append(infoPlant.Plant(listPlants[i]['name'], listPlants[i]['date'], listPlants[i]['seasonActive'], listPlants[i]['timeBtwWater'], listPlants[i]['lastDayWater']))

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
				'seasonActive':listPlantsEdited[i].getSeasonActive(),
				'lastDayWater':listPlantsEdited[i].getLastTimeWater()
				})

		open(PATH + "/../" + self.pathJSON, 'w').close()

		with open(PATH + "/../" + self.pathJSON, 'w') as f:
			json.dump(listJsonAble, f)
