#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

vector<int> CSP(int row, int col, int puzzle[9][9]){
    vector<int> domain;
    vector<int> existingNums; // stores the numbers that are found in the current row, col
    vector <int>:: iterator it; // to iterate through existingNums 
    vector<int>:: iterator it2; // to iterate through domain
    int boxX = col/3; // box horizontal
    int boxY = row/3; // box vertical 
    // check the box numbers
    for (int i = boxY*3; i < (boxY*3)+3; i++){
        for (int j = boxX*3; j < (boxX*3)+3; j++){
            if (puzzle[j][i] != 0){
                //cout << puzzle[j][i] << " ";
                existingNums.push_back(puzzle[j][i]);
            }
        }
    }
    for (int j = 1; j < 10; j++){
        domain.push_back(j); // first start with everything in the domain
    }
    for (int i = 0; i < 9; i++){
        if (puzzle[row][i] != 0){ // checks the row horitzontally 
            existingNums.push_back(puzzle[row][i]);
        }
        if (puzzle[i][col] != 0){ // checks the column vertically 
            existingNums.push_back(puzzle[i][col]);
        }
    }
    for (it = existingNums.begin(); it < existingNums.end(); it++){
        for (it2 = domain.begin(); it2 < domain.end(); it2++){
            if (*it == *it2){
                domain.erase(it2); // removes the numbers from domain that already exist in row or col
            }
        }
    }
    // prints out the values left in the domain for the current empty space 
    /*for (it2 = domain.begin(); it2 < domain.end(); it2++){
        cout << *it2 << " ";
    }*/
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
            for (int i = 0; i < output.length()-1; i++){
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
    // prints out the initial puzzle 
    /*for (int i = 0 ; i < 9; i++){
        for (int j = 0; j < 9; j++){
            cout << " " << puzzle[i][j] << " ";
        }
        cout << endl;
    }*/
    CSP(8, 7, puzzle);
}