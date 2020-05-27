from PIL import Image
import os
import datetime

datetime_object = datetime.datetime.now()
currentDateTime = datetime_object.strftime("%d-%m-%Y - %H-%M-%S")

ext = [".jpeg", ".jpg", ".jpe", ".jfif"]

for filename in os.listdir(os.getcwd()):
    if filename.endswith(tuple(ext)):
        if not os.path.exists(currentDateTime):
            os.mkdir(currentDateTime)
        break
    else:
        continue
    
for filename in os.listdir(os.getcwd()):
    if filename.endswith(tuple(ext)):
        newFileName = os.path.splitext(filename)[0]
        im = Image.open(filename)
        im.save(currentDateTime + '//' + newFileName + '.png')
        print(os.path.join(os.getcwd(), filename))
        continue
    else:
        continue
        
for filename in os.listdir(os.getcwd()):
    if filename.endswith(tuple(ext)):
        print('All JPEG to PNG Converted')
        break
    else:
        print('No File Here')
        break