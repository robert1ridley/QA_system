import jieba.posseg as pseg

class QuestionParser:
    def __init__(self):
        self.keywords_dict = {}


    def read_keywords(self):
        with open("keywords.txt", "r") as keywords:
            lines = keywords.readlines()
            for line in lines:
                splits = line.split("\t")
                word = splits[0]
                word_type = splits[1]
                self.keywords_dict[word] = word_type

    def find_keywords_in_text(self, sentence):
        for word in self.keywords_dict.keys():
            if word in sentence:
                print(word)

if __name__ == '__main__':
    question_parser = QuestionParser()
    question_parser.read_keywords()
    sentence = "一意孤行袁术篡逆称帝涉及多少人物？"
    question_parser.find_keywords_in_text(sentence)
    words = pseg.cut(sentence)
    # for word, flag in words:
    #     print('%s %s' % (word, flag))

