import qrcode
import csv
from PIL import Image, ImageFont, ImageDraw

names_file_path = "/home/rafy/Documents/marriage_seminar/QR-code-/names.csv"
qrcode_path = "/home/rafy/Documents/marriage_seminar/QR-code-/codes_generatged"
generate_qrcodes_images_paths = []


def read_sheet_names():
    names_index = 1
    names = []
    # the path from which i read the names file
    with open(names_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
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
        print(f"Processed {line_count} lines.")
    return names


def qr_code_generator(name):
    qr = qrcode.QRCode()
    qr.add_data(name)
    qr.make()
    img = qr.make_image()
    img_path = f"{qrcode_path}/{name}.png"
    generate_qrcodes_images_paths.append(img_path)
    img.save(img_path)


def write_text_on_qrcode_image(img_path, text):
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    font_size = 15
    font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf", font_size)
    draw.text((0, 0), text, 0, font=font)
    img.save(img_path)


names = read_sheet_names()
for name in names:
    qr_code_generator(name)

print("QR codes have been generated successfully")

for i in range(len(names)):
    write_text_on_qrcode_image(img_path=generate_qrcodes_images_paths[i], text=names[i])

print("QR codes have been updated with names successfully")
