import torch

def load_model():
    model = torch.load('model/sign_model.pth', map_location=torch.device('cpu'))
    model.eval()
    return model
