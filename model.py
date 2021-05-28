import torch
import torch.nn as nn
import torch.nn.functional as F

class Autoencoder(nn.Module):

    def __init__(self, input_dim):
        super(Autoencoder, self).__init__()

        # Encoder
        self.encoder1 = nn.Linear(input_dim, 256)
        self.encoder2 = nn.Linear(256, 128)
        self.encoder3 = nn.Linear(128, 26)

        # Decoder
        self.decoder1 = nn.Linear(26, 128)
        self.decoder2 = nn.Linear(128, 256)
        self.decoder3 = nn.Linear(256, input_dim)

    def forward(self, x):
        x = F.relu(self.encoder1(x))
        x = F.relu(self.encoder2(x))
        x = F.relu(self.encoder3(x))
        x = F.relu(self.decoder1(x))
        x = F.relu(self.decoder2(x))
        return self.decoder3(x)