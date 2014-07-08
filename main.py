import os
import json


class JLPTTest():

    def __init__(self):
        self.name = None
        self.type = None

    def set_test_name(self, test_file_name):
        self.name = take_data_from_json(test_file_name)["name"]

    def set_test_type(self, test_file_name):
        self.type = take_data_from_json(test_file_name)["type"]

    def get_test_name(self, test_file_name):
        return take_data_from_json(test_file_name)["name"]

    def get_test_type(self, test_file_name):
        return take_data_from_json(test_file_name)["type"]


class JLPTQuestion():

    def __init__(self):
        self.text = ""
        self.question_num = 0

    def set_question_num(self, question_num):
        self.question_num = question_num

    def get_question_num(self):
        return self.question_num

    def set_question_text(self, test_file_name):
        self.text = take_data_from_json(test_file_name)["questions"][self.question_num]["text"]

    def get_question_text(self, test_file_name):
        return take_data_from_json(test_file_name)["questions"][self.question_num]["text"]


class JLPTAnswer():

    def __init__(self):
        self.text = ""
        self.correct = False

    def set_answer_text(self, test_file_name, question_num):
        data = take_data_from_json(test_file_name)
        i = 0
        while (i<len(data["questions"][question_num]["answers"])):
            self.text = data["questions"][question_num]["answers"][i]["answer"]
            i += 1

    def get_answer_text(self, test_file_name, question_num):
        data = take_data_from_json(test_file_name)
        i = 0
        a = []
        while (i<len(data["questions"][question_num]["answers"])):
            a.append(data["questions"][question_num]["answers"][i]["answer"])
            i += 1
        return a


# static methods
def json_files_list():
    """Return all file names into current directory"""
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    test = []
    i = 0
    while (i < len(files)):
        if ".json" in files[i]:
            test.append(files[i])
        i += 1
    return test


def take_data_from_json(test_file_name):
    with open(test_file_name) as data_file:
        return json.load(data_file)





















right_answer_counter = 0

def isRightAnsw(TestFileName, question_num, answer):
    global right_answer_counter
    with open(TestFileName) as data_file:
        data = json.load(data_file)
    i = 0
    while (i<len(data["questions"][question_num]["answers"])):
        if data["questions"][question_num]["answers"][i]["isright"] == "true":
            right_answer = data["questions"][question_num]["answers"][i]["answer"]
            if right_answer == answer:
                right_answer_counter = right_answer_counter + 1
        i += 1

# all_type_list = []
# counter = 0
# while (counter < len(json_files_list())):
#     a = json_files_list()[counter]
#     all_type_list.append(get_test_type(a))
#     counter += 1

# # console work
# print("You can choose between: {}".format(all_type_list))
# line = input("Input your test type:")
#
# # work logic
# if line == "full":
#     print("You choose {}".format(get_test_name(json_files_list()[0])))
#     print(get_text_question(json_files_list()[0], 0))
#     print(get_test_answers(json_files_list()[0], 0))
#     answer = input("Answer: ")
#     isRightAnsw(json_files_list()[0], 0, answer)
#     print(right_answer_counter)
#     print()
# elif line == "N2":
#     print("You choose {}".format(get_test_name(json_files_list()[1])))
# elif line == "N5":
#     print("You choose {}".format(get_test_name(json_files_list()[2])))
#
# print("Prepare for battle")
#
#
# input()


if __name__ == "__main__":
    file = json_files_list()
    a = JLPTTest()
    b = JLPTQuestion()
    c = JLPTAnswer()
    a.set_test_name(file[0])
    b.set_question_num(0)
    b.set_question_text(file[0])
    c.set_answer_text(file[0], 0)
    print(c.get_answer_text(file[0], 0))