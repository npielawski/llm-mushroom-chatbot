# LLM and Societal Consequences of AI - Lab and Assignment

This repository contains the boilerplate code and exercises of the lab and assignement of the
course "Large Language Models and Societal Consequences of Artificial Intelligence"
(1RT730) at the University of Uppsala.

Feel free to look and try these exercises before-hand, attending the lab is optional and
is allocated to help students with problems or questions.

The goal of the lab sessions is to provide hands-on experience with the tools and
methods necessary to build an AI chatbot using pretrained models locally or in the
cloud.

There are two main parts to the lab sessions:
1. Getting acquainted with the AI models API, it has two path (choose one):

   a. Using Google's Gemini API in the cloud (recommended).

   b. Using the Huggingface API on your machine (requires a decent hardware setup).

Using the knowledge gained through the lab exercises you will then complete the assignment: 
* Building a chatbot using the results from the previous step. The chatbot is a
   mushroom expert that can answer questions about mushrooms, and work with images.

## Installation

The code runs on Python, there are three ways you can proceed with the installation:
1. Install docker and use the provided docker compose configuration.
2. Install Python with mamba/conda and install the provided environment.txt files.
3. Install Python and install the required packages manually (not recommended).

The instructions are detailed in [installation.md](installation.md).

## Lab Exercises

Complete one of the notebooks depending on the path you choose. The notebooks
have exercises that you can complete to get a better understanding of the API and the
models. They give you a good starting point for building the chatbot for the assignment.

It is advised to complete the exercises of the lab before moving to the assignment.

### Part 1.a.: Using the Gemini API

The notebook `part_1a_gemini.ipynb` contains all the exercises for the Gemini API. Just
start a Jupyter notebook server and open the notebook to start working on the exercises.

### Part 1.b.: Using the Huggingface API

The notebook `part_1b_huggingface.ipynb` contains all the exercises for the Huggingface
API. Just start a Jupyter notebook server and open the notebook to start working on the
exercises.

## Assignment: Building a Mushroom Chatbot
After the completion of the Lab, you are welcome to start working on the assignment. 
Here, you will be developing the mushroom chatbot presented during the lab seminar.

The python file `part_2_mushroom_chatbot.py` contains boilerplate code for building the
mushroom chatbot using Gradio. The code contains the instructions for the exercises you
need to complete to build the chatbot in the form of comments.

The goal of the chatbot is to be able to answer questions about mushrooms and process
images of mushrooms. The chatbot should be able to provide information about images of
mushrooms and answer questions about them.

Write a report (in any format you like) that contains the answers to the questions in
`Things to check` and the code for the exercises in `Main exercises`. The report should
also contain examples of the chatbot responses for the exercises. Submit the report, alongside your code,
through [Canvas](https://uppsala.instructure.com/courses/94786/assignments/280275).

#### Main exercises:
 1. Add the Gemini (or HuggingFace) chatbot to the interface.
 2. Make the chatbot multimodal so that it can read mushroom images.
 3. Add instructions to the chatbot, so that it behaves like a mushroom expert, and
    that it stirs the conversation in the right direction (i.e. mushrooms related).
 4. Stream the answers and display the chunks of text as they are being processed.
 5. (Gemini only) Print a message when the chatbot's safety filter is triggered.
 6. (Gemini only) If the streaming fails, it is not possible to keep the conversation going. Add
    a try catch block to handle this situation (tip: use the rewind function for
    Gemini).
 7. When the chatbot receives an image, ask it to produce a JSON response with the
    following fields: common_name, genus, confidence (of the prediction), visible
    (what parts of the mushrooms are visible in the image, from the set {cap,
    hymenium, stipe}, the color of the mushroom in the picture and the edibility of
    the mushroom.
    As an example:
    ```json
    {
      "common_name": "Inkcap",
      "genus": "Coprinus",
      "confidence": 0.5,
      "visible": ["cap", "hymenium", "stipe"],
      "color": "orange",
      "edible": true
    }
    ```
    Do not display the information in the chatbot, but print it in the console.
    Let the chatbot keep this information in mind for the next questions.
 8. If the user asked a question when they sent the image, after processing said image,
    answer the question, but if no questions were asked, provide a summary of the
    processed image, using the information in the JSON response.

#### Things to check (after completing the exercises):
 1. Assess if the model can correctly classify mushrooms? (The value is in the
    quality of your assessment, not the result itself.)
    Note: the model cannot classify the parasol mushroom as all information is not
    visible in the image (the stipe is missing). What happens in this case?
 2. The model is likely not consistent in its predictions (e.g. ask twice to classify
    the same image). One way is to change the temperature of the model and set it to 0.0
    from now on. Note that this solves the problem of reproducibility, and is generally
    considered a good practice, but doesn't guarantee consistency. What other causes
    could lead to inconsistent predictions?
 2. Can you find a way to make the chatbot talk about another topic than mushrooms?
    Is it hard? If not, how would you make it harder?
 3. Can you ask the chatbot to transcribe the text in the `nya_svampboken_p226.jpg`
    file? Did it do a good job? Are things reinterpreted or missing?
 4. To transcribe the page from `Nya svampboken`, you may have had to lower the safety
    of the model. What are the risks and consequences of doing so?
 5. Does the chatbot provide accurate descriptions given the instructions of
    exercise 7. and 8.? Specifically, is the JSON format correct? Are the fields
    correctly filled? Are the answers relevant? Does the summary correspond to the
    JSON response?
 6. Can you check the quality of the chatbot's answers? How would you do that? Try
    the mushroom_*.jpg images in the `data` folder with various models of various
    complexities. What are the results? What are the limitations of a mushroom expert
    chatbot?
 7. The Amanita Muscaria (the red mushroom with white dots) is a famous mushroom. It
    contains a neurotoxin that can cause delirium among other symptoms, but it is
    generally not deadly. It can be eaten if prepared correctly. Can you find a way to
    make the chatbot provide this information? Now, how can you make sure that the
    chatbot does not provide this information to someone who would eat the mushroom
    without proper preparation?
 7. Can you find a way to make the chatbot more engaging? How would you do that?

#### Optional exercises:
 1. Add a description to the chat interface.
 2. Add a theme to the chat interface.
 3. Add a few examples to the chat interface.

#### Evaluation

Some of the exercises are more challenging than others and a few even do not have a
clear solution. The evaluation will be based on the quality of the implementation, the
understanding of the concepts, and the creativity of the assessment in `Things to check`.

## Issues

If you encounter any issues, feel free to
[open an issue](https://github.com/npielawski/llm-mushroom-chatbot/issues) in the
repository or contact us through Canvas.
