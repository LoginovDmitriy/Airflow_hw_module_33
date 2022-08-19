import pandas as pd
import dill as pickle
import json
import os


# загрузим из pkl файла нашу модель
def get_model(path):
    
    dirname = f'{path}//data//models'
    files = os.listdir(dirname)
    files.sort()
    # загрузим самую последнюю модель
    with open(f'{path}//data//models//{files[-1]}', 'rb') as file:
        model_from_dill = pickle.load(file)
    return model_from_dill

# Получим список файлов в папке test
def get_list_of_test_data(path):
    dirname = f'{path}//data//test'
    files = os.listdir(dirname)
    return files

# Загрузим данные в формате json и преобразуем их в dataframe
def get_test_data(test_file, path):
    with open(f'{path}//data//test//{test_file}', 'r') as f:
        data = json.load(f)    
    df = pd.DataFrame(data, index=['0'])
    return df

# Выведем предсказание
def predict():
    #рабочая папка
    current_path = os.getcwd().replace('/', '//')
    path = current_path.replace('//modules', '')
    if path[-3:] != '_hw':
        path = path+'_hw'
    #создадим пустой dataframe, в который добавим предсказания
    df_pred = pd.DataFrame(columns=['car_id', 'pred'])
    
    model = get_model(path)
    
    for item in get_list_of_test_data(path):
        price_category = model.predict(get_test_data(item, path))
        item_pred = {'car_id': item.split('.')[0], 'pred': price_category[0]}
        df_new_row = pd.DataFrame({ 'car_id': [item.split('.')[0]], 'pred': [price_category[0]] })
        df_pred = pd.concat([df_pred, df_new_row])

    dirname = f'{path}//data//models'
    files = os.listdir(dirname)
    files.sort()
    pred = files[-1].split('_')[-1].split('.')[0]
    predictions_path = f'{path}//data//predictions//preds_{pred}.csv'
    
    if not os.path.exists(predictions_path):
        df_pred.to_csv(predictions_path, index=False)
    else:
        os.remove(predictions_path)
        df_pred.to_csv(predictions_path, index=False)


    

if __name__ == '__main__':
    predict()
