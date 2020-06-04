.. Neural Networks with Tensorflow

Getting started
===============

Installation
------------
With only a couple days to spend on this rich, challenging material, it would be a shame to waste time troubleshooting IT and program installation issues.  For this reason we recommend installing Docker, and then installing the Linux Tensorflow Docker image.  See the steps below for this straightforward installation process.


Docker
^^^^^^

:download:`Docker slides. <../slides/dlw_docker.pdf>`

Installation directions for your operating system:

* `Ubuntu <https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/>`_  
* `MacOs <https://docs.docker.com/docker-for-mac/install/>`_  
* `Windows - Docker Toolbox for Windows <https://docs.docker.com/toolbox/overview/#whats-in-the-box>`_   

Tensorflow
^^^^^^^^^^

:download:`Tensorflow introduction slides. <../slides/dlw_tensorflow_intro.pdf>`

We'll all be installing the same docker image that also mounts a data storage volume::

   $ docker run -it --name tf_container --mount source=tf_volume,target=/notebooks -p 8888:8888 gcr.io/tensorflow/tensorflow:latest-py3

If you have follow-up questions see the directions `here. <https://www.tensorflow.org/install/install_linux#InstallingDocker>`_  

The workshop uses data and examples that should train quickly enough without a GPU.  Even if you have a GPU please use the image above.

Moving files in/out of your volume
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Workshop notebooks and data will be added as the course proceeds. You can copy needed files into your docker volume using the `docker cp` command::

   $ docker cp <file> tf_container:/notebooks

To copy files that are in the volume to a desired directory, navigate to that directory and reverse the order of the arguments above.

