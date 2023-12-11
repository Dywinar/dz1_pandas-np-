import pandas as pd
import numpy as np
slovar = {
    'Name': ['Кирилл', 'Саня', 'Виктор', 'Виталий', 'Сергей', 'Ярик', 'Дмитрий'],
    'Age' : np.linspace(10,70,7),
    'City' : ['Ростов-на-Дону', 'Москва', 'Омск', 'Омск', 'Калининград', 'Воронеж', 'Керчь']
}
data = pd.DataFrame(slovar)
print(data.head(3))
print(data.tail(3))
data.to_csv('myData_Frame.csv', index = False)
