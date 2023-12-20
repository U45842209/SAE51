import mysql.connector
import csv
import io
from mysql.connector import errorcode

class MYSQL:
    def __init__(self):
        self.cnx = None

    def connect_to_db(self):
        try:
            cnx = mysql.connector.connect(user='root', password='aae@aQBB7LQG6&F8', host='172.36.30.2', database='SAE_51_1')
            self.cnx = cnx
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def close_connection_to_db(self):
        if self.cnx and self.cnx.is_connected():
            self.cnx.close()

    def testing(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()
            cursor.execute("SHOW TABLES;")
            results = cursor.fetchall()
            for row in results:
                table_name = row[0].decode('utf-8')  # Decode the bytearray to a string
                print(table_name)

    def injector_Computers(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()

            with open("../sql_data/Computers.csv", "r") as CSV:
                csv_data = csv.reader(io.StringIO(CSV.read()))
                x = True
                for row in csv_data:
                    if x:
                        x = False
                    else:
                        cursor.execute(f"INSERT INTO Computers (vendor_name, operating_system, cpu_family, ram_amount, bought_in) VALUES (%s, %s, %s, %s, %s);", row)

            self.cnx.commit()

    def injector_Users(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()

            with open("../sql_data/Users.csv", "r") as CSV:
                csv_data = csv.reader(io.StringIO(CSV.read()))
                x = True
                for row in csv_data:
                    if x:
                        x = False
                    else:
                        cursor.execute(f"INSERT INTO Users (name) VALUES (%s);", row)

            self.cnx.commit()

    def injector_Software(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()

            with open("../sql_data/Software.csv", "r") as CSV:
                csv_data = csv.reader(io.StringIO(CSV.read()))
                x = True
                for row in csv_data:
                    if x:
                        x = False
                    else:
                        cursor.execute(f"INSERT INTO Software (name, version, license) VALUES (%s, %s, %s);", row)

            self.cnx.commit()

    def injector_ComputerSoftware(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()

            with open("../sql_data/ComputerSoftware.csv", "r") as CSV:
                csv_data = csv.reader(io.StringIO(CSV.read()))
                x = True
                for row in csv_data:
                    if x:
                        x = False
                    else:
                        cursor.execute(f"INSERT INTO ComputerSoftware (computer_id, software_id, installation_date) VALUES (%s, %s, %s);", row)

            self.cnx.commit()

    def injector_ComputerUser(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()

            with open("../sql_data/ComputerUser.csv", "r") as CSV:
                csv_data = csv.reader(io.StringIO(CSV.read()))
                x = True
                for row in csv_data:
                    if x:
                        x = False
                    else:
                        cursor.execute(f"INSERT INTO ComputerUser (computer_id, user_id, assignment_date) VALUES (%s, %s, %s);", row)

            self.cnx.commit()

    def injector_Maintenance(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()

            with open("../sql_data/Maintenance.csv", "r") as CSV:
                csv_data = csv.reader(io.StringIO(CSV.read()))
                x = True
                for row in csv_data:
                    if x:
                        x = False
                    else:
                        cursor.execute(f"INSERT INTO Maintenance (computer_id, maintenance_date, actions_taken) VALUES (%s, %s, %s);", row)

            self.cnx.commit()

    def injector_master(self):
        self.injector_Users()
        self.injector_Software()
        self.injector_Computers()
        self.injector_ComputerUser()
        self.injector_ComputerSoftware()
        self.injector_Maintenance()




db = MYSQL()
db.connect_to_db()
db.injector_master()
db.close_connection_to_db()