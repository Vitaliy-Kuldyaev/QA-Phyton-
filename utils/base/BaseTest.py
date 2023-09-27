import configparser
import os
import sys
from pathlib import Path

import pytest

from utils.actions.do import doClass

do = doClass()

# @pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass