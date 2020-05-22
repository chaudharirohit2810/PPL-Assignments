class Cat:
    def __init__(self, sound = None):
		#Public Variable
        self.ears = 2  
        self.color = "White"

		#Private Variables
        self.__legs = 4 
        self._eyes = 2
        self.__speak = sound

	# Setters
    def setLegs(self, noOfLegs):
        self.__legs = noOfLegs
    def setEyes(self, noOfEyes):
        self._eyes = noOfEyes
    def setEars(self, noOfEars):
        self.ears = noOfEars
    def setColor(self, color):
        self.color = color
    def setSpeak(self, sound):
        self.__speak = sound

	# Getters
    def getLegs(self):
        return self.__legs
    def getEyes(self):
        return self._eyes
    def getEars(self):
        return self.ears
    def getColor(self):
        return self.color
    def getSpeak(self):
        return self.__speak



class Dog:
    def __init__(self, sound = None):

		#Public Variables
        self.ears = 2   
        self.color = "Brown"

		#Private Variables
        self.__speak = sound		
        self.__legs = 4 
        self._eyes = 2

	# Setters
    def setLegs(self, noOfLegs):
        self.__legs = noOfLegs
    def setEyes(self, noOfEyes):
        self._eyes = noOfEyes
    def setEars(self, noOfEars):
        self.ears = noOfEars
    def setColor(self, color):
        self.color = color
    def setSpeak(self, sound):
        self.__speak = sound


	# Getters
    def getLegs(self):
        return self.__legs
    def getEyes(self):
        return self._eyes
    def getEars(self):
        return self.ears
    def getColor(self):
        return self.color
    def getSpeak(self):
        return self.__speak



class Lion:
	def __init__(self, sound = None):
		super().__init__()
		self.__legs = 4
		self._eyes = 2
		self.ears = 2
		self.color = "Crimson" 
		self.__speak = sound
	def setLegs(self, noOfLegs):
		self.__legs = noOfLegs
	def setEyes(self, noOfEyes):
		self._eyes = noOfEyes
	def setSpeak(self, sound):
		self.__speak = sound
	def setColor(self, color):
		self.color = color
	def setEars(self, noOfEars):
		self.ears = noOfEars
	def getLegs(self):
		return self.__legs
	def getEyes(self):
		return self._eyes
	def getSpeak(self):
		return self.__speak
	def getColor(self):
		return self.color
	def getEars(self):
		return self.ears





class Sheep:
	def __init__(self, sound = None):
		self.__legs = 4
		self._eyes = 2
		self.ears = 2
		self.color = "Black"
		self.__speak = sound
	def setLegs(self, noOfLegs):
		self.__legs = noOfLegs
	def setEyes(self, noOfEyes):
		self._eyes = noOfEyes
	def setEars(self, noOfEars):
		self.ears = noOfEars
	def setColor(self, color):
		self.color = color
	def setSpeak(self, sound):
		self.__speak = sound
	def getLegs(self):
		return self.__legs
	def getEyes(self):
		return self._eyes
	def getEars(self):
		return self.ears
	def getColor(self):
		return self.color
	def getSpeak(self):
		return self.__speak

class Goat:
	def __init__(self, sound = None):
		self.__legs = 4
		self._eyes = 2
		self.ears = 2
		self.color = "Black"
		self.__speak = sound
	def setLegs(self, noOfLegs):
		self.__legs = noOfLegs
	def setEyes(self, noOfEyes):
		self._eyes = noOfEyes
	def setEars(self, noOfEars):
		self.ears = noOfEars
	def setColor(self, color):
		self.color = color
	def setSpeak(self, sound):
		self.__speak = sound
	def getLegs(self):
		return self.__legs
	def getEyes(self):
		return self._eyes
	def getEars(self):
		return self.ears
	def getColor(self):
		return self.color
	def getSpeak(self):
		return self.__speak


class Tiger:
	def __init__(self, sound = None):
		super().__init__()
		self.__legs = 4
		self._eyes = 2
		self.ears = 2
		self.color = "Brown-Striped" 
		self.__speak = sound
	def setLegs(self, noOfLegs):
		self.__legs = noOfLegs
	def setEyes(self, noOfEyes):
		self._eyes = noOfEyes
	def setSpeak(self, sound):
		self.__speak = sound
	def setColor(self, color):
		self.color = color
	def setEars(self, noOfEars):
		self.ears = noOfEars
	def getLegs(self):
		return self.__legs
	def getEyes(self):
		return self._eyes
	def getSpeak(self):
		return self.__speak
	def getColor(self):
		return self.color
	def getEars(self):
		return self.ears


class Rabbit:
	def __init__(self, sound = None):
		super().__init__()
		self.__legs = 4
		self._eyes = 2
		self.ears = 2
		self.color = "White" 
		self.__speak = sound
	def setLegs(self, noOfLegs):
		self.__legs = noOfLegs
	def setEyes(self, noOfEyes):
		self._eyes = noOfEyes
	def setSpeak(self, sound):
		self.__speak = sound
	def setColor(self, color):
		self.color = color
	def setEars(self, noOfEars):
		self.ears = noOfEars
	def getLegs(self):
		return self.__legs
	def getEyes(self):
		return self._eyes
	def getSpeak(self):
		return self.__speak
	def getColor(self):
		return self.color
	def getEars(self):
		return self.ears

class Elephant:
	def __init__(self, sound = None):
		super().__init__()
		self.__legs = 4
		self._eyes = 2
		self.ears = 2
		self.color = "Grey" 
		self.__speak = sound
	def setLegs(self, noOfLegs):
		self.__legs = noOfLegs
	def setEyes(self, noOfEyes):
		self._eyes = noOfEyes
	def setSpeak(self, sound):
		self.__speak = sound
	def setColor(self, color):
		self.color = color
	def setEars(self, noOfEars):
		self.ears = noOfEars
	def getLegs(self):
		return self.__legs
	def getEyes(self):
		return self._eyes
	def getSpeak(self):
		return self.__speak
	def getColor(self):
		return self.color
	def getEars(self):
		return self.ears


class Donkey:
	def __init__(self, sound = None):
		self.__legs = 4
		self._eyes = 2
		self.ears = 2
		self.color = "Black"
		self.__speak = sound
	def setLegs(self, noOfLegs):
		self.__legs = noOfLegs
	def setEyes(self, noOfEyes):
		self._eyes = noOfEyes
	def setEars(self, noOfEars):
		self.ears = noOfEars
	def setColor(self, color):
		self.color = color
	def setSpeak(self, sound):
		self.__speak = sound
	def getLegs(self):
		return self.__legs
	def getEyes(self):
		return self._eyes
	def getEars(self):
		return self.ears
	def getColor(self):
		return self.color
	def getSpeak(self):
		return self.__speak

class Bear:
	def __init__(self, sound = None):
		super().__init__()
		self.__legs = 4
		self._eyes = 2
		self.ears = 2
		self.color = "Brown" 
		self.__speak = sound
	def setLegs(self, noOfLegs):
		self.__legs = noOfLegs
	def setEyes(self, noOfEyes):
		self._eyes = noOfEyes
	def setSpeak(self, sound):
		self.__speak = sound
	def setColor(self, color):
		self.color = color
	def setEars(self, noOfEars):
		self.ears = noOfEars
	def getLegs(self):
		return self.__legs
	def getEyes(self):
		return self._eyes
	def getSpeak(self):
		return self.__speak
	def getColor(self):
		return self.color
	def getEars(self):
		return self.ears


