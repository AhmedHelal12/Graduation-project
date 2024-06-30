import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
import os
import pyttsx3
from gtts import gTTS

nltk.download('stopwords')
nltk.download('punkt')

def read_article(article):
    sentences = nltk.sent_tokenize(article)
    return sentences

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []

    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    # Build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1

    # Build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i == j:
                continue
            similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j], stop_words)

    return similarity_matrix

def generate_summary(article, top_n=5):
    stop_words = set(stopwords.words('english'))
    sentences = read_article(article)
    sentence_similarity_matrix = build_similarity_matrix(sentences, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)

    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    
    summary = ""
    for i in range(top_n):
        summary += ranked_sentences[i][1] + " "

    return summary

# abs_path = os.getcwd()
# # Input text to be summarized
# with open(f'{abs_path}/input_text.txt', 'r') as file:
#     input_text = file.read()

# # Generate the summary
# summary = generate_summary(input_text, top_n=10)

# with open(f'{abs_path}/generated.txt', 'w') as file:
#     file.write(summary)

# Initialize the gTTS object with the text and language
# tts = gTTS(text=summary, lang='en')

# # Set properties (adjust as needed)
# tts.speed = 1.5  # Speed of speech (1.0 is the default, higher values are faster)
# tts.volume = 0.7  # Volume (0.0 to 1.0)

# # Save the speech audio into a file
# audio_file_path = "audio1.mp3"
# tts.save(audio_file_path)

