import mysql.connector
from mysql.connector import errorcode


class DATA_HOARDER:
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
                table_name = row[0]  # Decode the bytearray to a string
                print(table_name)

    def exo_1(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()
            cursor.execute("SELECT * FROM Computers WHERE vendor_name = 'HP';")
            results = cursor.fetchall()
            return results

    def exo_2(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()
            cursor.execute("SELECT * FROM Computers WHERE bought_in BETWEEN 2018 AND 2020;")
            results = cursor.fetchall()
            return results

    def exo_3(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()
            cursor.execute(
                "SELECT * FROM Computers WHERE vendor_name = 'Lenovo' AND bought_in BETWEEN 2019 AND 2020;")
            results = cursor.fetchall()
            return results

    def exo_4(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()
            cursor.execute("SELECT COUNT(*) FROM Computers WHERE vendor_name = 'Acer';")
            results = cursor.fetchall()
            return results

    def exo_5(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()
            cursor.execute("SELECT * FROM Computers WHERE ram_amount BETWEEN 4 AND 8;")
            results = cursor.fetchall()
            return results

    def exo_6(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()
            cursor.execute("""SELECT Software.* FROM Software
            JOIN ComputerSoftware ON Software.software_id = ComputerSoftware.software_id
            WHERE ComputerSoftware.computer_id = 4;""")
            results = cursor.fetchall()
            return results

    def exo_7(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()
            cursor.execute("""SELECT S.*
            FROM Software AS S
            JOIN ComputerSoftware AS CS ON S.software_id = CS.software_id
            JOIN ComputerUser AS CU ON CS.computer_id = CU.computer_id
            WHERE CU.user_id = (SELECT user_id FROM Users WHERE name = 'Sandra Davis');""")
            results = cursor.fetchall()
            return results

    def exo_8(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()
            cursor.execute("""SELECT Users.* FROM Users
            JOIN ComputerUser ON Users.user_id = ComputerUser.user_id
            JOIN Computers ON Computers.computer_id = ComputerUser.computer_id
            WHERE Computers.vendor_name = 'Dell';""")
            results = cursor.fetchall()
            return results

    def exo_9(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()
            cursor.execute("""SELECT Users.* FROM Users
            JOIN ComputerUser ON Users.user_id = ComputerUser.user_id
            JOIN Computers ON Computers.computer_id = ComputerUser.computer_id
            WHERE Computers.vendor_name = 'HP' AND Computers.operating_system = 'Windows 10';""")
            results = cursor.fetchall()
            return results

    def exo_10(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()
            cursor.execute(
                """SELECT * FROM Maintenance WHERE maintenance_date BETWEEN '2021-01-10' AND '2021-12-10';""")
            results = cursor.fetchall()
            return results

    def exo_11(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()
            cursor.execute("""SELECT Computers.* FROM Computers
            JOIN Maintenance ON Computers.computer_id = Maintenance.computer_id
            WHERE Maintenance.actions_taken = 'Turn thus pattern once.';""")
            results = cursor.fetchall()
            return results

    def exo_12(self):
        if self.cnx and self.cnx.is_connected():
            cursor = self.cnx.cursor()
            cursor.execute("""SELECT Computers.* FROM Computers
            JOIN Maintenance ON Computers.computer_id = Maintenance.computer_id
            WHERE Maintenance.actions_taken = 'Kind collection follow value.' AND YEAR(Maintenance.maintenance_date) = 2021;""")
            results = cursor.fetchall()
            return results


#db = DATA_HOARDER()
#db.connect_to_db()
#db.close_connection_to_db()