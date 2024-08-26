import json
import os
import os.path
from pathlib import Path

INPUT_FOLDER = "./data/inputs"
OUTPUT_FOLDER = "./data/outputs"

def get_data():
    if(not os.path.exists(INPUT_FOLDER)): return
     
    onlyfiles = [f for f in os.listdir(INPUT_FOLDER) if os.path.isfile(os.path.join(INPUT_FOLDER, f))]

    if(len(onlyfiles) == 1):
        read_file = open(INPUT_FOLDER + "/" + onlyfiles[0], "r")
        data = read_file.read()
        read_file.close()
    return data


def compute_average(data):
    if (data):
        json_data = json.loads(data)
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