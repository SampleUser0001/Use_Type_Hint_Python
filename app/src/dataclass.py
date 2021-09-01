# -*- coding: utf-8 -*-
import dataclasses

@dataclasses.dataclass
class User:
  name: str
  age: int = 0
  
@dataclasses.dataclass
class User2:
  hoge: str
  piyo: int = 0
  fuga: str
