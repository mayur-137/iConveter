from django.shortcuts import render, redirect
from .serializer import PopularFeaturesSerializers, AllFeaturesSerializers
from .models import PopularFeatures, AllFeatures, FeatureDetails, FileUpload
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from .FeaturesAll import ConvertJPG_PNG
from PIL import Image


FunContainer = []
urlStorage = []


# home page
def index(request):
    myObj = PopularFeatures.objects.all()
    # serializer = PopularFeaturesSerializers(myObj, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # print(res)
    return render(request, 'apis/Home.html', {'res': myObj})


def Verify(request):
    if request.method == "POST":
        upload = request.FILES['file']
        FnName = request.POST.get('FnName')
        fs = FileSystemStorage()
        don = fs.save(upload.name, upload)
        ConvertJPG_PNG(upload.name)
        a = fs.url(upload.name)
        # urlStorage.append(a)
        return render(request, 'apis/Fetures-update-page.html', {'fileName': upload.name, 'url':a})
    else:
        return HttpResponse("sorry")


def Merged(request):

    return HttpResponse("done")


def SplitPDF(request):
    return HttpResponse("done")


def CompressPDF(request):
    return HttpResponse("done")


def PDFtoWORD(request):
    return HttpResponse("done")


def WORDtoPDF(request):
    return HttpResponse("done")


def PDFtoPOWERPOINT(request):
    return HttpResponse("done")


def POWERPOINTtoPDF(request):
    return HttpResponse("done")


def EXCELtoPDF(request):
    return HttpResponse("done")


def PDFtoEXCEL(request):
    return HttpResponse("done")


def PDFtoJPG(request):
    return HttpResponse("done")


def JPGtoPNG(request):
    Ext = 'image/jpeg'
    Heading = 'Your JPG file'
    FunctionName = 'ConvertJPG_PNG'
    FunContainer.append(FunctionName)
    print(FunContainer)
    return render(request, 'apis/Fetures-page.html', {'Ext': Ext, 'Heading': Heading, 'FunctionName': FunctionName})


def HTMLtoPDF(request):
    return HttpResponse("done")


def MP4toMP3(request):
    return HttpResponse("done")


def LOCKPDF(request):
    return HttpResponse("done")


def UNLOCKPDF(request):
    return HttpResponse("done")


def REPAIRPDF(request):
    return HttpResponse("done")


def WORDREADER(request):
    return HttpResponse("done")


def EXCELREADER(request):
    return HttpResponse("done")


def POWERPOINTREADER(request):
    return HttpResponse("done")


def EDITPDF(request):
    return HttpResponse("done")


def PAGENUMBER(request):
    return HttpResponse("done")


def WATERMARK(request):
    return HttpResponse("done")


def ROTATEPDFPAGES(request):
    return HttpResponse("done")


def SIGNPDF(request):
    return HttpResponse("done")


def About(request):
    return render(request, 'apis/About.html')


def Contact(request):
    return render(request, 'apis/Contact.html')


def Tools(request):
    AllFeature = AllFeatures.objects.all()
    return render(request, 'apis/All-Features.html', {'Allfeatures': AllFeature})


def Login(request):
    return render(request, 'apis/Login.html')


def SignUp(request):
    return render(request, 'apis/sign-up.html')


def download(request):
    return HttpResponse('aa')


# def FileUpload(request):
#     FDetails = FeatureDetails.objects.all()
#     return render(request, 'apis/Fetures-page.html', {"FDetails": FDetails})


# Fetch data with particular id
def popularFeaturesId(request, id):
    myObj = PopularFeatures.objects.get(id=id)
    serializer = PopularFeaturesSerializers(myObj)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


# fetch all data with queryset
def popularFeatures(request):
    myObj = PopularFeatures.objects.all()
    serializer = PopularFeaturesSerializers(myObj, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


# fetch all features
def allFeatures(request):
    myObj = AllFeatures.objects.all()
    serializer = AllFeaturesSerializers(myObj, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


# fetch data with particular id
def allFeaturesId(request, id):
    myObj = AllFeatures.objects.get(id=id)
    serializer = AllFeaturesSerializers(myObj)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)
