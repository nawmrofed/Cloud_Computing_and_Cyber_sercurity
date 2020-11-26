import torch
import torch.nn as nn
import numpy as np
import random

labels = []
features = []

class Classifier1(nn.Module):
    def __init__(self):
        super(Classifier1, self).__init__()
        self.fc = nn.Sequential(nn.Linear(4, 2))

    def forward(self, x):
        out = self.fc(x)
        out = out.view(out.size()[0], -1)
        return out

with open('data_banknote_authentication.txt','r') as f:
    lines = f.readlines()
    random.shuffle(lines)
    for line in lines:
        feats = line.strip().split(",") 
        label = feats[len(feats) - 1] 
        feats = feats[: len(feats) - 1]
        labels.append(float(label))
        fts = [ float(feature) for feature in feats ] # need floats
        features.append(fts)
    features = np.array(features)
    labels = np.array(labels)

model = Classifier1().cpu()
loss = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0)

train_acc = 0.0
train_loss = 0.0
model.train()
data = torch.from_numpy(features).float()
labels = torch.from_numpy(labels).type(torch.int64)


for j in range(0,10000):
    optimizer.zero_grad()
    train_pred = model(data)
    batch_loss = loss(train_pred, labels)
    batch_loss.backward()
    optimizer.step()
    train_acc += np.sum(np.argmax(train_pred.data.numpy(), axis=1) == labels.numpy())
    train_loss += batch_loss.item()

optimizer.zero_grad()
train_pred = model(data)
count = 0
print(loss(train_pred, labels).item())
print(np.sum(np.argmax(train_pred.cpu().data.numpy(), axis=1) == labels.numpy()) / len(labels))
