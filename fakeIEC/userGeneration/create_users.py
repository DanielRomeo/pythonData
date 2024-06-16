import sqlite3
import random
from faker import Faker
from datetime import datetime, timedelta

addresses_array = {
    "Limpopo": ["Vhembe", "Mopani", "Capricorn", "Sekhukhune", "Waterburg"],
    "Kwa-zulu Natal": ["Amajuba", "Ilembe", "Sisonke", "Ugu", "uMkhanyakude", "uMgungundlovu", "uMzinyathi", "Uthukela", "Uthungulu", "Zululand"],
    "Gauteng": ["Sedibeng", "West rand", "Johannesburg",  "Tswane", "Ekurhuleni", "Metsweding"],
    "Free State": ["Fezile Dabi", "Lejweleputswa", "Thabo Mofutsanyana", "Xhariep"] ,
    "North West": ["Bojanala Platinum ", "Dr Kenneth Kaunda", "Dr Ruth Segomotsi Mompati", "Ngaka Modiri Molema"],
    "Northern Cape": ["Frances Baard", "John Taolo Gaetsewe", "Namakwa", "Pixley Ka Seme", "ZF Mgcawu"],
    "Mpumalanga": ["Ehlanzeni", "Gert Sibande", "Nkangala", ],
    "Eastern Cape": ["Buffalo City Metropolitan", "Nelson Mandela Bay Metropolitan", "Alfred Nzo", "Amathole", "Chris Hani", "Joe Gqabi", "OR Tambo", "Sarah Baartman"],
    "Western Cape": ["City of Cape Town Metropolitan", "Cape Winelands", "Central Karoo", "Garden Route", "Overberg", "West Coast"]
}
ballot_array = [ "ANC", "MK", "DA", "IFP", "BOSA", "EFF", "VFF", "ACT", "COPE", "ALJAMA AH", "GOOD", "PAC", "UDM", "NFP"]
spread_sheet_cols = ["Firstname", "Lastaname", "Idnumber", "Ethnicity", "Province_address", "District_address", "National_vote", "Provincial_vote", "District_vote"]
ethnicity = ["black", "indian", "coloured", "white"]


class Voter(object):

	def __init__(self):
		# Initialize faker object
		self.faker = Faker()

		# Generate random data
		self.Firstname = self.faker.first_name()
		self.Lastaname = self.faker.last_name()
		self.Idnumber = self.generate_south_africa_id()
		self.Ethnicity = random.choice(ethnicity)
		self.Province_address = self.get_random_province()
		self.District_address = self.get_random_district(self.Province_address)
		vote = self.generate_vote() # this will populate the users vote or None, if they havent voted

	def generate_vote(self):
		isVoting = [0, 1,2]
		choice = random.choice(isVoting)
		print("choice is : ",choice)
		if(choice == 1 or choice == 2):
			self.National_vote = random.choice(ballot_array)
			self.Provincial_vote = random.choice(ballot_array)
			self.District_vote = random.choice(ballot_array)
		elif(choice == 0):
			self.National_vote = None
			self.Provincial_vote = None
			self.District_vote = None


	def generate_south_africa_id(self, min_age=18, max_age=120):
		current_date = datetime.now()
		min_birth_date = current_date - timedelta(days=max_age * 365)
		max_birth_date = current_date - timedelta(days=min_age * 365)

		# Generate a random date between min_birth_date and max_birth_date
		random_days = random.randint(0, (max_birth_date - min_birth_date).days)
		dob = min_birth_date + timedelta(days=random_days)
		dob=  dob.strftime('%Y%m%d') # this is my date of birth
		dob_halved = dob[2:]

		# Generate a random list of 9 digits
		random_7_digits = ''.join([str(random.randint(0, 9)) for _ in range(7)])

		return dob_halved+random_7_digits
	

	def get_random_province(self):
		return random.choice(list(addresses_array.keys()))

	def get_random_district(self, province):
		if province in addresses_array:
			return random.choice(addresses_array[province])
		else:
			return None  # Handle
	
	def print_data(self):
		"""
		Prints all voter data in a formatted way.
		"""
		print(f"Firstname: {self.Firstname}")
		print(f"Lastname: {self.Lastaname}")
		print(f"ID Number: {self.Idnumber}")
		print(f"Ethnicity: {self.Ethnicity}")
		print(f"Province: {self.Province_address}")
		print(f"District: {self.District_address}")
		print(f"National Vote: {self.National_vote}")
		print(f"Provincial Vote: {self.Provincial_vote}")
		print(f"District Vote: {self.District_vote}")
		print("=" * 30)  # Add a separator for readability
		
Daniel = Voter()
Daniel.print_data()