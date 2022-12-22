#include <iostream>

using namespace std;

int pierw, drug, trze;

int main(){
    cout << "Podaj trzy liczby rozdzielone spacja : "; 
    cin >> pierw >> drug >> trze;

    if((pierw>drug) && (pierw>trze)){
        cout << pierw;
    }

    if((pierw<drug) && (drug>trze)){
        cout << drug;
    }

    if((trze>pierw) && (trze>drug)){
        cout << trze;
    }

    return 0;
}
