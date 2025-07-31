# Converter for CSV to MySQL
Converting CSV file into MySQL syntaxes for importing purposes.

# Prequisite
- Python 3.9.0
- pandas  1.5.3
- CSV file's name **MUST** be the same as your DB's table name.

# How to use
1. Copy the code of `CSV2MySQL.py`
2. Create new .py file
3. Open a terminal
4. Run the Python script using `py CSV2MySQL.py`
    - Note: Make sure your terminal is at the same directory as the python script.
5. When the system asked for path input, enter the directory path towards your CSVs folder.
    - Example: C\\Desktop\\Some DB CSV folder\\table_name.csv
5. The script will create `output` folder with table name's.txt containing MySQL syntax.