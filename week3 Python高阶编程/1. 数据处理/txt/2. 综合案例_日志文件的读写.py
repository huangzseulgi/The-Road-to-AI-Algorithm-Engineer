import random

epoch = 100
accuracy = 0.2
loss = 0.9

with open("resources/training_log.txt", "w") as f:
    f.write("epoch\taccuracy\tloss\n")

    for i in range(epoch):
        accuracy += random.uniform(0, 0.005)
        loss -= random.uniform(0, 0.005)
        accuracy = min(1, accuracy)
        loss = max(0, loss)

        f.write(f'{i}\t{accuracy}\t{loss}\n')




