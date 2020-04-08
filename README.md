


![alt text](/images/network.png)

### A Modified RBF Network Implementation 

-----
RBF networks are unique networks that differ from standard MLP models. RBFs work from the idea that each neuron will have a central basis or 'prototype' data. Inputs that are closer to the prototype will result in higher activation of the neuron. Training occurs when the prototype is modified by adjusting weights through an optimization algorithm to match inputs. 

There are a handful of implementations of RBF. This is my attempt at implmenting a unique RBF 'like' network. The optimization algorithm I chose is gradient descent. 

The RBF-like network contains neurons that take a 1-D array of data and stores it as a central basis. During training weights that are applied to the prototype are adjusted by gradient descent as similar data is introduced to the network. The output of each neuron is 1-MSE(prototype,input), meaning that as the input is closer to the prototype the higher the activation is. 

My implementation allows for gradient ascent training, which can be used when the neurons are presented with data that should NOT be incorporated into the neuron's prototype. For example, below is the prototype of a neuron that has been trained using gradient descent on MNIST 0, but gradient ascent on MNIST 4. 


![alt text](/images/0 NOT 4.png)


With this implementation you are able to generate a set of RBF neurons, and also generate additional neurons even after the first set of neurons have been trained. In this way, you are also able to train subsets of neurons on your own choice of data.



See the Jupyter Notebook for implementation. 





To do: 
- [x] Write notebook to demonstrate basic implementation of RBF network.
- [ ] Notebook to demonstrate training multiple sets of RBF neurons on multiple types of data
- [ ] Notebook to demonstrate gradient ascent training. 
