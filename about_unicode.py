# There are so many ways to deal with unicode in python, different situation use different methods.
# I have already tried many methods, however, each time, in different situations, I had to find new solutions again
# Python version, IDE, data source, etc. will all influence the output
# so, I's better reocrd my solutions each time here to save my future time


# Sample 1: <p>...the police investigations into the women\u2019s disappearances,\u201d Mr. Oppal writes.</p>
## I etracted the data from HTML directly, when I used str(), I got these characters: \u201d, \u2019
## This works for me in python 3
import unidecode
text = ["<p>"+str(unidecode.unidecode(t.text))+"</p>" for t in content.findAll('p', {"class":''})]


# Sample 2: could\xe2\x80\x99t  (means couldn't)
import unidecode
word_lst = [str(unidecode.unidecode(w.decode('utf-8'))) for w in text.split()]


# Sample 3: the error message could be: UnicodeDecodeError: 'utf-8' codec cannot decode byte 0x93...
## this is a more complex situation, especially when you are using python3.*
# first of all you have to read the data from file as 'rb' and decode each line
text_string = ""
with open('input_file_path', 'rb') as indata:
  for l in indata:
    text_string = " ".join([text_string, l.strip().decode('utf-8', 'backlashescape')])
    
# BUT! Here, the python version could be different, check the multiple solutions here to cater for different situations:
# answer by "anatoly techtonik"
# http://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string


# Sample 4: UnicodeEncodeError: 'ascii' codec can't encode character u'\u2026'
data = text.encode('utf-8')
