import operator
import numpy as np
import pandas as pd

from typing import Dict
from typing import Union
from typing import List
from typing import Optional
from typing import Tuple

from pyrobot.stock_frame import StockFrame

class Indicators():
    def __init__(self, price_data_frame: StockFrame) -> None:
        #leading w underscore -> private
        self._stock_frame: StockFrame = price_data_frame
        self._price_groups = self._stock_frame.symbol_groups
        self._current_indicators = {}
        self._indicator_signals = {}
        self._frame = self._stock_frame.frame