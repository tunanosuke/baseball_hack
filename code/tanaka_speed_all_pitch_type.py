
# coding: utf-8

# In[2]:


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import OrderedDict

pitch_data = OrderedDict()
for day in (20170502, 20170508, 20170514, 20170520, 20170526):
    pitch = pd.read_csv("../data/mlbam_pitch_{day}.csv".format(day=day))
    pitch_data[day] = pitch.query("pit_box_name=='Tanaka'")


# ## 球種ごとの球速

# In[3]:


sns.set_context("notebook", 2.0, {"lines.linewidth": 6})

axarray = {day: None for day in pitch_data.keys()}
f, (axarray) = plt.subplots(1, len(pitch_data.keys()), sharey=True, figsize=(32,8))

for i, day in enumerate(pitch_data.keys()):
    axarray[i].set_title("Tanaka({day})".format(day=day))
    sns.stripplot(x = "pitch_type", y = "start_speed", data = pitch_data[day], hue = "pitch_res", ax = axarray[i], split = True, jitter = True)


# ## 投球回ごとの球速

# In[4]:


sns.set_context("notebook", 2.0, {"lines.linewidth": 2})

axarray = {day: None for day in pitch_data.keys()}
f, (axarray) = plt.subplots(1, len(pitch_data.keys()), sharey=True, figsize=(32,8))

for i, day in enumerate(pitch_data.keys()):
    axarray[i].set_title('Tanaka({day})'.format(day=day))
    sns.pointplot(x="inning_number", y="start_speed", hue="pitch_type", ax=axarray[i], data=pitch_data[day], dodge=True, palette="Set1")


# ## 投球回ごとの回転数

# In[6]:


sns.set_context("notebook", 2.0, {"lines.linewidth": 2})

axarray = {day: None for day in pitch_data.keys()}
f, (axarray) = plt.subplots(1, len(pitch_data.keys()), sharey=True, figsize=(32,8))

for i, day in enumerate(pitch_data.keys()):
    axarray[i].set_title('Tanaka({day})'.format(day=day))
    sns.pointplot(x="inning_number", y="spin_rate", hue="pitch_type", ax=axarray[i], data=pitch_data[day], dodge=True, palette="Set2")

