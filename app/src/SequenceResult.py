class SequenceResult:
    def __init__(self):
        self._result = list()

    
    def get_name(self):
        return self._name


    def get_matrix(self):
        return self._matrix


    def get_seq(self):
        return self._seq


    def get_threshold(self):
        return self._threhold


    def get_result(self):
        return self._result


    def set_name(self, name):
        self._name = name


    def set_seq(self, seq):
        self._seq = seq


    def set_threshhold(self, threshold):
        self._threshold = threshold


    def set_result(self, result):
        self._result = result


    def set_matrix(self, matrix):
        self._matrix = matrix


    def append_pos_score(self, pos_score):
        self._result.append(pos_score)


    def remove_pos_score(self, pos_score):
        self._result.remove(pos_score)

    def __str__(self):
        name = str(self.get_name()) + ":\n\t\t"
        str_result = ""
        for seq in self.get_result():
            str_result =  str_result + str(seq) + "\n\t\t"
        return name + str_result

