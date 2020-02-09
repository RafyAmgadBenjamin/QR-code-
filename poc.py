import csv
import pandas as pd
import datetime

# English names col in original sheet
original_names_index = 1
# TODO Need to get the last week in dynamic way.
original_new_week_name = "Week 1"
original_new_time_name = "Time 1"
# The time here is 24 hours formatted example "19:49:47"
session_start_time = "19:49:47"

new_attendance_names = []
data = None


def cal_late_time(base_time, attendee_time):
    attendee_time_only = datetime.datetime.strptime(
        attendee_time, "%Y.%m.%d  %X"
    ).time()
    base_time_only = datetime.datetime.strptime(base_time, "%X").time()
    attendee_min = attendee_time_only.minute
    attendee_hour = attendee_time_only.hour
    base_time_min = base_time_only.minute
    base_time_hour = base_time_only.hour
    if base_time_min <= attendee_min and base_time_hour <= attendee_hour:
        diff_min = attendee_min - base_time_min
        diff_hour = attendee_hour - base_time_hour
    else:
        diff_min = 0
        diff_hour = 0
    return diff_hour * 60 + diff_min


def read_original_sheet_panda(new_attendance_time):
    data = pd.read_csv("/home/rafy/Downloads/POC QR code/names.csv")
    for index, row in data.iterrows():
        index_attendee = check_name_exists(
            row[original_names_index], new_attendance_names
        )
        if index_attendee != -1:
            # adding present attendace
            data.loc[index, original_new_week_name] = "\u2713"
            # adding late time
            data.loc[index, original_new_time_name] = new_attendance_time[
                index_attendee
            ]
        else:
            # adding absent attendace
            data.loc[index, original_new_week_name] = "\u2715"
            data.loc[index, original_new_time_name] = "\u2715"
    return data


def read_new_attendance_sheet():
    new_attendance_late_time = []
    # English names col in attendance sheet
    new_attendance_names_index = 0
    new_attendance_data_time = 1

    with open("/home/rafy/Downloads/POC QR code/attendance1.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
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
                # Getting the new attendance time into list
                date_time = row[new_attendance_data_time]
                # TODO Handle the base time to be set in a better way
                new_attendance_late_time.append(
                    cal_late_time(session_start_time, date_time)
                )
                line_count += 1
        print(f"Processed {line_count} lines.")
        return new_attendance_late_time


def check_name_exists(original_name, new_attendance_names):
    original_name = original_name.lower()
    original_name = original_name.strip()

    # if (original_name in new_attendance_names):
    #     return True
    for index, name in enumerate(new_attendance_names):
        if name == original_name:
            # present
            return index
    return -1  # absent


# print("new attendance names list:")
# print(new_attendance_names)


def write_panda_csv(new_sheet):
    export_csv = new_sheet.to_csv(
        "/home/rafy/Downloads/POC QR code/names.csv", index=None, header=True
    )


new_attendance_time = read_new_attendance_sheet()
print("panda")
data = read_original_sheet_panda(new_attendance_time)
print(data)
write_panda_csv(data)
print("DONE.................")
