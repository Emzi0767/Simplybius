# Copyright 2019 Emzi0767
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import print_function, division # py2 compat
from typing import List
from sys import argv


map = {
    1: ":one:",
    2: ":two:",
    3: ":three:",
    4: ":four:",
    5: ":five:"
}
rmap = {
    ":one:": 1,
    ":two:": 2,
    ":three:": 3,
    ":four:": 4,
    ":five:": 5,
    ":blank:": 0
}


class Discordifier(object):
    def __init__(self, values: List[int]):
        self.values = values
        self.index = 0
        self.count = len(values)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.index >= self.count:
            raise StopIteration()

        c = self.values[self.index]
        self.index += 1

        if c == 0:
            return ":blank:"
        
        return "%s %s" % (map[c // 10], map[c % 10])


class Undiscordifier(object):
    def __init__(self, text: str):
        self.text = text
        self.index = 0
        self.count = len(text)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.index >= self.count:
            raise StopIteration()
        
        c = self.text[self.index]
        self.index += 1
        while self.index < self.count and c != ':': # find first colon
            c = self.text[self.index]
            self.index += 1
        
        start = self.index
        end = start + 1
        c = self.text[end]
        while end < self.count and c != ':': # find second colon
            end += 1
            c = self.text[end]
        
        self.index = end + 1
        str = self.text[start - 1:end + 1]
        if str not in rmap:
            raise ValueError("Invalid value supplied (%s)." % str)
        
        v = rmap[str]
        if v == 0:
            return 0

        v *= 10

        c = self.text[self.index]
        self.index += 1
        while self.index < self.count and c != ':': # find first colon
            c = self.text[self.index]
            self.index += 1
        
        start = self.index
        end = start + 1
        c = self.text[end]
        while end < self.count and c != ':': # find second colon
            end += 1
            c = self.text[end]

        self.index = end + 1
        str = self.text[start - 1:end + 1]
        v += rmap[str]

        return v


def discordify(values: List[int]) -> str:
    return " ".join(Discordifier(values))


def undiscordify(text: str) -> List[int]:
    return [x for x in Undiscordifier(text)]


if __name__ == "__main__":
    if argv[1] not in ["discordify", "undiscordify"]:
        raise ValueError("Operation needs to be discordify or undiscordify.")
    
    if argv[1] == "discordify":
        print(discordify([int(x) for x in argv[2:]]))
    elif argv[1] == "undiscordify":
        print(" ".join(str(x) for x in undiscordify(" ".join(argv[2:]))))
        