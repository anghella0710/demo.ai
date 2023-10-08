# Traffic

## Built with Python and pygame - Convolutional Neural Network
Program running: https://youtu.be/jouUEvA9HM0

## How to run
Download the [data](https://cdn.cs50.net/ai/2020/x/projects/5/gtsrb.zip) set for this project and unzip it. Move the resulting gtsrb directory inside of the traffic directory.

AI to identify which traffic sign appears in a photograph.

```
pip3 install -r requirements.txt
python traffic.py gtsrb
Epoch 1/10
500/500 [==============================] - 5s 9ms/step - loss: 3.7139 - accuracy: 0.1545
Epoch 2/10
500/500 [==============================] - 6s 11ms/step - loss: 2.0086 - accuracy: 0.4082
Epoch 3/10
500/500 [==============================] - 6s 12ms/step - loss: 1.3055 - accuracy: 0.5917
Epoch 4/10
500/500 [==============================] - 5s 11ms/step - loss: 0.9181 - accuracy: 0.7171
Epoch 5/10
500/500 [==============================] - 7s 13ms/step - loss: 0.6560 - accuracy: 0.7974
Epoch 6/10
500/500 [==============================] - 9s 18ms/step - loss: 0.5078 - accuracy: 0.8470
Epoch 7/10
500/500 [==============================] - 9s 18ms/step - loss: 0.4216 - accuracy: 0.8754
Epoch 8/10
500/500 [==============================] - 10s 20ms/step - loss: 0.3526 - accuracy: 0.8946
Epoch 9/10
500/500 [==============================] - 10s 21ms/step - loss: 0.3016 - accuracy: 0.9086
Epoch 10/10
500/500 [==============================] - 10s 20ms/step - loss: 0.2497 - accuracy: 0.9256
333/333 - 5s - loss: 0.1616 - accuracy: 0.9535

```


This project uses TensorFlow to build a neural network to classify road signs based on an image of those signs. To do so, it uses a labeled dataset: a collection of images that have already been categorized by the road sign represented in them.

For this project, we’ll use the [German Traffic Sign Recognition Benchmark](https://cdn.cs50.net/ai/2020/x/projects/5/gtsrb.zip) (GTSRB) dataset, which contains thousands of images of 43 different kinds of road signs.
