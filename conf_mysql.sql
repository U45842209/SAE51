-- Create a database
CREATE DATABASE IF NOT EXISTS SAE51;
USE SAE51;

CREATE TABLE Computers (
    computer_id INT AUTO_INCREMENT PRIMARY KEY,
    vendor_name VARCHAR(60),
    operating_system VARCHAR(255),
    cpu_family VARCHAR(40),
    ram_amount INT,
    bought_in INT
);

CREATE TABLE Software (
    software_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    version VARCHAR(50),
    license VARCHAR(255)
);

CREATE TABLE ComputerSoftware (
    computer_id INT,
    software_id INT,
    installation_date DATE,
    PRIMARY KEY (computer_id, software_id),
    FOREIGN KEY (computer_id) REFERENCES Computers(computer_id),
    FOREIGN KEY (software_id) REFERENCES Software(software_id)
);

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE ComputerUser (
    computer_id INT,
    user_id INT,
    assignment_date DATE,
    PRIMARY KEY (computer_id, user_id),
    FOREIGN KEY (computer_id) REFERENCES Computers(computer_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Maintenance (
    maintenance_id INT AUTO_INCREMENT PRIMARY KEY,
    computer_id INT,
    maintenance_date DATE,
    actions_taken TEXT,
    FOREIGN KEY (computer_id) REFERENCES Computers(computer_id)
);
