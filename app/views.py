from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def PDF(request):
    if request.method=='POST':
         coca=request.POST.get('coka')
         pepsi=request.POST.get('pepsi')
         sting=request.POST.get('sting')
         fanta=request.POST.get('fanta')
         dt=request.POST.get('dt')
         coka_rs=100
         pepsi_rs=200
         sting_rs=300
         fanta_rs=200
         total=(int(coca)*coka_rs+int(pepsi)*pepsi_rs+int(sting)*sting_rs+int(fanta)*fanta_rs)
         data={
                'coka':coca,
                'pepsi':pepsi,
                'sting': sting,
                'fanta':fanta,
                'dt':dt,
                'total':total,
                
             }
    return render(request,'pdf.html',data)
