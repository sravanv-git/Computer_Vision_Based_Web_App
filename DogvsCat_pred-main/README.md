# DogvsCat_pred
# Model Architecture:
This cats vs Dogs predicts wheather a given image is cat or dog. Intially we preproces the data,we convert every image into Gray scale so that it will be easier to copute for the machine. Now we build a model using Conv2D networks and using activation function as 'relu'. we experiment with the no. of layers and finalise them by best accuracy.This model gave us an accuracy of 67% in identifying cat or dog.


  
# Model Summary:



|(No. of Conv2D filters/layers,size od filters,epoch)    |loss|acc| val_loss|val_acc| prediction
| ---- |------| ----|---|---|---
| (9,3,8)  |0.0671           |0.9979    |  0.8085      | 0.673  |  -
| (15,4,8)         |0.0294    |   0.9997     | 1.0386    |0.6260    |-
| (15,3,8) |   0.0606     | 0.9973          |0.8133         |0.67907   | 1.0-cat,2.0-cat,3.1-cat

**images**

1.![](https://github.com/sravanv-git/DogvsCat_pred/blob/main/images/dogvscat1.png)   

2.![](https://github.com/sravanv-git/DogvsCat_pred/blob/main/images/dogvscat2.png)

3.![](https://github.com/sravanv-git/DogvsCat_pred/blob/main/images/dogvscat3.png)
