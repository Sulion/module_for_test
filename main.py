import os
import json

# objects description


class JLPTTest():

    def __init__(self, TestType):
        self.TestType = TestType


class JLPTQuestion():
    #def __init__(self, ID, ListOfTest, AnswersNum, QuestionText, ):
    pass


class JLPTAnswer():
    pass


def json_files_list():
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    test = []
    i = 0
    while (i < len(files)):
        if ".json" in files[i]:
            test.append(files[i])
        i += 1
    return test


def get_test_type(TestFileName):
    with open(TestFileName) as data_file:
        data = json.load(data_file)
    return data["type"]


def get_test_name(TestFileName):
    with open(TestFileName) as data_file:
        data = json.load(data_file)
    return data["name"]

def get_test_question(TestFileName):
    with open(TestFileName) as data_file:
        data = json.load(data_file)
    return data["questions"][0]

all_type_list = []
counter = 0
while (counter < len(json_files_list())):
    a = json_files_list()[counter]
    all_type_list.append(get_test_type(a))
    counter += 1

# external services

# console work
print("You can choose between: {}".format(all_type_list))
line = input("Input your test type:")

# work logic
if line == "full":
    print("You choose {}".format(get_test_name(json_files_list()[0])))
    print(get_test_question(json_files_list()[0]))
elif line == "N2":
    print("You choose {}".format(get_test_name(json_files_list()[1])))
elif line == "N5":
    print("You choose {}".format(get_test_name(json_files_list()[2])))

print("Prepare for battle")

input()