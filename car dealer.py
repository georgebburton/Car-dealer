# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 14:26:32 2026

@author: georg
"""
#imports and sets up the sql connection
import mysql.connector

conn = mysql.connector.connect(host = "localhost", user="root", password="Turtles4321!", database="cars")
cursor = conn.cursor()

#creates a class car to make it easier to store cars by using objects
class Car:
    #initializes the attributes
    def __init__(self, year, make, model, stock):
        self._year = year
        self._make = make
        self._model = model
        self._stock = stock
        
    #sets up the get functions
    def get_year(self):
        return self._year
    def get_make(self):
        return self._make
    def get_model(self):
        return self._model
    def get_stock(self):
        return self._stock
    
    #sets up the set functions
    def set_year(self, year):
        self._year = year
    def set_make(self, make):
        self._make = make
    def set_model(self, model):
        self._model = model
    def set_stock(self, stock):
        self._stock = stock
        
    #sets up the str functionn so when printed it is tidy
    def __str__(self):
        return f'{self._year} {self._make} {self._model}'
    
#sets up the main function 
def main():
    
    #main loop
    while True:
        
        #inputs for the vehicles
        year = str(input("input car's year or enter to exit: "))
        if not year:
            break
        make = str(input("input car's make: "))
        model = str(input("input car's model: "))
        stock = int(input("input stock amount: "))
        
        # creates the car object
        car = Car(year, make, model, stock)
        
        #connects to an SQL Database and stores the car input after all loop iterations
        sql = "INSERT INTO car (year, make, model, stock) VALUES (%s, %s, %s, %s)"
        val = (car.get_year(), car.get_make(), car.get_model(), car.get_stock())
        cursor.execute(sql, val)
        conn.commit()
        
    #gets the inventory list from the database
    cursor.execute("select * from car;")
    cars = cursor.fetchall()
    
    #prints the stock from the database tidy
    for i in cars:
        print(f"Year: {i[1]}, Make: {i[2]}, Model: {i[3]}, Stock: {i[4]}")

#calls the function
main()