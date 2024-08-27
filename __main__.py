import json
import os
import os.path
from pathlib import Path

INPUT_FOLDER = "./data/inputs/ea6890f851252e0646ab4887c40603182e42ab684f597f5731f02cfe9efe5be0"
OUTPUT_FOLDER = "./data/outputs"

def get_data():
    if(not os.path.exists(INPUT_FOLDER)): return
     
    onlyfiles = [f for f in os.listdir(INPUT_FOLDER) if os.path.isfile(os.path.join(INPUT_FOLDER, f))]
    print("os.listdir(): ")
    for entry in os.listdir(INPUT_FOLDER):
        print(entry)
        if os.path.isdir(os.path.join(INPUT_FOLDER, entry)):
            for entry1 in os.listdir(INPUT_FOLDER + entry):
                print(" --  " + entry1)
                if os.path.isdir(os.path.join(INPUT_FOLDER, entry)):
                    for entry2 in os.listdir(INPUT_FOLDER + entry2):
                        print("  ----  " + entry2)
                read_file = open(INPUT_FOLDER + "/" + entry + "/" + entry1 , "r")
                print(read_file.read())
        read_file = open(INPUT_FOLDER + "/" + entry , "r")
        print(read_file.read())    



    match len(onlyfiles):
        case 0:
            print("keine Dateien gefunden")
        case 1: 
            if(onlyfiles[0].__contains__('.json')):
                with open(INPUT_FOLDER + "/" + onlyfiles[0]) as file:
                    data = json.load(file)
                    print("Found exactly 1 File: " + onlyfiles[0])
                    print("It's a json file. Data = " + str(data))
                    print("file contains this: ")
                read_file = open(INPUT_FOLDER + "/" + onlyfiles[0], "r")
                print(read_file.read())
            else:
                read_file = open(INPUT_FOLDER + "/" + onlyfiles[0], "r")
                data = read_file.read()
                read_file.close()
                print("Found exactly 1 File: " + onlyfiles[0] + ". Data = " + data)
        case _:
            read_file = open('/data/inputs/algoCustomData.json', "r")
            data = read_file.read()
            read_file.close()
            print("Found " + len(onlyfiles) + " Files. Data = " + data)



    return data


def compute_average(data):
    if (data and len(data)):
        if(type(data) == type(str)):
            json_data = json.loads(data)
        else: json_data = data
        length = 0
        avg = 0
        for point in json_data:
            length += 1
            avg += int(point['value'])

        avg = avg / length
        write_file = open(OUTPUT_FOLDER + "/result", 'w')
        write_file.write("{avg: " + str(avg) + "}")
        write_file.close()
    return


if __name__ == '__main__':
    compute_average(get_data())