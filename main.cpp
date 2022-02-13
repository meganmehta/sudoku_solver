#include <iostream>
#include <vector>
#include <stack>
#include <fstream>
using namespace std;

vector<int> CSP(int row, int col, int puzzle[9][9]){
    vector<int> domain; //{1, 2, 3, 4, 5, 6, 7, 8, 9};
    vector <int>:: iterator it;
    vector<int>:: iterator it2;
    vector<int> existingNums; // stores the numbers that are found in the current row, col
    for (int j = 1; j < 10; j++){
        domain.push_back(j); // first start with everything in the domain
    }
    for (int i = 0; i < 9; i++){
        if (puzzle[row][i] != 0){ // checks the row horitzontally 
            cout << "this value was found in the current row: " << puzzle[row][i] << endl;
            existingNums.push_back(puzzle[row][i]);
        }
        if (puzzle[i][col] != 0){ // checks the column vertically 
            cout << "this value was found in the current column: " << puzzle[i][col] << endl;
            existingNums.push_back(puzzle[i][col]);
        }
    }
    for (it = existingNums.begin(); it < existingNums.end(); it++){
        for (it2 = domain.begin(); it2 < domain.end(); it2++){
            if (*it == *it2){
                domain.erase(it2);
            }
        }
    }

    for (it2 = domain.begin(); it2 < domain.end(); it2++){
        cout << *it2 << " ";
    }
    return domain;
}

int main(){
    int puzzle[9][9]; // 2D array to store the game
    string userInput; 
    string output;
    int countRow = 0;
    int countCol = 0;

    // accept user input in the form of a matrix
    getline(cin, userInput); 
    ifstream fileStream(userInput);
    if (fileStream.is_open()){
        while (getline(fileStream, output)){
            //cout << output << endl; 
            for (int i = 0; i < output.length()-1; i++){
                //cout << output[i];
                if (output[i] == '|' && output[i+1] == '|'){
                    puzzle[countRow][countCol] = 0;
                    countCol++;
                }
                else if (output[i] == '|' && output[i+1] != '|'){
                    continue;
                }
                else{
                    puzzle[countRow][countCol] = output[i] - '0';
                    countCol++;
                }
                if (countCol == 9){
                    countRow++;
                    countCol = 0;
                }
            }
        }
    }
  
    cout << endl;
    for (int i = 0 ; i < 9; i++){
        for (int j = 0; j < 9; j++){
            cout << " " << puzzle[i][j] << " ";
        }
        cout << endl;
    }
    CSP(0, 1, puzzle);
}