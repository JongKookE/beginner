import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def compare_of_two_attribute(data , title, x, hue = None):
    sns.set(style="darkgrid")
    plt.figure(figsize=(6,6))
    plt.title(title)
    sns.countplot(data = data, x = x, hue = hue)
