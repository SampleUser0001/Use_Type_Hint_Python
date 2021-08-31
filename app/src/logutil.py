# -*- coding: utf-8 -*-
import json
import os
from typing import Dict, Any

class LogUtil:
  
  @classmethod
  def get_log_conf(cls, log_conf_path: str) -> Dict[Any, Any]:
    """ ログ設定ファイルを読み込む
    """
    with open(log_conf_path, mode='r') as f:
      log_conf: Dict[Any, Any] = json.loads(f.read())
    return log_conf
