import csv
import pandas as pd

#English names col in original sheet
original_names_index = 1
# TODO Need to get the last week in dynamic way.
original_new_week_name = "Week 3"
#English names col in attendance sheet
new_attendance_names_index = 0
new_attendance_names = []
data = None

def read_original_sheet_panda():
    data = pd.read_csv("/home/rafy/Downloads/POC QR code/names.csv")
    for index, row in data.iterrows():
        if check_name_exists(row[original_names_index],new_attendance_names):
            data.loc[index,original_new_week_name] = 1
        else :
            data.loc[index,original_new_week_name] = 0
    return data

def read_new_attendance_sheet():
    with open('/home/rafy/Downloads/POC QR code/attendance1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                print(row[new_attendance_names_index])
                # Getting the new attendance names into list
                name = row[new_attendance_names_index].lower()
                new_attendance_names.append(name.strip())
                line_count += 1
        print(f'Processed {line_count} lines.')



def check_name_exists(original_name,new_attendance_names):
    original_name = original_name.lower()
    original_name = original_name.strip()

    if (original_name in new_attendance_names):
        return True
    return False


read_new_attendance_sheet()

# print("new attendance names list:")
# print(new_attendance_names)

def write_panda_csv(new_sheet):
    export_csv = new_sheet.to_csv ("/home/rafy/Downloads/POC QR code/names.csv", index = None, header=True)


print("panda")
data = read_original_sheet_panda()
print(data)
write_panda_csv(data)
print("DONE.................")