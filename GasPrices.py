#!/usr/bin/env python3
# -*- coding: utf-8 -*-

@author: ericacatalan
"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
gas = pd.read_csv('gas_prices.csv')
plt.figure(figsize=(8,5))
plt.title('Gas Prices Over Time (in USD)', fontdict={'fontweight' : 'bold', 'fontsize' : 18})
plt.plot(gas.Year, gas.USA, 'b.-', label = 'United States')
plt.plot(gas.Year, gas.Canada, 'r.-')
plt.plot(gas.Year, gas('South Korea'), 'g.-')
plt.plot(gas.Year, gas.Australia, 'y.-')
plt.xticks(gas.Year[::3].tolist()+[2011])
plt.xlabel('Year')
plt.ylabel('US Dollars')
plt.legend()
plt.savefig('Gas_Price_figure.png' dpi=300
plt.show()


