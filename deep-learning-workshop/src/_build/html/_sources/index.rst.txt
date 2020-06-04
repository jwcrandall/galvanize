.. Neural Networks using Tensorflow documentation master file

.. figure:: images/galvanize-logo.png
   :scale: 35%
   :align: center
   :alt: galvanize-logo
   :figclass: align-center

   
Course Overview
===============

Welcome!
--------

This is an exciting time to be exploring deep learning with neural networks, Tensorflow, and Galvanize.  This workshop will get you up-and-running in Tensorflow using network architectures that are in use today for general machine learning, image recognition, language processing, and encodings.  The goal of this course is to offer breadth and depth by providing short, targeted lectures with relevant example code paired with supervised coding sessions where instructors are available to answer conceptual and implementation questions.  

 
Course Contents
---------------

This four part course covers neural network architectures in use today:  multilayer perceptrons (MLPs), convolutional neural nets (CNNs), recurrent neural nets (RNNs), and autoencoders. Generally, there will be short lectures in the morning and afternoon to provide conceptual and code guidance for the exercises of that day.  Galvanize believes that you learn by doing, and that learning process is facilitated by immediate access to helpful resource material and knowledgeable staff.

Each part is further described below.

Part 1
^^^^^^

Fundamental concepts of neural networks are discussed, such as the basic computational unit, activation functions, feed forward calculation, back propogation of gradients, solvers and convergence criteria.  
Tensorflow is introduced, and the concept of computational graphs.  Tensorflow is used to perform basic matrix operations at first, but quickly builds to using neural network concepts and advanced Tensorflow syntax to recognize digits in the seminal MNIST dataset using a Multi-Layer Perceptron (MLP) network.

Part 2
^^^^^^

A more advanced architecture - the Convolutional Neural Net (CNN) - with significant advantages over MLPs in many domains is described.  Image kernels are introduced, and then how these kernels create feature maps that illustrate hierarchical learning of features is demonstrated.  Tensforflow syntax specific to CNNs is provided in examples, and culminates in using creating a CNN to classify images in the CIFAR-10 dataset.
   

Part 3
^^^^^^

So much data is sequential.  Interpreting meaning from data in diverse fields such as language, music, stock prices, and genes all require context and "remembering" data that has come before.  Recurrent Neural Networks (RNNs) can successfully model this type of data.  The basics of RNNs and their implementaion in Tensorflow are covered and a specific type of RNN - an LSTM (Long-Short-Term-Memory) is used in seq2seq to model a simple numerical sequence.

Part 4
^^^^^^

Data are often complicated, noisy, and exist in high-dimensional spaces.  Autoenoders can find simpler representations of the data and find uses in many tasks: compression, dimension reduction, and recently as generative models.  The theory behind autoencoders is presented in the morning with examples showing its use in dimension reduction, and then a generative variational autoencoder is used to reconstruct images in the MNIST dataset.


Links
-----

.. toctree::
   :maxdepth: 1

   00-overview
   01-getting-started
   02-introduction
   03-part-1
   04-part-2
   05-part-3
   06-part-4
