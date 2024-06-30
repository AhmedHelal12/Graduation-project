from django.shortcuts import render, redirect
from myapp.forms import SummyForm, AudioForm, PowerPointForm, VideoForm
from myapp.models import Summarization, Audio, PowerPoint, Video
from myapp.ai.summarization import generate_summary
from myapp.ai.convertAudio import audioFun
from myapp.ai.powerpoint import create_powerPoint
# from myapp.ai.Easy_Wav2Lip.comput import update_video

def home(request):
    return render(request, 'home.html')

def summarization(request):
    if request.method == 'POST':
        form = SummyForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            try:
                summary = generate_summary(text)
                Summarization.objects.create(text=text, summary=summary)
                return redirect('/myapp/home')
            except (IndexError, ValueError) as e:
                return render(request, 'text_summarization.html', {'form': form, 'error': str(e)})
    else:
        form = SummyForm()
    return render(request, 'text_summarization.html', {'form': form})

def generate_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['text']
            summ = form.cleaned_data['isSummarized']
            try:
                if summ:
                    summary = generate_summary(text)
                else:
                    summary = text
                summarized_audio = audioFun(summary)
                audio_instance = Audio(text=text, summary=summary)
                audio_instance.audio.save('audio1.mp3', summarized_audio)
                return redirect('/myapp/home')
            except (IndexError, ValueError) as e:
                return render(request, 'audio.html', {'form': form, 'error': str(e)})
    else:
        form = AudioForm()
        return render(request, 'audio.html', {'form': form})

def generate_powerPoint(request):
    if request.method == 'POST':
        form = PowerPointForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            generatedPowerPoint = create_powerPoint(text)
            ppt_instance = PowerPoint.objects.create(text=text)
            ppt_instance.file.save('output.pptx', generatedPowerPoint)
            return redirect('/myapp/home')
    else:
        form = PowerPointForm()
    return render(request, 'powerpoint.html', {'form': form})

def powerpoint_success(request, id):
    ppt_instance = PowerPoint.objects.get(id=id)
    return render(request, 'powerpoint_success.html', {'ppt_instance': ppt_instance})


def generate_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['text']
            isSummarized = form.cleaned_data['need_summarize']
            image = form.cleaned_data['image']
            print(image)
            if isSummarized:
                summarized = generate_summary(text)
            else:
                summarized = text

            # try:
            generated_audio_file = audioFun(summarized)
            print(generated_audio_file)
            # generated_video = update_video(str(image), str(generated_audio_file))


            video_instance = Video.objects.create(
                text=text,
                summary=summarized,
                image=image,
                # video=generated_video
            )
            video_instance.audio.save('generated_audio.mp3', generated_audio_file)
            
            return redirect('/myapp/home')

        else:
            print(f"Form is invalid: {form.errors}")
    else:
        form = VideoForm()

    return render(request, 'video.html', {'form': form})




