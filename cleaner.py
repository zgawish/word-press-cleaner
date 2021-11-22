import os
import enchant

def find_last(file):
    for i in range(len(file) - 1, -1, -1):
        if file[i] == ".":
            return i
    return -1

def is_valid(filename):
    d = enchant.Dict("en_US") 
    if d.check(filename) is True:
        return True
    else:
        dash_parts = filename.split('-')
        under_parts = filename.split('_')
        dot_parts = filename.split('.')
        
        if len(dash_parts) > 0:
            for part in dash_parts:
                if d.check(part) is True:
                    return True
        
        if len(under_parts) > 0:
            for part in under_parts:
                if d.check(part) is True:
                    return True
        
        if len(dot_parts) > 0:
            for part in dot_parts:
                if d.check(part) is True:
                    return True
        
        return False

def main():
    directory = "./"

    for root, subdirectories, files in os.walk(directory):
        # for subdirectory in subdirectories:
        #     print(os.path.join(root, subdirectory))
        for file in files:
            dot_index = find_last(file)
            filename = file
            if dot_index > 0:
                filename = file[:dot_index]

            if is_valid(filename) is False:
                print("Would you want to delete: {}? [y/n]".format(filename))
                if (input() == "y"):
                    print("Deleted: {}".format(file))
                    os.remove(os.path.join(root, file))
            # filename = file.split('.')[0]
            
            # print(os.path.join(root, file))

if __name__ == "__main__":
    main()