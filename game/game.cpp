#include <iostream>
#include <string>
using namespace std;

void intro() {
	string name;
	cout << "What is your name: ";
	getline(cin, name);
	cout << "Welcome to the game "<< name<< endl 
		<< "You have 3 options to defeat the villian stalking you and to keep fighting: Attack, Heal or Run"<<endl
		<<"You choose to attack, you loose health points."<< endl<< "You choose to run, game ends."<< endl
		<<"You choose to heal, you restore some of your health points to fight again."<<endl<<endl
		<<"Things to note: "<<endl<<"10 total Health points."<<endl<<"1 Heal opportunity."<<endl<<"GOODLUCK!"<<endl;
}

/*i want to do a class that would have the players and the computers actions like choices, health, heal*/
class player {
public:
	char choice;
	int health;
	int heal;
};

class villain {
public:
	char choice;
	int health;
	int heal;
};

int main() {
	intro();
	return 0;
}