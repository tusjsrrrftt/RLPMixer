import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

from models.rlpmixer_model import RLPMixer
from reinforcement.agent import RLAgent
from utils import load_data

def train(model, agent, dataloader, epochs=10):
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for batch in dataloader:
            state, action, reward, next_state, done = batch
            agent.optimize(state, action, reward, next_state, done)
            loss = nn.functional.mse_loss(model(state), action.float())
            total_loss += loss.item()
        print(f"Epoch {epoch + 1}/{epochs}, Loss: {total_loss / len(dataloader)}")

def main():
    # Load data
    train_data = load_data('data/processed/train_dataset.pt')
    dataloader = DataLoader(train_data, batch_size=32, shuffle=True)

    # Initialize model and agent
    model = RLPMixer(input_dim=256, output_dim=10)
    agent = RLAgent(model)

    # Train the model
    train(model, agent, dataloader)
    
    # Save model
    torch.save(model.state_dict(), 'models/rlpmixer_checkpoint.pt')
    print("Training complete. Model saved.")

if __name__ == "__main__":
    main()
