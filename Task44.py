import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


categories = data['whoAmI'].unique()


onehot_encoded = []
for category in categories:
    onehot_encoded.append(data['whoAmI'].apply(lambda x: 1 if x == category else 0))


onehot_df = pd.DataFrame(onehot_encoded).T
onehot_df.columns = categories


print(onehot_df.head())

