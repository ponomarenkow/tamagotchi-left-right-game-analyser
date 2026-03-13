
def save(combinations, path, current_character):

    file_path = path + current_character + ".txt"
    
    stringified = []
    for i in range(0, len(combinations)):
        stringified.append(str(combinations[i]))
        
    try:
        save_file = open(file_path, 'w')
        try:
            save_file.write(",".join(stringified))
            print("Saved!")
        except:
            print("An error occured while attemtipng to write the save. Please copy the string below and put it in the '" + path + current_character + ".txt' file")
            print(",".join(stringified))
        finally:
            save_file.close()
    except:
        print("Failed to load the save file. You may copy the string below and put it in the '" + path + current_character + ".txt' file")
        print(",".join(stringified))

def read_save(path, current_character):
    
    file_path = path + current_character + ".txt"
    
    combinations = []
    try:
        save_file = open(file_path)
        try:
            file_input = save_file.read()
            if file_input != '':
                combinations = file_input.split(',')
            else:
                combinations = []
        except:
            print("An error occured while trying to read from the save file.")
        finally:
            save_file.close()
    except:
        print("Failed to load the save file. Make sure the file " + current_character + ".txt is in the '" + path + "' path, relative to main program's folder.")
        if path != "":
            print("If the file is present, check if '" + path + "' is a valid and existing path - note that it should end with '/'.")

    try:
        for i in range(0, len(combinations)):
            combinations[i] = int(combinations[i])
            if combinations[i] < 0 or combinations[i] > 31:
                print("An error occured while trying to encode the save file. Make sure it doesn't contain any numbers outside of the 0-31 range.")
                return
    except:
        print("An error occured while trying to encode the save file. Make sure it contains only numbers separated with commas.")
        return

    return combinations
