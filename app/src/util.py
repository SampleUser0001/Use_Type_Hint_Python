# -*- coding: utf-8 -*-
from typing import List
from dataclass import User

class Util:
  @staticmethod
  def print_array(v: List[str]) -> None:
    for i in range(len(v)):
      print("%d : %s" % (i, v[i]))
  
  @staticmethod
  def print_user(user: User) -> None:
    print("name : %s , age : %d" % (user.name, user.age))
