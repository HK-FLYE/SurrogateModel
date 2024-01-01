#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <utility>
using std::vector, std::string, std::ifstream, std::cout, std::endl, std::unordered_map, std::pair;

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
// combine hash calculation of the members
struct HashFunc
{
    template<typename T, typename U>
    size_t operator() (const pair<T, U> &p) const {
        return std::hash<T>()(p.first) ^ std::hash<U>()(p.second);
    }
};
// compare keys when hash collision 
struct Equalkey {
    template<typename T, typename U>
    bool operator () (const pair<T, U> &p1, const pair<T, U> &p2) const {
        return p1.first == p2.first && p1.second == p2.second;
    }
};

// a function to extract surface triangles from given meshed
void extractSurfaceTriangles (vector<vector<string>> &meshes, vector<int> &SurfaceNodes, vector<vector<int>> &SurfaceTriangles) 
{
    unordered_map<pair<int, int>, int, HashFunc, Equalkey> record;
    int cur = 0;
    while (cur < meshes.size()) {
        for (int i = 0; i < meshes[cur].size() - 1; ++i) {
            int first = std::atoi(meshes[cur][i].c_str());
            for (int j = i + 1; j < meshes[cur].size(); ++j) {
                int second = std::atoi(meshes[cur][j].c_str());
                if (first > second) {
                    first = second;
                    second = std::atoi(meshes[cur][i].c_str());
                }
                pair<int, int> tmp = std::make_pair(first, second);
                if (record.count(tmp) != 0) {
                    record[tmp] += 1;
                } else {
                    record[tmp] = 1;
                }
            }
        }
    }

}