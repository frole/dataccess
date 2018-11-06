class Corpus(object) :
    def __init__(self, corpus_name) :
        self.name= corpus_name

    def get_raw_texts(self) :
        pass

    def get_tokenized_texts(self) :
        pass

    def get_tokenized_digitized_texts(self) :
        pass

    def get_labels(self) :
        pass

    def get_doc_term_matrix(self):
        pass

    def get_frequency(self, word) : 
        pass

    def get_oov(self, word):
        pass

    def get_contexts(self, word, window_size) :
        pass



    
