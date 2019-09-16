from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.template import loader  
from . import predictor
import pickle , os
# Create your views here.


@xframe_options_exempt
def predict(request):
    mapped_data = {
        "age" : int(request.GET.get("age")) , 
        "sex" : int(request.GET.get("sex")) , 
        "bmi" : float(request.GET.get("bmi")) , 
        "children" : int(request.GET.get("children")),
        "smoker" : int(request.GET.get("smoker"))
    }

    prediction = predictor.get_predictions(mapped_data)

    filename = 'PredictionPresenter\\prediction.value'
    pickle.dump(prediction, open(filename, 'wb'))
    
    return HttpResponse("Success")

def load_prediction(request):
    path = "{}\\PredictionPresenter".format(os.getcwd())
    prediction = pickle.load(open(path+"\\prediction.value", 'rb'))

    template = loader.get_template('index.html')
    
    message = "Profile Seems Positive for Approval"
    color = "green"

    if prediction == 0:
        message = "Profile Seems Negative for Approval"
        color = "red"

    name = {
        "message" : message ,
        "color" : color
    }
    return HttpResponse(template.render(name))