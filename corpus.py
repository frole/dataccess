class Corpus(object) :
    def __init__(self, corpus_name) :
        self.name = corpus_name

    def get_raw_documents(self) :
        pass

    def get_tokenized_documents(self) :
        pass

    def get_tokenized_digitized_documents(self) :
        pass

    def get_tokenized_sentences(self) :
        pass

    def get_tokenized_digitized_sentences(self) :

    def get_document_labels(self) :
        pass

    def get_document_term_matrix(self):
        pass

    def get_tfidf_document_term_matrix(self):
        pass

    def get_frequency(self, word) : 
        pass

    def get_oov(self, word):
        pass

    def get_contexts(self, word, window_size) :
        """"""
        def find_context_of_a_occurrence_in_a_sentence(word_index, window_size, s):
            max_length = len(s)
            left_border = word_index - window_size
            left_border = 0 if word_index - window_size < 0 else left_border
            right_border = word_index + 1 + window_size
            right_border = max_length if right_border > max_length else right_border
            return s[left_border:word_index] + s[word_index+1: right_border]
        
        all_contexts = []
        if not self.tokenized_sentences :
           tokenized_sentences = self.get_tokenized_texts()
        for s in tokenized_sentences :
            target_word_indices = [i for i, e in enumerate(s) if e == word]
            for target_word_index in target_word_indices :
               all_contexts.extend(find_context_of_a_occurrence_in_a_sentence(target_word_index,
                                                       window_size, s) )
        return all_contexts



    
