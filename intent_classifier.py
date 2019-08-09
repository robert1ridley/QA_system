import random
import jieba.posseg as pseg

def load_data(filename):
    text_file = open(filename)
    lines = text_file.readlines()
    data = []
    for line in lines:
        data.append(line)
    random.shuffle(data)
    return data


def split_data(data):
    training_data = data[:4000]
    dev_data = data[4000:5000]
    test_data = data[5000:6300]
    return training_data, dev_data, test_data


def get_labels(data):
    x_data, y_data = [], []
    for item in data:
        item = item.strip()
        splits = item.split()
        x = splits[0]
        y = splits[1]
        x_data.append(x.strip())
        y_data.append(y.strip())
    return x_data, y_data


def generate_vocabulary(data):
    vocabulary_dict = {'<unk>': 0}
    index = len(vocabulary_dict)
    for sentence in data:
        words = pseg.cut(sentence)
        for word, flag in words:
            if word not in vocabulary_dict.keys():
                vocabulary_dict[word] = index
                index += 1
    return vocabulary_dict


def indicize_data(vocab_dict, data):
    all_indices = []
    max_sent = -1
    for sentence in data:
        sentence_indices = []
        words = pseg.cut(sentence)
        word_count = 0
        for word, flag in words:
            if word not in vocab_dict.keys():
                word = '<unk>'
            sentence_indices.append(vocab_dict[word])
            word_count += 1
        all_indices.append(sentence_indices)
        sent_length = word_count
        if sent_length > max_sent:
            max_sent = sent_length
    return all_indices, max_sent


if __name__ == '__main__':
    filename = 'data/training.txt'
    all_data = load_data(filename)
    train, dev, test = split_data(all_data)
    x_train, y_train = get_labels(train)
    x_dev, y_dev = get_labels(dev)
    x_test, y_test = get_labels(test)
    voc_dict = generate_vocabulary(train)
    x_train, max_train_sentence = indicize_data(voc_dict, x_train)
    x_dev, max_dev_sentence = indicize_data(voc_dict, x_dev)
    x_test, max_test_sentence = indicize_data(voc_dict, x_test)
    max_sentence = max(max_train_sentence, max_dev_sentence, max_test_sentence)
    


