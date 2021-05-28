import pyreadr
import torch

from torch.utils.data import Dataset

class Dataset(Dataset):

    def __init__(self, rdata_file, rdata_key):
        """
        Args:
            csv_file (string): Path to the csv file with data.
        """
        self.data = pyreadr.read_r(f'.\\data\\{rdata_file}')[rdata_key].iloc[:, 3:]
        self.norm_data = (self.data - self.data.mean()) / self.data.std()

    def __len__(self):
        return len(self.norm_data)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        X = self.norm_data.iloc[idx, :].values        
        sample = {'X': torch.from_numpy(X).float()}
        return sample