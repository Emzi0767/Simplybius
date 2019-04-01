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


from __future__ import print_function
from encode import encode
from decode import decode
from discord import discordify, undiscordify
from typing import List
from sys import argv


def main(args: List[str]):
    if args[0] not in ["encode", "decode", "dencode", "ddecode"]:
        raise ValueError("Operation needs to be encode, decode, dencode, or ddecode.")
    
    if args[0] == "encode":
        print(" ".join(str(x) for x in encode(" ".join(args[1:]))))
    
    elif args[0] == "decode":
        print(decode([int(x) for x in args[1:]]))
    
    elif args[0] == "dencode":
        print(discordify(encode(" ".join(args[1:]))))
    
    elif args[0] == "ddecode":
        print(decode(undiscordify(" ".join(args[1:]))))


if __name__ == "__main__":
    main(argv[1:])
