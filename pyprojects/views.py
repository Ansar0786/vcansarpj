from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os
from django.contrib import messages
import pandas as pd

# Create your views here.
def home(request):
    return render(request,'welcome.html')

def appi(request):
    return render(request,'index.html')

def index1(request):

    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file)

        if uploaded_file.name.endswith ('.csv'):
        #save the file in media folder
            savefile = FileSystemStorage( )
            name = savefile.save(uploaded_file.name,uploaded_file)

            #know where to save file
            d = os.getcwd()  # current directory of the project
            file_directory = d +'\media\\' + name
            readfile(file_directory)
            return redirect(results)
        else:
            messages.warning(request, 'File was not uploaded.Please use csv file extension ! ')

    return render(request,'index1.html')

def readfile(filename):
    global rows,columns,data,my_file,missing_values
    my_file = pd.read_csv(filename, sep = '[:;,|_]', engine = 'python')
    data = pd.DataFrame(data=my_file, index=None)

    print(data)

    # rows and columns
    # rows = len(data.axes[0])
    columns = len(data.axes[1])
    # find missing data
    missingsings = [' ? ', ' 0 ', ' -- ']
    null_data = data[data.isnull().any(axis=1)]  # find the missing data
    missing_values = len(null_data)


def results(request):
    message = 'I found : '   + str(columns) + 'columns . Missing data are :'+ str(missing_values)
    messages.warning(request, message)
    return render(request, 'results.html')