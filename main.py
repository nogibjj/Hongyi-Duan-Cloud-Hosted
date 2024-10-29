import numpy as np
import pandas as pd

def create_dataframe():
    data = {
        'Heroes': ['Kailin', 'Kaiserui', 'Shakete', 'Adela', 'Luna', 'Siqiangke', 'Taiz', 'Zhanshu'],
        'Skill 1': ['Houqin', 'Zhaohunshu', 'Jingongshu', 'Waijiaoshu', 'Zhihuishu', 'Zhaohunshu', 'Fangyushu', 'Jianshu'],
        'Skill 2': ['Jianshu', 'Fangyushu', 'Zhanshu', 'Zhihuishu', 'Huoximofa', 'Dikangli', 'Dikangli', 'Jianshu'],
        'Race': ['Bilei', 'Muyuan', 'Dixiacheng', 'Chengbao', 'Yuansucheng', 'Muyuan', 'Yaosai', 'Bilei'],
        'Hero Score': [9.5, 10.0, 9.5, 9.5, 9.5, 3.0, 9.0, 8.0],
        'Race Score': [8.5, 9.5, 7.5, 9.0, 9.5, 9.5, 8.5, 7.0]
    }
    
    df = pd.DataFrame(data)
    return df

def modify_dataframe(df):
    df['Skill Score'] = np.array([9.5, 9, 9, 8.5, 8, 7, 9, 9])
    new_row = ['Gengna', 'Houqin', 'Zhanshu', 'Bilei', 9.5, 7.5, 9.5]
    df.loc[8] = new_row
    df.loc[0, 'Race Score'] = 8.5
    return df

if __name__ == "__main__":
    df = create_dataframe()
    df = modify_dataframe(df)
    print(df)
