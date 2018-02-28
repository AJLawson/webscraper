from bs4 import BeautifulSoup
import requests, string
from collections import Counter

def get_words_list(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    text = soup.findAll('div', {"class":"scrolling-script-container"})[0].text.lower()
    for char in string.punctuation:
        text = text.replace(char, "")
    text_list = text.split()
    words_counts = Counter(text_list).most_common(50)
    return words_counts
    
def main():
    words_list = get_words_list("http://www.springfieldspringfield.co.uk/movie_script.php?movie=finding-nemo")
    print(words_list)

if __name__ == "__main__":
    main()

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

def plot_words(words_list, fname):
    words = []
    numbers = []
    for (w, n) in words_list:
        words.append(w)
        numbers.append(n)

    index = np.arange(len(words))

    fig = plt.figure()
    plt.bar(index, numbers)
    plt.xticks(index + .5, words, rotation="vertical", size="x-small")
    fig.savefig(fname)
    
def main():
    words_list = get_words_list("http://www.springfieldspringfield.co.uk/movie_script.php?movie=finding-nemo")
    plot_words(words_list, "finding_nemo")
	
