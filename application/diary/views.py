from django.shortcuts import render
from .models import Diary
from .sentimentAnalysis import analyse
def mydiary(request):
    user = request.user
    print(user)
    diarys = Diary.objects.all()

    return render(request, 'collection.html', {'diarys': diarys})


def postDiary(request):
    if request.method == 'POST':
        # title = request.POST['title']
        content = request.POST['title']
        mood =analyse(content) # Using cohere to get the decision based on mood
        # user = request.user
        diary = Diary(content=content, mood=mood)
        diary.save()
        return render(request, 'write.html')
    else:
        return render(request, 'write.html')


def deleteDiary(request):
    if request.method == 'POST':
        diary_id = request.POST['diary_id']
        diary = Diary.objects.get(id=diary_id)
        diary.delete()
        return render(request, 'mydiary.html')
    else:
        return render(request, 'mydiary.html')
    


def home(request):
    data = Diary.objects.all()
    score = 0
    for i in data:
        if(i.mood !='sadness'):
            score +=5
        if(i.mood == 'sadness'):
            score -=2
    return render(request, 'home.html', {'data': score})

def mood(request):
    return render(request,'music.html')