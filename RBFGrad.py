# -*- coding: utf-8 -*-
"""RBFGrad.py

Automatically generated by Colaboratory.

"""
import numpy as np
from sklearn.metrics import mean_squared_error as MSE
class RBFNeuron(): 
  def __init__(self,learningRate=1.0): 
    
    self.primative=[] 
    self.inputs=[]
    self.w=[] 
    self.prototype=[]
    self.currentoutput=[]
    self.learningRate=learningRate
    self.deltaW=[]
    self.receiveID=[] 
  def set_primative(self,pattern):  #this will be the 'primative' = x_{prim}
    if self.primative==[]: #if the primative in this neuron is empty, otherwise it will always have a primative and does not have to be overwritten.
      self.primative=pattern
      self.w=np.ones(len(self.primative)) #same idea goes with weights, it should not be reinitiatd with 1s as it has already been set. 
      for i in range(len(pattern)):
        self.prototype.append(np.tanh(self.primative[i] * self.w[i])) #the prototype w*x_{prim}
  
  def set_inputs(self,inputs):  #this sets what the neuron should be grad descent the prototype to (by adjusting weights) 
    self.inputs=inputs  

  def store_receiveID (self,connections): #this will tell which indices the data will be pulled from. 
    if self.receiveID==[]:
      self.receiveID = connections 
  
  def output(self,inputs=[]): 
    if inputs==[]: 
      inputs=self.inputs
    output=[]
    for i in range(len (inputs)):
      output.append(np.tanh(inputs[i]))
    return (1-MSE(output,self.prototype))
            

  def backprop(self): 
    self.deltaW =[]
    for i in range(len(self.inputs)):
      self.deltaW.append(-self.learningRate*(np.tanh(self.primative[i]*self.w[i])-np.tanh(self.inputs[i]) )*(1-(np.tanh(self.primative[i]*self.w[i]))**2) * self.primative[i])
    self.w=self.w+self.deltaW
    #update pattern: 
    self.prototype=[]
    for i in range(len(self.primative)):
      self.prototype.append(np.tanh(self.primative[i] * self.w[i]))
    
  def punish(self): 
    self.deltaW =[]
    for i in range(len(self.inputs)):
      self.deltaW.append(-self.learningRate*(np.tanh(self.primative[i]*self.w[i])-np.tanh(self.inputs[i]))*(1-(np.tanh(self.primative[i]*self.w[i]))**2) * self.primative[i])
    self.w=self.w-self.deltaW #this is gradient ascent
    #update pattern: 
    self.prototype=[]
    for i in range(len(self.primative)):
      self.prototype.append(np.tanh(self.primative[i] * self.w[i]))

class RBFLayer(): 
  def __init__(self): 
    self.num_neurons=0
    self.neuron=[]
    self.inputs=[] 
    self.new_neurons=0

  def add(self,num_neurons=10):
    self.new_neurons=num_neurons #this will keep track of the start point of new neurons 
    self.num_neurons=self.num_neurons+num_neurons
    for i in range(self.new_neurons):
      self.neuron.append(RBFNeuron()) #no learning rate has been assigned, defaulted to 1.0. 

  def initialize(self,inputs): #When initializing, you set the primatives for each neuron. Should it grab a portion each? I think it should in uniform. 
    if self.new_neurons !=0:
      self.inputs =inputs
      input_len = len(inputs)
      #calculating the spaces.  #keep in mind that this tends to miss out on  the edges of data. 
      space=input_len//self.new_neurons
    
      ctr=0
      for i in range((self.num_neurons-self.new_neurons),self.num_neurons): 
        self.neuron[i].set_primative (inputs[ctr:(ctr+space)])
        self.neuron[i].store_receiveID(np.arange(ctr,(ctr+space),1))
        ctr=ctr+space
      self.new_neurons=0 #these have been set and therefore should n e reemoved. 

  def set_input (self,inputs): #this is for backprop. 
    self.inputs=inputs

  def trainNeurons (self,selectNeurons): 
      for i in range (len(selectNeurons)): 
        gatherInputs = [self.inputs[j] for j in (self.neuron[selectNeurons[i]].receiveID)]

        self.neuron[selectNeurons[i]].set_inputs(gatherInputs)
        self.neuron[selectNeurons[i]].backprop()

  def punishNeurons (self,selectNeurons): 
      #the set inputs must have a value. 
      for i in range (len(selectNeurons)): 
        gatherInputs = [self.inputs[j] for j in (self.neuron[selectNeurons[i]].receiveID)]
        self.neuron[selectNeurons[i]].set_inputs(gatherInputs)
        self.neuron[selectNeurons[i]].punish()

  def layerOutput(self,inputs=[]):
    output=[] 

    for i in range(self.num_neurons): 
      temp = [inputs[i] for i in (self.neuron[i].receiveID)]
      output.append(self.neuron[i].output(temp))
    return output

