import sys 
import clipboard
import json
#key : --
Saved_data  = 'Clipboard.json'

#save data the json file, If data is not present add it
def Save(filepath,data):
    with open(filepath,'w') as f:
        json.dump(data, f)

def Load(filepath):
    try:
        with open(filepath,'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = Load(Saved_data)

    if command == 'Save':
        key  = input("Enter a key: ")
        data[key] = clipboard.paste()
        Save(Saved_data, data)
        print('Data Saved!')

    elif command == "Load":
        key = input('Enter key: ')
        if key in data:
                clipboard.copy(data[key])
        else:
            print('Key does not exist')
    
    elif command == "Change":
        key = input('Enter previous key: ')
        change = input("Enter the new key: ")
        data[change] = data[key]
        del data[key]
        Save(Saved_data, data)

    elif command == "List":
        print(data)
    else:
        print("Unknown Error ")
else:
    print("Input Error")