

class Plant():
	"""
    A class used to represent a Plant

    ...

    Attributes
    ----------
    plt_name : str
        Name of the plant
    plt_date : str
        Date of the plant first registered
    plt_seasonActive : list[bool]
        Seasons when the plant is active: [Winter,Spring,Summer,Autumn]
    plt_timeBtwWater : int
        Time Btw Watering the plant in active seasons
    Methods
    -------
		Getters of all the Methods
			getName(self) -> str , return plt_name
			getDate(self) -> str , return plt_date
			getSeasonActive(self) ->  list[bool] , return plt_seasonActive
			getTimeWater(self) -> int , return plt_timeBtwWater
    """

	plt_name: str = ""
	plt_date: str = "12/12/1990"
	plt_seasonActive: list[bool] = [True,True,True,True]
	plt_timeBtwWater: int = 2

	def __init__(self, name : str, date : str, datesActive : list[bool], waterTime: int):
		"""
        Parameters
        ----------
        name : str
            The name of the plant
        date : str
            The date of the registery
        datesActive : list[bool]
            Seasons where de plant is active: [Winter,Spring,Summer,Autumn]
        waterTime: int
			Days Btw Watering the plant in active seasons
        """

		self.plt_name = name
		self.plt_date = date
		self.plt_seasonActive = datesActive
		self.plt_timeBtwWater = waterTime
	
	def getName(self) -> str:

		return self.plt_name

	def getDate(self) -> str:
		return self.plt_date

	def getSeasonActive(self) ->  list[bool]:
		return self.plt_seasonActive

	def getTimeWater(self) -> int:
		return self.plt_timeBtwWater