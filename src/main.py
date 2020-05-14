# %%
import os
import pandas as pd


class ad():
    def __init__(self):
        self.raw_data_path = '../data/raw/'
        if 'test' not in os.listdir(self.raw_data_path):
            self.getdataset()
        self.read_dataset()

    def read_dataset(self):
        path_train = self.raw_data_path + 'train_preliminary/'
        self.train_ad = pd.read_csv(path_train + 'ad.csv')
        self.train_click_log = pd.read_csv(path_train + 'click_log.csv')
        self.train_user = pd.read_csv(path_train + 'user.csv')

        path_test = self.raw_data_path + 'test/'
        self.test_ad = pd.read_csv(path_test + 'ad.csv')
        self.test_click_log = pd.read_csv(path_test + 'click_log.csv')

    def getdataset(self):
        def get_data(url):
            # !pip install wget
            path = self.raw_data_path
            import wget
            import tarfile
            filename = wget.download(url, out=path)
            print(filename)
            import zipfile
            zFile = zipfile.ZipFile(filename, "r")
            for fileM in zFile.namelist():
                zFile.extract(fileM, path)
                print(fileM)
            zFile.close()

        url = ['https://tesla-ap-shanghai-1256322946.cos.ap-shanghai.myqcloud.com/cephfs/tesla_common/deeplearning/dataset/algo_contest/test.zip',
               'https://tesla-ap-shanghai-1256322946.cos.ap-shanghai.myqcloud.com/cephfs/tesla_common/deeplearning/dataset/algo_contest/train_preliminary.zip', ]

        list(map(get_data, url))


if __name__ == '__main__':
    ex = ad()


# %%
ex.train_user.median()[1:].values


# %%
ex.test_click_log.user_id.unique()

# %%
df = pd.DataFrame()
df['user_id'] = ex.test_click_log.user_id.unique()
df['age'] = ex.train_user.median()[1]
df['gender'] = ex.train_user.median()[2]
path = '../res/'
df.to_csv(path + 'submission00.csv')

# %%
