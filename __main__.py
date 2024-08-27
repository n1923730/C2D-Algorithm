import json
import os
import os.path
from pathlib import Path

INPUT_FOLDER = "./data/inputs"
OUTPUT_FOLDER = "./data/outputs"

def get_data():
    if(not os.path.exists(INPUT_FOLDER)): return
     
    onlyfiles = [f for f in os.listdir(INPUT_FOLDER) if os.path.isfile(os.path.join(INPUT_FOLDER, f))]
    print(len(onlyfiles))

    match len(onlyfiles):
        case 0:
            print("keine Dateien gefunden")
        case 1: 
            if(onlyfiles[0].__contains__('.json')):
                with open(INPUT_FOLDER + "/" + onlyfiles[0]) as file:
                    data = json.load(file)
                    print("Found exactly 1 File: " + onlyfiles[0])
                    print("It's a json file. Data = " + str(data))
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