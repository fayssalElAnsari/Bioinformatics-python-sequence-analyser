class MatrixResult:
    def __init__(self):
        self._result = list()

    
    def get_name(self):
        return self._name


    def get_seq_list(self):
        return self._matrix


    def get_threshold(self):
        return self._threhold


    def get_result(self):
        return self._result


    def set_name(self, name):
        self._name = name


    def set_seq_list(self, matrix):
        self._matrix = matrix


    def set_threshhold(self, threshold):
        self._threhold = threshold


    def set_matrix(self, matrix):
        self._matrix = matrix


    def set_result(self, result):
        self._result = result


    def append_scan_result(self, seq_pos_score):
        self._result.append(seq_pos_score)

    def __str__(self):
        return str(self.get_name()) + ": " + str([str(result) for result in self.get_result()])

    
