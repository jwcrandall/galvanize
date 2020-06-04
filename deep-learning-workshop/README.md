# Galvanize Deep Learning Workshop

This is a five-part short course on neural networks implemented in Tensorflow.  The parts are three hour blocks containing the following content:  
- Part 0: Installs and Introduction to Docker and Tensorflow  
- Part 1: Multilayer perceptron neural networks   
- Part 2: Convolutional neural networks  
- Part 3: Recurrent neural networks  
- Part 4: Autoencoders  

#### For students
The project is built in [Sphinx](http://www.sphinx-doc.org/en/stable/).  You can view the present state of this workshop by cloning it and then:  
```
$ cd src/_build
$ firefox index.html
```
You don't need to use Firefox, any browser should work.

#### Modifying the course (for instructors)
Sphinx uses reStructuredText (.rst) instead of Markdown, but syntax is similar.  The `src/index.rst` is the master document which serves as the welcome page and hosts the Table of Contents.

If you make changes to the reStructuredText files (i.e. the \*.rst files in `src`) you can re-complile the code and make new html files by navigating to the `src` folder and typing  
```
$ make html  
```

Before this `make` command will work you'll likely need to install some Sphinx dependencies.  It's straight-forward.

Adam Richard's Short Course (also built and deployed in Sphinx) has been a useful Sphinx reference during this workshop's development.  Here's a link to his [Statistics Short Course.](https://github.com/GalvanizeOpenSource/stats-shortcourse)


