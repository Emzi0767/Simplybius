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


class PolybiusEncoder(object):
    def __init__(self, text: str):
        self.text = text
        self.index = 0
        self.length = len(text)

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()

    def next(self):
        if self.index >= self.length:
            raise StopIteration()
        
        c = self.text[self.index]
        self.index += 1

        if c == ' ':
            return 0
        
        c = ord(c)
        if c >= ord('a') and c <= ord('z'):
            c -= ord('a')
            if c > 8: # i
                c -= 1
        elif c >= ord('A') and c <= ord('Z'):
            c -= ord('A')
            if c > 8: # i
                c -= 1
        else:
            return None
        
        y = c // 5 + 1
        x = c % 5 + 1
        return y * 10 + x


def encode(text: str) -> List[int]:
    return [x for x in PolybiusEncoder(text)]


if __name__ == "__main__":
    print(" ".join(str(x) for x in encode(" ".join(argv[1:]))))
