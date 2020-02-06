import pandas as pd
from cenpy import products
import matplotlib.pyplot as plt

chicago = products.ACS(2017).from_place('Chicago, IL', level='tract',
                                        variables=['B00002*', 'B01002H_001E'])

f, ax = plt.subplots(1,1,figsize=(20,20))
chicago.dropna(subset=['B00002_001E'], axis=0).plot('B00002_001E', ax=ax, cmap='plasma')
ax.set_facecolor('k')