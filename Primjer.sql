CREATE DATABASE primjer;
USE primjer;

CREATE TABLE korisnici (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ime VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);