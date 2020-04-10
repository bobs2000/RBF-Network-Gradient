


![alt text](/images/network.png)


### A Modified RBF Network Implementation 

-----
RBF networks are unique networks that differ from standard MLP models. RBFs work from the idea that each neuron will have a central basis or 'prototype' data. Inputs that are closer to the prototype will result in higher activation of the neuron. Training occurs when the prototype is modified by adjusting weights through an optimization algorithm to match inputs. 

There are a handful of implementations of RBF. This is my attempt at implmenting a unique RBF 'like' network. The optimization algorithm I chose is gradient descent. 

The RBF-like network contains neurons that take a 1-D array of data and stores it as a central basis or 'prototype'. During training weights that are applied to the prototype are adjusted by gradient descent as similar data is introduced to the network. The output of each neuron is 1-MSE(prototype,input), meaning that as the input is closer to the prototype the higher the activation is. 

My implementation allows for gradient ascent training, which can be used when the neurons are presented with data that should NOT be incorporated into the neuron's prototype. For example, below is the prototype of a neuron that has been trained using gradient descent on MNIST 0, but gradient ascent on MNIST 4. 


 ![alt text](/images/0NOT4.png)


With this implementation you are able to generate a set of RBF neurons, and also generate additional neurons even after the first set of neurons have been trained. In this way, you are also able to train subsets of neurons on your own choice of data.


### How to Use:
------

<a href="https://github.com/pluu2/RBF-Network-Gradient/blob/master/Basic_Implementation.ipynb">Basic Implementation</a> - This notebook demonstrates how to create a RBF network using 10 neurons, and train the network on MNIST 0 and compare the network's activation against non MNIST 0 samples. 

<a href="https://github.com/pluu2/RBF-Network-Gradient/blob/master/RBF_Multiple_Neuron_Sets.ipynb">Training multiple sets of neurons on multiple classes of data</a> - This notebook demonstrates how to train 10 RBF neurons on MNIST 0, then add 10 new neurons and train those neurons on MNIST 4, then compare their activation on test data. 


### To do:
-----
- [x] Write notebook to demonstrate basic implementation of RBF network.
- [X] Notebook to demonstrate training multiple sets of RBF neurons on multiple types of data
- [ ] Notebook to demonstrate gradient ascent training and why it can be useful.  
