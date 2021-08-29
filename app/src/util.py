# -*- coding: utf-8 -*-
from typing import List

class Util:
  @staticmethod
  def print_array(v: List[int]) -> None:
    for i in range(len(v)):
      print("%d : %s" % (i, v[i]))
  
