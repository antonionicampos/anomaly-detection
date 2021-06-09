import time
import torch
import re

from datetime import datetime
from model import Autoencoder
import torch.optim as optim

def train_model(model, train_loader, criterion, optimizer, initial_epoch=0, epochs=20):
    
    print('starting model training...')
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"training on {'cuda' if torch.cuda.is_available() else 'cpu'}")
    model.to(device)
    history = []
    
    for epoch in range(initial_epoch, epochs):
        start = time.time()
        model.train()
        training_loss, running_loss = 0.0, 0.0
        
        # Iterando sobre o dataset
        for batch_i, data in enumerate(train_loader):
            X = data['X'].to(device)
            
            # Zero Grad
            optimizer.zero_grad()

            # Forward Pass
            output = model(X)

            # Loss Function
            loss = criterion(output, X)

            # Backward Pass
            loss.backward()
            running_loss += loss.item()
            training_loss += loss.item()

            # Update
            optimizer.step()

            if batch_i % 200 == 199:
                print('Batch: {}, Avg. Loss: {}'.format(batch_i + 1, running_loss / 200))
                running_loss = 0.0
        
        # Epoch results
        training_loss /= len(train_loader)
        print(f'[{round(time.time() - start, 3)} secs] Epoch: {epoch+1}/{epochs}', end='')
        print(f', Training loss: {training_loss}', end='\n\n')
        history.append(training_loss)
    
    print('training finished.')
    
    date = str(datetime.now()).split('.')[0]    
    model_path = f'.\\models\\model_mae_{re.sub(r"[^0-9]", "", date)}.pt'
    torch.save({
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'loss': training_loss
    }, model_path)
    
    print('model saved.')
    
    return history

def load_model(path, dataset):
    dim = dataset[0]['X'].shape[0]
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    model = Autoencoder(input_dim=dim)
    model.to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    checkpoint = torch.load(path)
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    epoch = checkpoint['epoch']
    train_loss = checkpoint['loss']
    
    return model, optimizer, epoch, train_loss