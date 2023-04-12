import pandas as pd
import numpy as np


chat_id = 433193277 # Ваш chat ID, не меняйте название переменной

def solution(x1: np.array) -> bool: 
    result = ztest(x1, value = 500, alternative = 'larger')[1] 
    
    if result < 0.04:
        return True
    return False
solution(x1)
