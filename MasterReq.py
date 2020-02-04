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

    def prepend(self, node_data):
        self.head = Node(node_data, self.head)
        self.size += 1

    def append(self,node_data):
        if not self.head:
            self.head = Node(node_data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.set_next(Node(node_data))

    def get_size(self):
        return self.size

    def get_head(self):
        return self.head

    def find_node_data(self,node_data_key):
        curr = self.head
        while curr and curr.get_node_data().get_key() != node_data_key:
            curr = curr.next
        if curr:
            return curr.get_node_data()
        return None

    def __str__(self):
        curr = self.head
        str = ''
        while curr:
            str = "{} [{}, {}]".format(str,curr.get_node_data().get_key(),curr.get_node_data().get_count())
            curr = curr.next
            if curr:
                str = '{} ->'.format(str)
        return str

# articles_sample_data = {1:'asdnjsadlkjfalkjdsflkjahsdlhflasdhfasdf',
#             2:'slkdjflskjdflsjdflsdf',
#             3:'sdçlfsljdflksjdfkjdlsjldkfjslkdjf'}
#
# def read_articles_sample_data():
#     articles_hash = {}
#     for key, phrase in articles_sample_data.items():
#         for letter in phrase:
#             letter_list = articles_hash.get(key,[])
#             letter_list.append(letter)
#             articles_hash[key] = letter_list
#
#     return articles_hash
#
# articles_words_hash = {}
#
# for key,words in read_articles_sample_data().items():
#     for word in words:
#         letter_list = articles_words_hash.get(word, LinkedList())
#         node_data = letter_list.find_node_data(key)
#         if node_data:
#             node_data.increment_count()
#         else:
#             letter_list.append(NodeData(key, 1))
#
#         articles_words_hash[word] = letter_list
#
# for key,value in articles_words_hash.items():
#     print('[{}] ->{}'.format(key,value))

import re



def remove_xml_tags(text):
    return re.sub('<[^<]+>', "")

articles_words_hash = {}
current_doc = 0

with open("txt-for-assignment-data-science.txt") as f:
    for line in f.readlines():
        #clean the line
        line = line.replace('&amp;','').strip()
        # line.startswith('<') and line.endswith('>')
        if re.match('<[^<]+>',line):
            if line.startswith('<doc>'):
                current_doc += 1
        else:
            words = line.lower().strip().split(' ')
            for word in words:
                word = re.sub('[^A-Za-z0-9]+', '', word)
                if word:
                    words_list = articles_words_hash.get(word, LinkedList())
                    node_data = words_list.find_node_data(current_doc)
                    if node_data:
                        node_data.increment_count()
                    else:
                        words_list.append(NodeData(current_doc, 1))

                    articles_words_hash[word] = words_list

for key,value in articles_words_hash.items():
    print('[{}] ->{}'.format(key,value))