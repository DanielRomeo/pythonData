import sqlite3
import random
from faker import Faker

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
ballot_array = ["ANC", "MK", "DA", "IFP", "BOSA", "EFF", "VFF", "ACT", "COPE", "ALJAMA AH", "GOOD", "PAC", "UDM", "NFP"]
spread_sheet_cols = ["Firstname", "Lastaname", "Idnumber", "Ethnicity", "Province_address", "District_address", "National_vote", "Provincial_vote", "District_vote"]


from faker import Faker
import random

# Address dictionary
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

# Ballot dictionary
ballot_array = ["ANC", "MK", "DA", "IFP", "BOSA", "EFF", "VFF", "ACT", "COPE", "ALJAMA AH", "GOOD", "PAC", "UDM", "NFP"]

# Spread sheet columns
spread_sheet_cols = ["Firstname", "Lastaname", "Idnumber", "Ethnicity", "Province_address", "District_address", "National_vote", "Provincial_vote", "District_vote"]


class Voter(object):

	def __init__(self):
		# Initialize faker object
		self.faker = Faker()

		# Generate random data
		self.Firstname = self.faker.first_name()
		self.Lastaname = self.faker.last_name()
		self.Idnumber = self.generate_south_africa_id()
		self.Ethnicity = self.faker.ethnicity()
		self.Province_address = self.get_random_province()
		self.District_address = self.get_random_district(self.Province_address)
		self.National_vote = random.choice(ballot_array)
		self.Provincial_vote = random.choice(ballot_array)
		self.District_vote = random.choice(ballot_array)

	def generate_south_africa_id(self):
		""" Generates a random south african ID"""
		year = self.faker.random_int(min=24, max=99)  # Simulates birth year between 1924 and 1999
		month = self.faker.random_int(min=1, max=12)
		day = self.faker.random_int(min=1, max=28)  # Adjust for leap year if needed
		seq = self.faker.random_int(min=1000, max=9999)
		return f"{year:02d}{month:02d}{day:02d}{seq:04d}"

	def get_random_province(self):
		return random.choice(list(addresses_array.keys()))

	def get_random_district(self, province):
    	if province in addresses_array:
			return random.choice(addresses_array[province])
		else:
			return None  # Handle