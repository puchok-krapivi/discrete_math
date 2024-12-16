#include<iostream>
#include <string>
#include <vector>
#include <random>
using namespace std;

vector<string> new_variables(vector<string> old_variables)
{
	vector <string> new_variables;

	for (int i = 0; i < old_variables.size(); i++)
	{
		for (int j = i + 1; j < old_variables.size(); j++)
		{
			string s = old_variables[i];
			int delete_index;
			int count = 0;
			for (int index = 0; index < min(old_variables[i].size(), old_variables[j].size()); index++)
			{
				if (old_variables[j].find(old_variables[i][index]) == string::npos)
				{
					delete_index = index;
					count++;
				}
			}
			if (count == 1)
			{
				if (s[delete_index] == 'X' && old_variables[j].find('x') != string::npos)
				{
					s.erase(delete_index, 1);
					new_variables.push_back(s);
				}
				else if (s[delete_index] == 'Y' && old_variables[j].find('y') != string::npos)
				{
					s.erase(delete_index, 1);
					new_variables.push_back(s);
				}
				else if (s[delete_index] == 'Z' && old_variables[j].find('z') != string::npos)
				{
					s.erase(delete_index, 1);
					new_variables.push_back(s);
				}
				else if (s[delete_index] == 'W' && old_variables[j].find('w') != string::npos)
				{
					s.erase(delete_index, 1);
					new_variables.push_back(s);
				}
			}
		}
	}
	return new_variables;
}

bool check_mdnf(vector<vector<string>> implicate_table, string mdnf, string check, string answer)
{
	for (int j = 0; j < implicate_table.size(); j++)
	{
		if (mdnf.find(implicate_table[j][0]) != string::npos)
		{
			for (int i = 1; i < implicate_table[0].size(); i++)
			{
				if (implicate_table[j][i] == "1   ")
				{
					check[i - 1] = '+';
				}
			}
		}
	}
	if (check == answer)
		return 1;
	else
		return 0;
}

int main()
{
	setlocale(LC_ALL, "rus");
	vector < vector <bool> > bool_table(16, vector <bool>(5));
	int i = 0, j = 0;
	for (int x = 0; x < 2; x++)
	{
		for (int y = 0; y < 2; y++)
		{
			for (int z = 0; z < 2; z++)
			{
				for (int w = 0; w < 2; w++)
				{
					bool_table[i][j] = x;
					bool_table[i][j + 1] = y;
					bool_table[i][j + 2] = z;
					bool_table[i][j + 3] = w;
					i++;
				}
			}
		}
	}
	string Vector_func = "";
	cout << "Вектор функции - ";
	cin >> Vector_func;

	for (int i = 0; i < 16; i++)
	{
		if (Vector_func[i] == '0')
			bool_table[i][4] = false;
		else
			bool_table[i][4] = true;
	}
	cout << "Таблица истиности:" << endl;
	cout << "X Y Z W f" << endl;
	for (int i = 0; i < 16; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			cout << bool_table[i][j] << " ";
		}
		cout << endl;
	}
	vector <string> sdnf;
	string s = "";
	for (int i = 0; i < 16; i++)
	{
		s = "";
		if (bool_table[i][4])
		{
			if (bool_table[i][0]) s += "x";
			else s += "X";

			if (bool_table[i][1]) s += "y";
			else s += "Y";

			if (bool_table[i][2]) s += "z";
			else s += "Z";

			if (bool_table[i][3]) s += "w";
			else s += "W";

			sdnf.push_back(s);
		}
	}
	cout << endl;
	cout << "----------------------------------------------" << endl;
	cout << "СДНФ: ";
	for (int i = 0; i < sdnf.size(); i++)
	{
		cout << sdnf[i];
		if (i != sdnf.size() - 1)
			cout << " v ";
	}
	cout << endl;
	cout << "----------------------------------------------" << endl;

	vector <string> variables = sdnf;
	vector <string> using_variables = sdnf;

	while (variables.size() > 1)
	{
		variables = new_variables(variables);
		for (int i = 0; i < variables.size(); i++)
		{
			using_variables.push_back(variables[i]);
		}
	}

	variables.clear();
	variables.push_back(using_variables[using_variables.size() - 1]);
	for (int i = using_variables.size() - 1; i > -1; i--)
	{
		int v_count = 0;
		for (int j = 0; j < variables.size(); j++)
		{
			int count = 0;
			for (int index = 0; index < min(using_variables[i].size(), variables[j].size()); index++)
			{
				if (using_variables[i].find(variables[j][index]) != string::npos)
				{
					count++;
				}
			}
			if (count == variables[j].size())
			{
				v_count++;
			}
		}
		if (v_count == 0)
		{
			variables.push_back(using_variables[i]);
		}
	}

	while (using_variables[using_variables.size() - 1].size() < 4)
	{
		using_variables.pop_back();
	}

	vector < vector <string> > table(variables.size() + 1, vector <string>(using_variables.size() + 1));

	for (int i = 1; i < using_variables.size() + 1; i++)
	{
		table[0][i] = using_variables[i - 1];
	}
	for (int i = 1; i < variables.size() + 1; i++)
	{
		table[i][0] = variables[i - 1];
	}

	for (int i = 1; i < table.size(); i++)
	{
		for (int j = 1; j < table[0].size(); j++)
		{
			int t = 0;
			for (int k = 0; k < table[i][0].size(); k++)
			{
				if (table[0][j].find(table[i][0][k]) != -1)
				{
					t++;
				}
			}
			if (t == table[i][0].size())
			{
				table[i][j] = "1   ";
			}
		}
	}

	cout << "Импликантная матрица:" << endl;
	for (int i = 0; i < table.size(); i++)
	{
		for (int j = 0; j < table[0].size(); j++)
		{
			for (int k = 0; k < 4 - table[i][j].size(); k++)
			{
				cout << " ";
			}
			cout << table[i][j] << " ";
		}
		cout << endl;
	}
	vector<string> table_tmp;
	string string_mdnf;
	int mdnf_len = 0;
	string check = "", answer = "";
	for (int i = 0; i < table[0].size() - 1; i++)
	{
		check += "-";
		answer += "+";
	}

	int n = table.size() - 1;
	vector<vector<int> > all_combinations(n, vector<int>(1 << n));

	unsigned num_to_fill = 1U << (n - 1);
	for (unsigned col = 0; col < n; ++col, num_to_fill >>= 1U)
	{
		for (unsigned row = num_to_fill; row < (1U << n); row += (num_to_fill * 2))
		{
			fill_n(&all_combinations[col][row], num_to_fill, 1);
		}
	}
	int mdnf_len_min = 1000;
	string mdnf_min;
	for (unsigned x = 0; x < (1 << n); ++x)
	{
		for (unsigned y = 0; y < n; ++y)
		{
			if (all_combinations[y][x])
			{
				string_mdnf = string_mdnf + table[y + 1][0] + " v ";
			}
		}
		unsigned index;
		if (check_mdnf(table, string_mdnf, check, answer))
		{
			if (string_mdnf.size() != 0)
			{
				string_mdnf.pop_back();
				string_mdnf.pop_back();
			}
			if (string_mdnf.size() < mdnf_len_min)
			{
				mdnf_len_min = string_mdnf.size();
				mdnf_min = string_mdnf;
			}
		}
		string_mdnf = "";
	}

	cout << "----------------------------------------------" << endl;
	cout << "МДНФ: " << mdnf_min << endl;
	cout << "----------------------------------------------" << endl;

}