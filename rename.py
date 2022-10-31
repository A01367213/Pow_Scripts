import os

print("Insert a '\\' at the end of the path")
folder = input("Insert Path:") #Variable where folder path will be stored
new_name = input("Name to be replaced: ") #Stores the new name for archives

#Retrive the archive names inside a folder
file_name = os.listdir(folder)

#Counters for name
count_img = 1
count_vid = 1


for i in range(len(file_name)):
    name_aux = file_name[i].split('.')

    if name_aux[1] == 'jpg':
        try: 
            original_file = folder + file_name[i]
            new_file = folder + new_name + '_IMG' + ('0' * (2 - len(str(count_img)))) + str(count_img) +  '.jpg'
            os.rename(original_file, new_file)
            count_img += 1

        except:
            print('jeje, no')
    
    if name_aux[1] == 'mp4':
        try: 
            original_file = folder + file_name[i]
            new_file = folder + new_name + '_VID' + ('0' * (2 - len(str(count_vid)))) + str(count_vid) + '.mp4'
            os.rename(original_file, new_file)
            count_vid += 1
        except:
            print('jeje, no')


print(file_name)
