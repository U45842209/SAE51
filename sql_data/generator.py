import csv
import random
from faker import Faker

fake = Faker()

# Generate larger test data for Computers
computers_data = []
for i in range(1, 31):
    computers_data.append([
        fake.random_element(elements=('HP','Dell','Acer','Lenovo')),
        fake.random_element(elements=('Windows 10', 'Windows 7', 'Ubuntu', 'macOS')),
        fake.random_element(elements=('Intel i7', 'Intel i5', 'AMD Ryzen 5')),
        random.randint(4, 32),  # RAM amount (between 4 and 32 GB)
        random.randint(2008, 2023)  # Bought year
    ])

with open('Computers.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['vendor_name', 'operating_system', 'cpu_family', 'ram_amount', 'bought_in'])
    csvwriter.writerows(computers_data)

def generate_software_name():
    words = ['Microsoft Office', 'Adobe Photoshop', 'Google Chrome', 'Mozilla Firefox', 'Adobe Illustrator', 'AutoCAD', 'Microsoft Word', 'Excel', 'PowerPoint', 'Visual Studio', 'Eclipse', 'PyCharm', 'Android Studio', 'Unity', 'Photoscape']
    return random.choice(words)

# Generate larger test data for Software
software_data = []
for i in range(1, 31):
    software_data.append([
        generate_software_name(),
        fake.random_element(elements=('2018', '2019', '2020', '2021', '2022')),
        fake.random_element(elements=('Commercial', 'Free'))
    ])

with open('Software.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['name', 'version', 'license'])
    csvwriter.writerows(software_data)

# Generate larger test data for ComputerSoftware
computer_software_data = []
for i in range(1, 31):
    computer_software_data.append([
        random.randint(1, 30),  # computer_id (between 1 and 30)
        random.randint(1, 30),  # software_id (between 1 and 30)
        fake.date_of_birth(minimum_age=1, maximum_age=5).strftime('%Y-%m-%d')  # Installation date in the last 5 years
    ])

with open('ComputerSoftware.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['computer_id', 'software_id', 'installation_date'])
    csvwriter.writerows(computer_software_data)

# Generate larger test data for Users
users_data = []
for i in range(1, 31):
    users_data.append([fake.name()])

with open('Users.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['name'])
    csvwriter.writerows(users_data)

# Generate larger test data for ComputerUser
computer_user_data = []
for i in range(1, 31):
    computer_user_data.append([
        random.randint(1, 30),  # computer_id (between 1 and 30)
        random.randint(1, 30),  # user_id (between 1 and 30)
        fake.date_of_birth(minimum_age=1, maximum_age=5).strftime('%Y-%m-%d')  # Assignment date in the last 5 years
    ])

with open('ComputerUser.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['computer_id', 'user_id', 'assignment_date'])
    csvwriter.writerows(computer_user_data)

# Generate larger test data for Maintenance
maintenance_data = []
for i in range(1, 31):
    maintenance_data.append([
        random.randint(1, 30),  # computer_id (between 1 and 30)
        fake.date_of_birth(minimum_age=1, maximum_age=5).strftime('%Y-%m-%d'),  # Maintenance date in the last 5 years
        fake.sentence()
    ])

with open('Maintenance.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['computer_id', 'maintenance_date', 'actions_taken'])
    csvwriter.writerows(maintenance_data)