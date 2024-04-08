import pandas as pd
import os

folder_path = r'C:\Users\Admin\Desktop\json_to_excel'

def read_json_files(folder_path):
    all_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = pd.read_json(file)
                data['File id'] = os.path.splitext(filename)[0] 
                all_data.append(data)
    if all_data:
        return pd.concat(all_data, ignore_index=True)
    else:
        return None

json_data = read_json_files(folder_path)

if json_data is not None:
    # Write DataFrame to Excel
    excel_file = r'C:\Users\Admin\Desktop\json_to_excel\json_to_excel_file.xlsx'
    json_data.to_excel(excel_file, index=False)
    print(f'Successfully converted JSON files to Excel: {excel_file}')
else:
    print('No JSON files found in the folder.')
