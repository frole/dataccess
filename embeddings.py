class Embeddings(object) :
    def __init__(self, embeddings_name) :
        self.name = embeddings_name 

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


