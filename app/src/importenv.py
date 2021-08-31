# -*- coding: utf-8 -*-
import os
from os.path import join, dirname
from dotenv import load_dotenv
from enum import Enum

from typing import List , Dict

class ImportEnvKeyEnum(Enum):
  """ .envファイルのキーを書く """

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ENV_DIC: dict = {}
# ImportEnvKeyEnumの値を書く
ENV_KEYS: list = []

for key in ENV_KEYS:
  ENV_DIC[key] = os.environ.get(key)