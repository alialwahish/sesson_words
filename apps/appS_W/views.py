from django.shortcuts import render , redirect
from time import gmtime, strftime
def index(request):
    
    
    return render(request,'appS_W/index.html')

def reset(request):
    request.session['words']=[]
    return redirect('/session_words')
        
def process(request):
       
    if request.method=='POST':
        
        temp_list = request.session['words']
        # temp_list.append(str(request.POST['word'])+"&"+str(request.POST['color']+"&"))
        
        if request.POST.get('isBig'):
            print("Checked")
            # temp_list.append("Checked")
            stat=True    
        else:
            print("unchecked")
            # temp_list.append("Checked")
            stat=False
        temp_list.append({'word':request.POST['word'],'color':request.POST['color'],'isBig':stat,'time':strftime("%Y-%m-%d %H:%M:%S", gmtime())})
        request.session['words'] = temp_list
        
       
        
        print(temp_list[0]['word'])
    # return render(request,'appS_W/index.html',{'code':temp_list})
    
    return redirect('/session_words')