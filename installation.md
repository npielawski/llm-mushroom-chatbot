# Installation

This page is there to help you set up a python environment to run the exercises for the
lab.

You can choose between using docker or using Python with conda/mamba. The docker setup
is the easiest and recommended way to get started.

## Introduction

You first need to download the repository. You can do this by running the following
command:

```bash
git clone https://github.com/npielawski/llm-mushroom-chatbot.git
cd lab-mushroom-chatbot
```

If you chose to run the model locally, you may need to install CUDA if you are running
the model on a GPU. You can find the installation instructions for CUDA at the end of
this document. This option is specific to the Huggingface API, as the Gemini API does
the computation on the server side.

The folder contains the boilerplate code, exercises and data files to test the chatbot.
There is an visual description of the data files in the [transcript.txt](transcript.txt)
file.

## Using docker

The easiest way to get started is to use docker. You can either install docker from
[here](https://docs.docker.com/get-docker/) or install Docker Desktop from
[here](https://www.docker.com/products/docker-desktop).

Docker will compile an image and run a container with all the necessary dependencies
but you will need to choose between using the Gemini API or the Huggingface API, as well
as the hardware acceleration you have available.

First, create a `.env` file with the following content:

```
LLM_PATH=gemini
DEVICE=cpu
```
Set the `LLM_PATH` to `gemini` if you want to use the Gemini API, or `huggingface` if
you want to use the Huggingface API. Set the `DEVICE` to `cpu` if you don't have a GPU
available, `cuda11` if you have a CUDA 11 compatible GPU, or `cuda12` if you have a CUDA
12 compatible GPU.

Make sure to source the `.env` file before running the docker compose command.
Once you have docker installed, you can run the following command to start the lab:

```bash
docker compose up
```

This will start the lab environment and you can access the Jupyter notebook at the
link provided in the terminal, usually `http://localhost:8888`.

If you want to run arbitrary commands on the container, you can run the following
command:

```bash
docker compose exec jupyter <command>
```

You can replace `<command>` with any command you want to run on the container. For
instance `bash` will start a bash shell on the container,
`python3 part_2_mushroom_chatbot.py` will run the `part_2_mushroom_chatbot.py` file on
the container.

### Running gradio in development mode

If you want to run the gradio server in development mode, you can run the following
command:

```bash
docker compose exec jupyter gradio part_2_mushroom_chatbot.py
```

This will start the gradio server and you can access it at `http://localhost:7860`. The
server will automatically reload when you make changes to the code in the
`part_2_mushroom_chatbot.py` file.

### Updating the docker image

If you make any changes to the `Dockerfile` or the `requirements.txt` files, you will
need to rebuild the docker image. You can do this by running the following command:

```bash
docker compose up --build
```

## Using Python with conda/mamba

For this option, you will need to have conda or mamba installed. You can install conda
from
[here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
or mamba from [here](https://mamba.readthedocs.io/en/latest/). We recommend using mamba
as it is faster than conda, but the commands are the same.

You can then create a new environment with the following command:
```bash
mamba env create -n lab-mushroom-chatbot python=3.10
mamba activate lab-mushroom-chatbot
pip install -r requirements_gemini.txt
```

If you want to use the Huggingface API, you can run the following command:
```bash
mamba env create -n lab-mushroom-chatbot python=3.10
mamba activate lab-mushroom-chatbot
pip install -r requirements_huggingface.txt
```

## Using bare Python

If you don't want to use conda or docker, you can install the dependencies with the
following command:
```bash
pip install -r requirements_gemini.txt
```
or
```bash
pip install -r requirements_huggingface.txt
```

This approach is not recommended as it may cause conflicts with your system packages.

## Installing CUDA

In some of the labs and your final Project you will use PyTorch, a GPU-accelerated
Machine Learning framework. To ensure that it can access your GPU (it will make a *big*
difference in how much time you spend staring at your computer while it thinks), you
need to follow some manual installation steps:

1. Make sure you have a [CUDA-enabled](https://developer.nvidia.com/cuda-gpus) or
   [ROCm-enabled](https://github.com/ROCm/ROCm.github.io/blob/master/hardware.md) GPU.
2. If your GPU is ROCm-enabled, install it following the procedure here:
   [ROCm](https://rocmdocs.amd.com/en/latest/). If your GPU is CUDA-enabled, download
   and install its latest version from here:
   [CUDA Downloads](https://developer.nvidia.com/cuda-downloads)
3. Install PyTorch following the instructions shown in the official website:
   [PyTorch - Get started](https://pytorch.org/get-started/locally/).

