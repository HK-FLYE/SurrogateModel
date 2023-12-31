#include <fstream>
#include <string>
#include <vector>
#include <iostream>
using std::vector, std::string, std::ifstream, std::cout, std::endl;

bool getStringLines (string FileName, vector<string> &lines)
{
    ifstream file (FileName.c_str(), ifstream::in);
    if (file.is_open()) {
        cout << "Open File Successfull" << endl;
        string line;
        while (std::getline(file, line)) {
            lines.push_back(line);
        }
    } else {
        cout << "Failed to open " << FileName << endl;
        getchar();
        return false;
    }
    getchar();
    return true;
}

void parceLineIntoWords (string line, vector<string> &words, char delimiter = ' ')
{
    if (words.empty()) {
        return;
    }
    int cur = 0;
    string word;
    while (cur < line.length()) {
        if (line[cur] == ' ' || line[cur] == '\t' || line[cur] == delimiter) {
            words.emplace_back(word);
            cur++;
            word = "";
        } else {
            word += line[cur];
            cur++;
        }
    }
    words.emplace_back(word);
}


