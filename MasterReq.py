import re
import matplotlib.pyplot as plt
import numpy as np

class NodeData(object):
    def __init__(self, key,count):
        self.key = key
        self.count = count

    def get_key(self):
        return self.key

    def increment_count(self):
        self.count += 1

    def get_count(self):
        return self.count

class Node(object):
    def __init__(self, node_data, next=None):
        self.node_data = node_data
        self.next = next

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def get_node_data(self):
        return self.node_data

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 1

    def append(self,node_data):
        if not self.head:
            self.head = Node(node_data)
            return
        curr = self.head
        while curr.get_next():
            curr = curr.get_next()
        curr.set_next(Node(node_data))

    def get_size(self):
        return self.size

    def get_head(self):
        return self.head

    def find_node_data(self,node_data_key):
        curr = self.head
        while curr and curr.get_node_data().get_key() != node_data_key:
            curr = curr.get_next()
        if curr:
            return curr.get_node_data()
        return None

    def __str__(self):
        curr = self.head
        str = ''
        while curr:
            str = "{} [{}, {}]".format(str,curr.get_node_data().get_key(),curr.get_node_data().get_count())
            curr = curr.get_next()
            if curr:
                str = '{} ->'.format(str)
        return str

# a hash with key = document number and value = linked list of all the word appearances
articles_words_hash = {}
current_doc = 0

with open("txt-for-assignment-data-science.txt") as f:
    for line in f.readlines():
        #clean the line
        line = line.replace('&amp;','').strip()
        # check if it is a Xml tag
        if re.match('<[^<]+>',line):
            if line.startswith('<doc>'):
                current_doc += 1
        else:
            words = line.lower().strip().split(' ')
            for word in words:
                #cleaning the words
                word = re.sub('[^A-Za-z0-9]+', '', word)
                if word:
                    words_list = articles_words_hash.get(word, LinkedList())
                    node_data = words_list.find_node_data(current_doc)
                    if node_data:
                        node_data.increment_count()
                    else:
                        words_list.append(NodeData(current_doc, 1))

                    articles_words_hash[word] = words_list

words_count_distribution = []

#Print the words and the associated documents
for doc_number,linked_list in articles_words_hash.items():
    print('[{}] ->{}'.format(doc_number,linked_list))

    curr = linked_list.get_head()
    while curr:
        words_count_distribution.append(curr.get_node_data().get_count())
        curr = curr.get_next()

bins = np.arange(max(words_count_distribution)) - 0.5
print (bins)
# plt.hist(words_count_distribution, bins, alpha=0.75, color='g', linewidth=0.75, edgecolor='black')
# plt.title("(b)")
# plt.xlabel("Total count of words")
# plt.ylabel("Frequency of total count")
# x1,x2,y1,y2 = plt.axis()
# plt.axis((1,21,y1,y2))
# plt.xticks(np.arange(1, 20, 2))
# plt.xlim([0.5, 20.5])
# frequency, bins = np.histogram(words_count_distribution, bins=20, range=[1, 25])
plt.hist(words_count_distribution, bins=bins, alpha=0.5, edgecolor='gray',  linewidth=1)
plt.xticks(range(1,25,2))
plt.show()