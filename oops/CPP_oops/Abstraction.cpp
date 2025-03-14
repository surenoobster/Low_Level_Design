#include <iostream>
using namespace std;

// Abstract class
class Vehicle {
protected:
    string brand;
public:
    Vehicle(string b) : brand(b) {}
    virtual void start() = 0; // Pure virtual function  @abstractmethod hota h python mei 
    void displayBrand() {
        cout << "Brand: " << brand << endl;
    }
};

// Subclass implementing the abstract method
class Car : public Vehicle {
public:
    Car(string b) : Vehicle(b) {}
    void start() override {
        cout << "Car is starting..." << endl;
    }
};

int main() {
    Vehicle* myCar = new Car("Toyota");  //dynamic memory 
    
    myCar->displayBrand();
    myCar->start();
    delete myCar;
    return 0;
}