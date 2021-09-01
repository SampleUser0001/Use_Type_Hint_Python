# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os
from typing import List, Dict, Any, Optional

import sys
sys.path.append('./')
from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting
from util import Util
from dataclass import User, User2

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)

# なんでこれエラーなんだ？
log_conf: Dict[Any, Any] = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')

config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

if __name__ == '__main__':
  i: int = 10
  b: bool = True
  s: str = 'hoge'
  f: float = 1.2
  d: dict = {}
  
  # これはエラー。
  i = 'error'
  
  tmp_list: List[str] = []
  tmp_list.append('hoge')
  tmp_list.append('piyo')

  Util.print_array(tmp_list)
  
  # エラー。strをappendしたにも関わらず、intをappendしている。
  tmp_list.append(1)

  Util.print_array(tmp_list)
  
  # これはエラーにならない。
  user: User = User(name='hoge', age=20)
  # こっちはエラー。
  user2: User2 = User(name='hoge', age=20)

  Util.print_user(user)
  # これもエラー。
  Util.print_user(user2)

  # .envの取得
  # setting.ENV_DIC[ImportEnvKeyEnum.importenvに書いた値.value]