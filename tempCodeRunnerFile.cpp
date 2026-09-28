#include <iostream>
#include <string>
using namespace std;

struct PersonalDetails
{
    string name;
    string father_name;
    string mobile_no;

  
    struct Address
    {
        string colony;
        string name;
        string area;
        string district;
    };

    Address address;
};

int main()
{
    int n;

    cout << "Enter number of persons: ";
    cin >> n;

  
    PersonalDetails p[n];

     
    for (int i = 0; i < n; i++)
    {
        cout << "\n===== Enter Details of Person " << i + 1 << " =====\n";

        cout << "Enter Name: ";
        cin >> p[i].name;

        cout << "Enter Father Name: ";
        cin >> p[i].father_name;

        cout << "Enter Mobile No: ";
        cin >> p[i].mobile_no;

        cout << "\n--- Address ---\n";

        cout << "Enter Colony: ";
        cin >> p[i].address.colony;

        cout << "Enter House Name: ";
        cin >> p[i].address.name;

        cout << "Enter Area: ";
        cin >> p[i].address.area;

        cout << "Enter District: ";
        cin >> p[i].address.district;
    }

    // Display using loop
    cout << "\n\n========== ALL DETAILS ==========\n";

    for (int i = 0; i < n; i++)
    {
        cout << "\n===== Person " << i + 1 << " =====\n";

        cout << "Name        : " << p[i].name << endl;
        cout << "Father Name : " << p[i].father_name << endl;
        cout << "Mobile No   : " << p[i].mobile_no << endl;

        cout << "Colony      : " << p[i].address.colony << endl;
        cout << "House Name  : " << p[i].address.name << endl;
        cout << "Area        : " << p[i].address.area << endl;
        cout << "District    : " << p[i].address.district << endl;
    }

    return 0;
}