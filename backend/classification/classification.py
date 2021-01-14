from backend.api.models import ClassificationRequest


class Classification:
    def __init__(self, request: ClassificationRequest):
        self.request = request
        self.X = []
        self.Y = []
        
    def parse_request(self):
        for cl_obj in self.request.data:
            target_val = cl_obj.index
            self.X += cl_obj.points
            self.Y += [target_val for _ in range(len(cl_obj.points))]
        print(self.X)
        print(self.Y)
        
    
    def preprocess_data(self):
        pass
    
    
    def build_model(self):
        pass
    
    
    def train_model(self):
        pass
    
    
    def evaluate(self):
        pass
    
    
    def main(self):
        self.parse_request()
        self.preprocess_data()
        self.build_model()
        self.train_model()
        self.evaluate()
        
        return "das ist das Ergebniss"
    
    
class Svm(Classification):
    pass


class RandomForest(Classification):
    pass