import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

import sys
sys.path.insert(0, 'C:/Users/PC/Desktop/webCategorization-main')
from config import datasetPath
from main import x

df = pd.read_csv(datasetPath)
df = df.rename(columns={'main_category:confidence': 'main_category_confidence'})
df = df[['url', 'main_category', 'main_category_confidence']]

df = df[(df['main_category'] != 'Not_working') & (df['main_category_confidence'] >= 0.5)]

X_train, X_test, y_train, y_test = train_test_split(df['url'], df['main_category'],test_size=0.01, random_state = 0)

# display train data
# df.main_category.value_counts().plot(figsize=(12, 5), kind='bar', color='green')
# plt.xlabel('Category')
# plt.ylabel('Total Number Of Individual Category for Training')
# plt.show()

# display test data
# dt =pd.DataFrame({'url':X_test,'main_category':y_test})
# dt.main_category.value_counts().plot(figsize=(12, 5), kind='bar', color='green')
# plt.xlabel('Category')
# plt.ylabel('Total Number Of Individual Category for Training')
# plt.show()
print(y_test)
new_index=[]
for j in range(115):
    new_index.append(j)

y_test_new=pd.Series(y_test.values)
y_test.index=new_index
y_test =values

y_pred=[]
# print(y_test)
c=0;
for i in X_test:
    res=x(i)
    if type(res)==tuple:
        a=res[0]
        y_pred.append(a)
    else:
        y_test.drop(index=c)
    c+=1
print(leny_test)


lab = set(df['main_category'].values)
lab = dict(enumerate(lab,1))
lab = dict (zip(lab.values(),lab.keys()))


                
'''convert keys to values and values to keys.
                This helps to turn the label into numerics.
                for classification'''
y_test_label = list(map(lab.get, y_test))
y_pred_label = list(map(lab.get, y_pred))

target_names = ['Hukuk ve Hükümet', 'Referans',   'Finans', 'Hobi', 'Hayvanlar',
                            'Yeme ve İçme', 'Haberler ve Medya', 'İş ve Endüstri', 'İnsan ve Toplum',
                            'Ev ve Bahçe', 'Seyahat', 'Otomobil ve Araçlar',
                            'İnternet ve Telekom', 'Kariyer ve Eğitim', 'Bilim',
                            'Kumar', 'Sağlık', 'Spor', 'Kitaplar ve Literatür',
                            'Bilgisayar ve Elektronik', 'Sanat ve Eğlence', 'Güzellik ve Fitness',
                'Yetişkin','Alışveriş','Oyunlar']

print(classification_report(y_test,y_pred,target_names=target_names))

# array=y_test.array
# count=0
# countN=0

# for j in range(len(y_pred)):
#     if y_pred[j]=='None':
#         countN+=1
#     elif y_pred[j]==array[j]:
#         count+=1

# acc=count/(len(y_pred)-countN)
# print(f'Eslesen eleman sayisi : {count}')
# print(f'None eleman sayisi : {countN}')
# print(f'Accuracy Degeri : {acc}')