import os
import json

class UserCondition():

    def __init__(self, Question_num, Test_result):
        self.Question_num = Question_num



class JLPTTest():



    def get_test_name(TestName):
        with open(TestName) as data_file:
            data = json.load(data_file)
        return data["name"]

class JLPTQuestion():
    #def __init__(self, ID, ListOfTest, AnswersNum, QuestionText, ):
    pass


class JLPTAnswer():
    pass


# realisacia
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

def get_text_question(TestFileName, question_num):
    with open(TestFileName) as data_file:
        data = json.load(data_file)
    return data["questions"][question_num]["text"]

def get_test_answers(TestFileName, question_num):
    with open(TestFileName) as data_file:
        data = json.load(data_file)
    i = 0
    a = []
    while (i<len(data["questions"][question_num]["answers"])):
        a.append(data["questions"][question_num]["answers"][i]["answer"])
        i += 1
    return a

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

all_type_list = []
counter = 0
while (counter < len(json_files_list())):
    a = json_files_list()[counter]
    all_type_list.append(get_test_type(a))
    counter += 1

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

    b = json_files_list()[0]
    # print(type(b))
    # a = JLPTTest().get_test_name(b)
    #print(a)
    print(get_test_name(b))