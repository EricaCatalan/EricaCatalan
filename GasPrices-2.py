#!/usr/bin/env python3
# -*- coding: utf-8 -*-

@author: ericacatalan
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('gas_prices.csv')
plt.figure(figsize=(8,5), dpi=300)
bars = plt.bar(Countries, Gas Prices)
Countries = ['Australia', 'Canada', 'South Korea', 'USA']
Gas Prices = ['4.45', '4.08', '6.21', '3.27']
plt.title('Highest Gas Price by Country (in USD)' , fontdict ={'fontweight':'bold', 'fontsize': 18})
plt.xlabel('Countries')
plt.ylabel('Gas In US Dollars')
plt.legend()
plt.savefig('Highest_Gas_Price_By_Country')
plt.show()