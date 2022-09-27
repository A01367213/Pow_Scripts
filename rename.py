import os


iso_8 = 'ISO-8'
iso_9 = 'ISO-9'

folder = r'D:\Operator_Day\21-09-2022_OD\\' + iso_9 + '\\'

archive_name = os.listdir(folder)

count_img = 1
count_vid = 1


for i in range(len(archive_name)):
    name_aux = archive_name[i].split('.')

    if name_aux[1] == 'jpg':
        try: 
            original_file = folder + archive_name[i]
            new_file = folder + iso_9 + '_IMG' + ('0' * (2 - len(str(count_img)))) + str(count_img) +  '.jpg'
            os.rename(original_file, new_file)
            count_img += 1

        except:
            print('jeje, no')
    
    if name_aux[1] == 'mp4':
        try: 
            original_file = folder + archive_name[i]
            new_file = folder + iso_9 + '_VID' + ('0' * (2 - len(str(count_vid)))) + str(count_vid) + '.mp4'
            os.rename(original_file, new_file)
            count_vid += 1
        except:
            print('jeje, no')


print(archive_name)