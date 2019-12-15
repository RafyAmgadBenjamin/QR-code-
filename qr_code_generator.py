import qrcode
import csv

def read_sheet_names():
    names_index =1
    names = []
    with open('/home/rafy/Downloads/POC QR code/names.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                print(row[names_index])
                # Getting the new attendance names into list
                name = row[names_index].lower()
                names.append(name.strip())
                line_count += 1
        print(f'Processed {line_count} lines.')
    return names

def qr_code_generator(name):
    qr = qrcode.QRCode()
    qr.add_data(name)
    qr.make()
    img = qr.make_image()
    img.save('/home/rafy/Downloads/POC QR code/codes_generatged/{}.png'.format(name))


names = read_sheet_names()
for name in names:
    qr_code_generator(name)

print("QR codes are ready")