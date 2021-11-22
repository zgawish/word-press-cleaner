import os
import json

f = open('words_dictionary.json')
# returns JSON object as
# a dictionary
WORDS = json.load(f)
# import enchant
f.close()



def find_last(file):
    for i in range(len(file) - 1, -1, -1):
        if file[i] == ".":
            return i
    return -1


def is_mumbo(filename):
    pass


def is_valid(filename):
    if len(filename) == 0:
        print("Empty file name")
        return False
    if filename.lower() in WORDS:
        return True
    else:
        dash_parts = filename.split('-')
        under_parts = filename.split('_')
        dot_parts = filename.split('.')
        
        if len(dash_parts) > 1:
            for part in dash_parts:
                if part.lower() in WORDS:
                    return True
        
        if len(under_parts) > 1:
            for part in under_parts:
                if part.lower() in WORDS:
                    return True
        
        if len(dot_parts) > 1:
            for part in dot_parts:
                if part.lower() in WORDS:
                    return True
        
        return False

def main():
    directory = input("Enter a Directory: ")
    if len(directory) == 0:
        directory = "./"

    for root, subdirectories, files in os.walk(directory):
        # for subdirectory in subdirectories:
        #     print(os.path.join(root, subdirectory))
        for file in files:
            dot_index = find_last(file)
            filename = file
            file_type = ""
            if dot_index > 0:
                filename = file[:dot_index]
                file_type = file[dot_index:]

            print(file_type)
            if is_valid(filename) is False and file_type == ".php":
                print("Would you want to delete: {}? [y/n]".format(os.path.join(root, file)))
                if (input() == "y"):
                    print("Deleted: {}".format(file))
                    os.remove(os.path.join(root, file))
            # filename = file.split('.')[0]
            
            # print(os.path.join(root, file))

if __name__ == "__main__":
    main()