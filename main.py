import json
import hashlib
# from pprint import pprint
import os


class IterCounter:          
    def __init__(self, file):        
        self.file = open(file, 'r', encoding='utf-8')

    def __iter__(self):      
        return self

    def __next__(self):
      d = next(self.g)
      return d

    def counter_writer(self, country):
        with open('json_file.txt', 'a', encoding='utf-8') as f:
            f.write(country + ', https://en.wikipedia.org/wiki/' + country.replace(' ', '_') + '\n')
          
    def start_iter(self):
        for i in iter(json.load(self.file)): 
            for k,v in i.items():
                if k == 'name':
                    for k,v in v.items():
                        if k == 'common':
                            self.counter_writer(v)


def MyHashGen(file_path):     # хэш генератор                   
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, v in enumerate(f):
            yield hashlib.md5(v.encode()).hexdigest()
                     
       
file = 'json_file.txt'
file_path = os.path.join(os.getcwd(), 'ad_files', file)

 
if __name__ == '__main__':
    f = IterCounter('countries.json')
    f.start_iter()                       ####### DZ 1


for hash in MyHashGen(file):
    print(hash)                          ####### DZ 2
