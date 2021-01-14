from .classification import Svm, RandomForest
from backend.api.models import ClassificationRequest


def get_model_type(clf_request: ClassificationRequest):
    getter = {
        "svm": Svm,
        "random_forest": RandomForest
    }
    
    model = getter.get(clf_request.model.value, None)
    
    return model(clf_request)