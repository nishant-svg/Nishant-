#include <iostream>
#include <fstream>
#include <string>

using namespace std;

struct Car 
{
    string licensePlate;
    string brand;
    string model;
};
void addCar() 
{
    ofstream file("parking_lot.txt", ios::app);
    
    Car newCar;
    cout << "Enter license plate: ";
    cin >> newCar.licensePlate;
    cout << "Enter brand: ";
    cin >> newCar.brand;
    cout << "Enter model: ";
    cin >> newCar.model;
    
    file << newCar.licensePlate << " " << newCar.brand << " " << newCar.model << endl;
    
    file.close();
    cout << "Car parked successfully!" << endl;
}
void removeCar() 
{
    ifstream file("parking_lot.txt");
    ofstream temp("temp.txt");
    
    string licensePlate;
    cout << "Enter the license plate of the car to be removed: ";
    cin >> licensePlate;
    
    string line;
    bool found = false;
    while (getline(file, line)) {
        string storedLicensePlate = line.substr(0, line.find(' '));
        if (storedLicensePlate != licensePlate) 
        {
            temp << line << endl;
        } 
        else 
        {
            found = true;
        }
    }
    
    file.close();
    temp.close();
    
    remove("parking_lot.txt");
    rename("temp.txt", "parking_lot.txt");
    
    if (found) 
    {
        cout << "Car removed successfully!" << endl;
    } else {
        cout << "Car not found in the parking lot!" << endl;
    }
}
void displayCars() 
{
    ifstream file("parking_lot.txt");
    
    string line;
    cout << "Cars parked in the parking lot:" << endl;
    while (getline(file, line)) 
    {
        cout << line << endl;
    }
    
    file.close();
}

int main() 
{
    int choice;
    while (true) 
    {
        cout << "Car Parking Management System" << endl;
        cout << "1. Park a car" << endl;
        cout << "2. Remove a car" << endl;
        cout << "3. Display parked cars" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        
        switch (choice) 
        {
            case 1:
                addCar();
                break;
            case 2:
                removeCar();
                break;
            case 3:
                displayCars();
                break;
            case 4:
                cout << "Exiting the program." << endl;
                return 0;
            default:
                cout << "Invalid choice! Please try again." << endl;
        }
        
        cout << endl;
    }
    
    return 0;
}
