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

# Define connection string (replace with your database filename if different)
conn = sqlite3.connect('mydatabase.sqlite')
cursor = conn.cursor()

# Initialize Faker
fake = Faker()


