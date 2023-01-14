class SentimentLexicon:
    def __init__(self):
        self.dictionary: dict = self.load_dictionary("./positive-words.txt", "./negative-words.txt")


    def load_file(self, src: str, sentiment_val: int) -> dict:
        # load a single file and return a dictionary that contains all the words that aren't commented out with a ;
        result = {}
        with open(src, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(";") or line.strip() == "":
                    continue
                result[line.lower().strip()] = sentiment_val
        return result
    

    def load_dictionary(self, pos_src: str, neg_src: str) -> dict:
        # load all source files and return a mixed dictionary of good and bad words
        pos_dictionary = self.load_file(pos_src, 1)
        neg_dictionary = self.load_file(neg_src, -1)
        return { **pos_dictionary, **neg_dictionary }


class Classifier:
    def __init__(self):
        self.sentiment_lexicon = SentimentLexicon()


    def split_txt(self, txt: str):
        # This splits the sentence and removes pre-defined punctuations to make it easier to match with sentiment dictionary values 
        txt_array = txt.lower().strip().split()
        punctuations = [",", ".", "!"]
        result = []
        for word in txt_array:
            wrd_stripped = word.strip()
            for punctuation in punctuations:
                if wrd_stripped.startswith(punctuation) or wrd_stripped.endswith(punctuation):
                    wrd_stripped = wrd_stripped.strip(punctuation)

            result.append(wrd_stripped)

        return result



    def classify(self, txt: str) -> int:
        dictionary = self.sentiment_lexicon.dictionary
        total = 0
        txt_array = self.split_txt(txt)

        # check if word exists in the dictionary and add the value to the total if it exists, else add 0
        for word in txt_array:
            score = dictionary[word] if word in dictionary else 0
            total += score
        
        # check if total is 0, positive or negative and return the right sentiment rating (1, -1 or 0)
        sentiment = 0 if total == 0 else 1 if total > 0 else -1

        return sentiment




"""
Main program to simulate a couple of sentiment analysis 
"""

def main():
    classifier = Classifier()
    sentences = ["I love Python.", "Python is the language I love!", "The iPhone is clearly not the most terrible and worst phone ever. It is the best."]

    # classify test cases and print them out
    for sentence in sentences:
        sentiment = classifier.classify(sentence)
        print("{'text': ",sentence, "'sentiment':",sentiment, "}")


if __name__ == "__main__":
    main()
