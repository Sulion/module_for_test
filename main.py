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

    def set_correct(self, correct):
        self.correct = correct

    def iscorrect(self, test_file_name, question_num, answer_num):
        if take_data_from_json(test_file_name)["questions"][question_num]["answers"][answer_num]["correct"] == "true":
            return 1
        else:
            return 0


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
    right_answers_counter = 0
    while(question_num < test.get_total_question(test_file_name)):
        question = JLPTQuestion()
        question.set_question_num(question_num)
        test.set_current_question(question_num)
        print(question.get_question_text(test_file_name))
        answer_num = 0
        answer = JLPTAnswer()
        while(answer_num < test.total_answers):
            answer.set_answer_text(test_file_name, question_num, answer_num)
            print("{}) ".format(answer_num + 1) + answer.get_answer_text(test_file_name, question_num, answer_num))
            answer_num = answer_num + 1
        print("Choose correct answer")
        choosing_answer = int(input())
        answer.set_correct(answer.iscorrect(test_file_name, question_num, choosing_answer - 1))
        print(answer.correct)
        right_answers_counter = right_answers_counter + answer.iscorrect(test_file_name, question_num, choosing_answer - 1)
        print(right_answers_counter)
        question_num = question_num + 1
    return right_answers_counter

def get_test_result(test_file_name, right_answers_counter):
    return (right_answers_counter)/(TestCondition().get_total_question(test_file_name))


if __name__ == "__main__":
    #file initialization
    file = json_files_list()

    #test initialization
    test = JLPTTest()
    test.set_test_name(file[0])
    test.set_test_type(file[0])
    a = question_dialog(file[0])
    print("Your result is: {}".format(get_test_result(file[0], a)))