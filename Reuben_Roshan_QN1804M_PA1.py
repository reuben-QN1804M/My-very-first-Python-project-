import glob , win32api

class CalUtils():

	def __init__(self):
		#Indivial
		self.name = ""
		self.heights = 0
		#summary
		self.totalStudentHeight = 0
		self.totalStudentCount = 0
		self.total_height = 0
		#location 
		self.location = []

	def calAvgHeight(self):

		# Show list of drives
		drives_list = win32api.GetLogicalDriveStrings().split("\000")[:-1]

		#locating the "listOfStudentHeight.txt" in Drives
		for drive in drives_list:
			location = glob.glob(pathname=f"{drive}**\\listOfStudentHeight.txt",recursive= True)
			
		
		# If no files end program
		if len(location) == 0:
			print("No Files found")
			exit()

		# If multiple files found
		elif len(location) > 1:
			print(f"multiple files found\nLocation-> {location}")
			exit()

		else:
			print(f"File found -> {location[0]}\n\n")
			self.location = location
			self.reading_and_listing()


	def reading_and_listing(self):


		#Opening file as read
		with open(self.location[0] , "r") as file:
			#spliting each user information
			content = file.read().split("\n")
		

		#Spliting each line data to 2 parts in a list
		for user in content:
			user_list = user.split("\t")
			self.totalStudentCount += 1
			self.total_height += float(user_list[1])
		


		#round total hight to 2.d.p
		self.totalStudentHeight = round(self.total_height / self.totalStudentCount , 2)


		#Prints required data
		print("\n")
		print("#"*50)
		print(f"\n\n\nThere are {self.totalStudentCount} students and thier average height is {self.totalStudentHeight} Meter.\n\n\n")
		print("#"*50)
		


		#Auditing the File

		continuing = str(input("\n\nDo you want to write additional information?\nType in Y for yes and N for no:   ").upper())

		while continuing == "Y":

			#gathering DATA
			try:
				self.name = str(input("What's your student name?"))
				self.heights = float(input(f"What's the {self.name} height? (in Meter)"))
			except:
				print("\n\nInvalid name or height \n\n\n EXITING!")
				exit()


			#Putting it in file
			with open(self.location[0] , "a") as file:

				file.write(f"\n{self.name}\t{self.heights}")
			self.totalStudentHeight = 0
			self.totalStudentCount = 0
			self.total_height = 0

			#for repeating
			self.reading_and_listing()

		else:
			print("\n\nExiting")
			exit()







try:
    index = CalUtils()
    index.calAvgHeight()
except:
    print("Error")
    exit()
