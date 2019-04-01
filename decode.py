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

class PolybiusDecoder(object):
    def __init__(self, values: List[int]):
        self.values = values
        self.count = len(values)
        self.index = 0
    
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
            return " "
        
        x = (c - 1) % 10 
        y = c // 10 - 1

        if x < 0 or x >= 5 or y < 0 or y >= 5:
            raise ValueError("Invalid value supplied (%d)" % c)

        c = y * 5 + x
        if c > 8:
            c += 1
        c += ord('A')
        return chr(c)


def decode(values: List[int]) -> str:
    return "".join(PolybiusDecoder(values))


if __name__ == "__main__":
    print(decode([int(x) for x in argv[1:]]))
