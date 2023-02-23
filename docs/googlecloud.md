# ⚡️ Setting up a VM with GPU in Google Cloud Platform

## ☁️ Google Cloud Platform

Google Cloud Platform is a public cloud vendor that offers a wide variety of computing services, running on Google infrastructure. It is extremely useful for spinning up resources on demand, that otherwise would require a large upfront investment in hardware and set up time.

There are many cloud vendors - the largest being Amazon Web Services (AWS), Microsoft Azure and Google Cloud Platform (GCP). Through these cloud platforms, you can spin up servers, databases other services through the online user interface and easily turn them off or tear them down when you are finished using them. This makes cloud computing an excellent choice for anyone who wants to get started with state-of-the-art machine learning, because you can get access to powerful resources at the click of a button, without having to invest significant amounts of money in your own hardware.

In this book, we will demonstrate how to set up a virtual server with a GPU on Google Cloud Platform. You can use this environment to run the codebase that accompanies this book on accelerated GPU hardware, for faster training.

## 🚀 Getting started

### Get a Google Cloud Platform Account

Firstly, you'll need a Google Cloud Console account - visit https://cloud.google.com/cloud-console/ to get set up.

If you've never used GCP, you get access to $300 free credit over 90 days (correct at time of writing), which is more than enough to run all of the training examples in this book.

Once you're logged in, the first thing you need to do is create a project. You can call this whatever you like, for example `generative-deep-learning`. Then you have to set up a billing account for the project - if you are using the free trial credits, you will not be automatically billed after the credits are used up.

You can now go ahead and set up a compute engine with an attached GPU, within this project. You can see which project you are currently in next to the Google Cloud Platform logo in the top left corner of the screen.

### Set up a compute engine

Firstly, search for 'Compute Engine' in the search bar and click 'Create Instance' (or navigate straight to https://console.cloud.google.com/compute/instancesAdd

You will see a screen where you can select the configuration of your virtual machine (VM). Below, we run through a description of each field and a recommended value to choose.

| Option | Description | Example Value
| --- | --- | --- 
| Name | What you would like to call the compute instance? | gdl-compute
| Region | Where the compute instance should be physically located? | us-central1-c (Iowa)
| Machine family | What type of machine would you like? | GPU
| GPU type | What GPU would you like? | NVIDIA Tesla T4
| Machine type | What specification of machine would you like? | n1-standard-4 (4vCPU, 15 GB memory)
| Boot disk > Operating System| What boot disk OS would you like? | Deep Learning on Linux

All other options can be left as the default.

The NVIDIA Tesla T4 is a sufficiently powerful GPU to use to run the examples in this book. Note that other more powerful GPUs are available, but these are more expensive per hour. Choosing the 'Deep Learning on Linux' boot disk means that the NVIDIA CUDA stack will be installed automatically at no extra cost.

You may wish to select a different region for your machine - price does vary between regions and some regions are not compatible with GPU (see https://cloud.google.com/compute/docs/gpus/gpu-regions-zones for the full list of GPU regions). In the `us-central1-c` region, the whole virtual machine should be priced at around $0.55 per hour (without any sustained use discount applied).

Click 'Create' to build your virtual machine - this may take a few minutes. You'll be able to see when the machine is ready to access, as there will be a green tick next to the machine name.

### Accessing the VM

The easiest way to access the VM is by using the Google Cloud CLI and Visual Studio Code.

Firstly, you'll need to install the Google Cloud CLI onto your machine. You can do this by following the instructions at the following link: https://cloud.google.com/sdk/docs/install

Then, to set up the configuration for the SSH connection to your virtual machine, first run the command below in your local terminal:

```
gcloud compute config-ssh
```

Then run the command shown below to connect to the virtual machine, replacing `<VM_NAME>` with the name of your virtual machine (e.g. `gdl_compute`).

```
gcloud compute ssh <VM_NAME>
```

The first time you connect, it will ask if you want to install NVIDIA drivers - select 'yes'.

To start coding on the VM, I recommend installing VSCode from https://code.visualstudio.com/download, which is a modern Interactive Development Environment (IDE) through which you can easily access you virtual machine and manipulate the file system.

Make sure you have the Remote SSH extension installed (see https://code.visualstudio.com/blogs/2019/10/03/remote-ssh-tips-and-tricks).

In the bottom left-hand corner of VSCode, you'll see a green box with two arrows - click this and then select 'Connect Current Window to Host'. Then select your virtual machine. VSCode will then connect via SSH. Congratulations - you are now connected to the virtual machine!

### Cloning the codebase

You can then clone the codebase onto the VM:

```
git clone https://github.com/davidADSP/Generative_Deep_Learning_2nd_Edition.git
```

Then in VSCode, if you click 'Open Folder', you can select the folder that you have just cloned into, to see the files in the repository.

Lastly, you'll need to make sure that Docker Compose is installed on the virtual machine using the commands shown below

```
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

Now you can build the image and run the container, using the GPU-specific commands discussed in the main `README` of this codebase.

Congratulations - you're now running the Generative Deep Learning codebase on a cloud virtual machine, with attached GPU!

If you navigate to `http://127.0.0.1:8888/` in your browser, you should see Jupyter Lab, as VS Code automatically forwards the Jupyter Lab port in the container to the same port on your machine. If not, check that the ports are mapped under the 'Ports' tab in VSCode.

## 🚦 Starting and stopping the virtual machine

When you are not using the virtual machine, it's important to turn it off so that you don't incur unnecessary charges.

You can do this by selecting 'Stop' in the dropdown menu net to your virtual machine, in GCP. A stopped virtual machine will not be accessible via SSH, but the storage will be persisted, so you will not lose any of your files or progress. The storage will still incur a small charge.

To turn the virtual machine back on, select 'Start / Resume' from the dropdown menu net to your virtual machine, in GCP. This will take a few minutes. When the green tick appears next to the machine description, you'll be able to access your machine in VS Code as before.

### Changing IP address

When you stop and restart your virtual machine, the external IP address of the server may change. You can see the current external IP address of the virtual machine in the console, as shown in <<gcp-vms>>. If this happens, you will need to update the external IP address of the aliased SSH connection, which you can do within VS Code.

Firstly, click on the green SSH connection arrows in the bottom left-hand corner of VS Code and then 'Open SSH Configuration File...'. Select your SSH configuration file and you should see a block of text similar to that shown in <<ssh_config>>. This is the text added by Google Cloud CLI to allow you an easy way to connect to your virtual machine.

To update the external IP address, you just need to change the `HostName` value and save the file.

### Destroying the VM

To completely destroy the machine, select 'Delete' from the dropdown menu net to your virtual machine in GCP. This will completely remove the virtual machine and all attached stored, and there will be no further incurred charges.

In this section, we have seen how to build a virtual machine with attached GPU in Google Cloud Platform, from scratch. This should allow you to build sophisticated generative deep learning models, trained on sophisticated hardware that you can scale to your requirements.