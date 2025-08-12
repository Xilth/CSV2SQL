import pandas as pd
import os
import re

class ConvertCSV2MySQL:
    def __init__(self, file_path_csv):
        self.header_line = ""
        self.file_path_csv = file_path_csv
        with open(self.file_path_csv, 'r', encoding='utf-8') as f:
            self.header_line = f.readline().strip()

    def get_file_name(self):
        return os.path.splitext(os.path.basename(self.file_path_csv))[0]
    
    def fix_csv_file(self):
        self.fixed_file_path_csv = f"{os.path.splitext(self.file_path_csv)[0]}_fixed.csv"
        open(self.fixed_file_path_csv, "w", encoding="utf-8").write(
            re.sub(r'\r?\n(?=\")', '', open(self.file_path_csv, encoding="utf-8").read())
        )
        self.csv_df = pd.read_csv(self.fixed_file_path_csv, sep=',', quotechar='"', skipinitialspace=True)
    
    def convert(self):
        os.makedirs('output', exist_ok=True)

        table_name = self.get_file_name()
        table_columns = []
        for col in self.header_line.split(','):
            cleaned_col = col.strip().strip('"')
            table_columns.append(cleaned_col)
            
        values_list = []
        for _, row in self.csv_df.iterrows():
            values = []
            for value in row:
                if pd.isna(value) or value == '':
                    values.append("NULL")
                elif isinstance(value, (int, float)):
                    integer_value = int(value) if value == int(value) else value
                    values.append(str(integer_value))
                else:
                    value_str = str(value).replace("'", "\\'")
                    values.append(f"'{value_str}'")
        
            columns_str = ', '.join(table_columns)
            values_str = f"({', '.join(values)})"
            values_list.append(values_str)
            
        group_values_str = ",\n".join(values_list)    
        mysql_strng = f"INSERT INTO {table_name} ({columns_str}) VALUES\n{group_values_str};"

        output_file_path = os.path.join('output', f"{table_name}.txt")
        with open(output_file_path, 'w', encoding='utf-8') as writeMySQL:
            writeMySQL.write(mysql_strng)

        print(f"MySQL syntax has been saved to {output_file_path}.")

if __name__ == "__main__":
    csv_path = input("Input your CSV file directory (full path):\n")
    cv2mysql = ConvertCSV2MySQL(csv_path)
    cv2mysql.fix_csv_file()
    cv2mysql.convert()
                