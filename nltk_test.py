# 第一步: 先查詢文本id
import nltk
from nltk.corpus import inaugural
inaugural.fileids()
# 後3筆Result
['2001-Bush.txt', '2005-Bush.txt', '2009-Obama.txt']
# 輸入文本原始內容並進行斷句
sent = inaugural.raw('1789-Washington.txt')
print(nltk.sent_tokenize(sent))
"""
# 英文範例
sentence = 'At eight oclock on Thursday morning Arthur didnt feel very good Andy Lau.'

# 使用 split
print(sentence.split())
#result ['At', 'eight', 'oclock', 'on', 'Thursday', 'morning', 'Arthur', 'didnt', 'feel', 'very', 'good', 'Andy', 'Lau.']


# 透過 fileid 可以找到該語料庫底下的文本有哪些
from nltk.corpus import brown
print(brown.categories())




from nltk.corpus import gutenberg

# 以 gutenberg 語料庫當中的第一篇語料為例
#print(gutenberg.raw('austen-emma.txt'))
#print(gutenberg.words('austen-emma.txt'))
#print(gutenberg.sents('austen-emma.txt'))

# 字詞數/句子數的計算
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))   # 輸出文本原始內容
    num_words = len(gutenberg.words(fileid)) # 輸出文本單詞列表
    num_sents = len(gutenberg.sents(fileid)) # 輸出文本句子列表
    print(num_chars, num_words, num_sents, fileid)
"""