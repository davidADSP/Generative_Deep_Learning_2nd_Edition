# 🐳 Getting started with Docker

Before we start, you will need to download Docker Desktop for free from https://www.docker.com/products/docker-desktop/

In this section, we will explain the reason for using Docker and how to get started.

The overall structure of the codebase and how Docker can be used to interact with it is shown below.

<img src="../img/structure.png">

We will run through everything in the diagram in this `README`.

## 🙋‍♂️ Why is Docker useful?

A common problem you may have faced when using other people's code is that it simply doesn't run on your machine. This can be especially frustrating, especially when it runs just fine on the developer's machine and they cannot help you with specific bugs that occur when deploying onto your operating system.

There are two reasons why this might be the case:

1. The underlying Python version or packages that you have installed are not identical to the ones that were used during development of the codebase

2. There are fundamental differences between your operating system and the developer's operating system that mean that the code does not run in the same way.

The first of these problems can be mostly solved by using *virtual environments*. The idea here is that you create an environment for each project that contains the required Python interpreter and specific required packages and is separated from all other projects on your machine. For example, you could have one project running Python 3.8 with TensorFlow 2.10 and another running Python 3.7 with TensorFlow 2.8. Both versions of Python and TensorFlow would exist on your machine, but within isolated environments so they cannot conflict with each other. 

Anaconda and Virtualenv are two popular ways to create virtual environments. Typically, codebases are shipped with a `requirements.txt` file that contains the specific Python package versions that you need to run the codebase.

However, solely using virtual environments does not solve the second problem - how can you ensure that your operating system is set up in the same way as the developer's?  For example, the code may have been developed on a Windows machine, but you have a Mac and the errors you are seeing are specific to macOS. Or perhaps the codebase manipulates the filesystem using scripts written in `bash`, which you do not have on your machine.

Docker solves this problem. Instead of specifying only the required Python packages, the developer specifies a recipe to build what is known as an *image*, which contains everything required to run the app, including an operating system and all dependencies. The recipe is called the `Dockerfile` - it is a bit like the `requirements.txt` files, but for the entire runtime environment rather than just the Python packages.

Let's first take a look at the Dockerfile for the Generative Deep Learning codebase and see how it contains all the information required to build the image.

## 📝 The Dockerfile

In the codebase that you pulled from GitHub, there is a file simply called 'Dockerfile' inside the `docker` folder. This is the recipe that Docker will use to build the image. We'll walk through line by line, explaining what each step does.

```
FROM ubuntu:20.04 #<1>
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update #<2>
RUN apt-get install -y unzip graphviz curl musescore3 python3-pip

RUN pip install --upgrade pip #<3>

WORKDIR /app #<4>

COPY ./requirements.txt /app #<5>
RUN pip install -r /app/requirements.txt

# Hack to get around tensorflow-io issue - https://github.com/tensorflow/io/issues/1755
RUN pip install tensorflow-io
RUN pip uninstall -y tensorflow-io

COPY /notebooks/. /app/notebooks #<6>
COPY /scripts/. /app/scripts

ENV PYTHONPATH="${PYTHONPATH}:/app" #<7>
```

1. The first line defines the base image. Our base image is an Ubuntu 20.04 (Linux) operating system. This is pulled from DockerHub - the online store of publicly available images (`https://hub.docker.com/_/ubuntu`).
2. Update `apt-get`, the Linux package manager and install relevant packages
3. Upgrade `pip` the Python package manager
4. Change the working directory to `/app`.
5. Copy the `requirements.txt` file into the image and use `pip` to install all relevant Python packages
6. Copy relevant folders into the image
7. Update the `PYTHONPATH` so that we can import functions that we write from our `/app` directory

You can see how the Dockerfile can be thought of as a recipe for building a particular run-time environment. The magic of Docker is that you do not need to worry about installing a resource intensive virtual machine on your computer - Docker is lightweight and allows you to build an environment template purely using code.

A running version of an image is called a *container*. You can think of the image as like a cookie cutter, that can be used to create a particular cookie (the container). There is one other file that we need to look at before we finally get to build our image and run the container - the docker-compose.yaml file.

## 🎼 The docker-compose.yaml file

Docker Compose is an extension to Docker that allows you to define how you would like your containers to run, through a simple YAML file, called 'docker-compose.yaml'.

For example, you can specify which ports and folders should be mapped between your machine and the container. Folder mapping allows the container to treat folders on your machine as if they were folders inside the container. Therefore any changes you make to mapped files and folders on your machine will be immediately reflected inside the container. Port mapping will forward any traffic on a local port through to the container. For example, we could map port 8888 on your local machine to port 8888 in the container, so that if you visit `localhost:8888` in your browser, you will see Jupyter, which is running on port 8888 inside the container. The ports do not have have to be the same - for example you could map port 8000 to port 8888 in the container if you wanted.

The alternative to using Docker Compose is specify all of these parameters in the command line when using the `docker run` command. However, this is cumbersome and it is much easier to just use a Docker Compose YAML file. Docker Compose also gives you the ability to specify multiple services that should be run at the same time (for example, a application container and a database), and how they should talk to each other. However, our purposes, we only need a single service - the container that runs Jupyter, so that we can interact with the generative deep learning codebase.

Let's now take a look at the Docker Compose YAML file.

```
version: '3' #<1>
services: #<2>
  app: #<3>
    build: #<4>
      context: .
      dockerfile: ./docker/Dockerfile
    tty: true #<5>
    volumes: #<6>
      - ./data/:/app/data
      - ./notebooks/:/app/notebooks
      - ./scripts/:/app/scripts
    ports: #<7>
        - "$JUPYTER_PORT:$JUPYTER_PORT"
        - "$TENSORBOARD_PORT:$TENSORBOARD_PORT"
    env_file: #<8>
     - ./.env
    entrypoint: jupyter lab --ip 0.0.0.0 --port=$JUPYTER_PORT --no-browser --allow-root #<9>
```

1. This specifies the version of Docker Compose to use (currently version 3)
2. Here, we specify the services we wish to launch
3. We only have one service, which we call `app`
4. Here, we tell Docker where to find the Dockerfile (the same directory as the docker-compose.yaml file)
5. This allows us to open up an interactive command line inside the container, if we wish
6. Here, we map folders on our local machine (e.g. ./data), to folders inside the container (e.g. /app/data).
7. Here, we specify the port mappings - the dollar sign means that it will use the ports as specified in the `.env` file (e.g. `JUPYTER_PORT=8888`)
8. The location of the `.env` file on your local machine.
9. The command that should be run when the container runs - here, we run JupyterLab.

## 🧱 Building the image and running the container

We're now at a point where we have everything we need to build our image and run the container. Building the image is simply a case of running the command shown below in your terminal, from the root folder.

```
docker compose build
```

You should see Docker start to run through the steps in the Dockerfile. You can use the command `docker images` to see a list of the images that have been built on your machine.

To run the container based on the image we have just created, we use the command shown below:

```
docker compose up
```

You should see that Docker launches the Jupyter notebook server within the container and provides you with a URL to the running server.

Because we have mapped port 8888 in the container to port 8888 on your machine, you can simply navigate to the address starting `http://127.0.0.1:8888/lab?token=` into a web browser and you should see the running Jupyter server. The folders that we mapped across in the `docker-compose.yaml` file should be visible on the left hand side.

Congratulations! You now have a functioning Docker container that you can use to start working through the Generative Deep Learning codebase! To stop running the Jupyter server, you use `Ctrl-C` and to bring down the running container, you use the command `docker compose down`. Because the volumes are mapped, you won't lose any of your work that you save whilst working in the Jupyter notebooks, even if you bring the container down.

## ⚡️ Using a GPU

The default `Dockerfile` and `docker-compose.yaml` file assume that you do not want to use a local GPU to train your models. If you do have a GPU that you wish to use (for example, you are using a cloud VM), I have provided two extra files called `Dockerfile-gpu` and `docker-compose.gpu.yml` files that can be used in place of the default files.

For example, to build an image that includes support for GPU, use the command shown below:

```
docker compose -f docker-compose.gpu.yml build
```

To run this image, use the following command:

```
docker compose -f docker-compose.gpu.yml up
```
