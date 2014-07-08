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

    def set_answer_text(self, test_file_name, question_num, answer_num):
        self.text = take_data_from_json(test_file_name)["questions"][question_num]["answers"][answer_num]["text"]

    def get_answer_text(self, test_file_name, question_num, answer_num):
        return take_data_from_json(test_file_name)["questions"][question_num]["answers"][answer_num]["text"]

    def iscorrect(self, test_file_name, question_num, answer_num):
        return take_data_from_json(test_file_name)["questions"][question_num]["answers"][answer_num]["correct"]

class TestCondition():

    def __init__(self):
        self.total_questions = 0
        self.total_answers = 4
        self.current_question = 0
        self.current_answer = 0

    def set_total_questions(self, total_questions):
        self.total_questions = total_questions

    def get_total_question(self, test_file_name):
        return len(take_data_from_json(test_file_name)["questions"])

    def set_total_answers(self, total_answers):
        self.total_answers = total_answers

    def set_current_question(self, current_question):
        self.current_question = current_question

    def get_current_question(self, test_file_name):
        return take_data_from_json(test_file_name)["questions"][self.current_question]

    def set_current_answer(self, current_answer):
        self.current_answer = current_answer

    def get_current_answer(self, test_file_name):
        return take_data_from_json(test_file_name)["questions"][self.current_answer]

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


def question_dialog(test_file_name):
    test = TestCondition()
    question_num = 0
    while(question_num < test.get_total_question(test_file_name)):
        test.set_current_question(question_num)
        print(test.get_current_question(test_file_name))
        question_num = question_num + 1

        answer_num = 0
        while(answer_num < test.total_answers):
            test.get_current_answer(test_file_name)
            print(test)
            answer_num = answer_num + 1



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
    #file initialization
    file = json_files_list()

    #test initialization
    test = JLPTTest()
    test.set_test_name(file[0])
    test.set_test_type(file[0])

    question_dialog(file[0])

