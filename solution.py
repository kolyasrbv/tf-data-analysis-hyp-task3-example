import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 433193277 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.04
    
    # порог доходности нового продукта
    threshold = 500
    
    # вычисляем t-статистику и p-value
    t_statistic, p_value = st.ttest_1samp(x, threshold, alternative="two-sided")
    return p_value < 2*alpha and x.mean() > threshold


433193277
