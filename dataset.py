import pandas as pd
import pandas as pd
import torch

from torch.utils.data import Dataset

class Dataset(Dataset):

    mean: pd.Series = pd.read_hdf('.\\data\\norm.h5', key='mean')
    std: pd.Series = pd.read_hdf('.\\data\\norm.h5', key='std')

    def __init__(self, path: str, key: str, simulation=None):
        df = pd.read_hdf(path, key=key)
        if key == 'normal':
            if simulation:
                assert isinstance(simulation, int), 'Parâmetro simulation deve ser int com número da simulação'
                df = df[df['simulationRun'] == simulation]
            self.data = df.iloc[:, 3:]
            self.norm_data = (self.data - self.mean) / self.std
        elif key == 'faulty':
            assert isinstance(simulation, tuple), 'Parâmetro simulation deve ser tupla com número da simulação e número da falha'
            self.data = df[(df['simulationRun'] == simulation[0]) & (df['faultNumber'] == simulation[1])].iloc[:, 4:]
            self.norm_data = (self.data - self.mean) / self.std            

    def __len__(self) -> int:
        return len(self.norm_data)

    def __getitem__(self, idx: int) -> dict:
        if torch.is_tensor(idx):
            idx = idx.tolist()

        X = self.norm_data.iloc[idx, :].values        
        sample = {'X': torch.from_numpy(X).float()}
        return sample