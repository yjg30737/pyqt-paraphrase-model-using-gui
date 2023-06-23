# pyqt-paraphrase-model-using-gui
Using paraphrase(text2text generation) model from huggingface in Python desktop app

This is using the model <a href="https://huggingface.co/tuner007/pegasus_paraphrase">tuner007/pegasus_paraphrase</a>.

The model's size is approximately 2.3G.

## Requirements
* PyQt5 >= 5.14
* huggingface_hub
* transformers

## How to Run
1. git clone ~
2. pip install -r requirements.txt
3. python main.py
4. see "preview" below

## Preview
![image](https://github.com/yjg30737/pyqt-paraphrase-model-using-gui/assets/55078043/b89f1a0b-e9fa-499f-8ca5-54096309af8b)
* **beam** typically refers to the beam search algorithm used in sequence generation tasks such as machine translation or text generation. Beam search is a heuristic search algorithm that explores multiple possible sequences of tokens during generation and keeps track of a fixed number of most promising sequences called the "beam width."is typically refers to the beam search algorithm used in sequence generation tasks such as machine translation or text generation. In layman's term, it helps the model find the most suitable sequence of words. 
* **return sequences** refers to the number of sentences the model will generate.
* **context** is the context in which you want to perform paraphrasing.

After you click "Submit", model will be downloaded in your PC and this app will perform paraphrasing with that and show you the result in text browser below. 
