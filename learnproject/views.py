# I created this file -- mayaank
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")
    # return HttpResponse("Home")


def analyze(request):
    text = request.POST.get("text", "default")
    remove_punc = request.POST.get("removepunc", "off")
    caps = request.POST.get("fullcapital", "off")
    lineremove = request.POST.get("newlinerm", "off")
    extraspace = request.POST.get("extraspace", "off")
    charcounter = request.POST.get("charcount", "off")

    analyzed_text = ""
    action = ""

    if remove_punc == "on":
        punctuations = """!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
        for char in text:
            if char not in punctuations:
                analyzed_text = analyzed_text + char
            elif char == " ":
                analyzed_text += " "
        action += "Remove Punctuations "
        text = analyzed_text

    analyzed_text = ""

    if caps == "on":
        for char in text:
            if char == " ":
                analyzed_text += " "
            else:
                analyzed_text = analyzed_text + char.upper()
        action += "Capitalize the Text "
        text = analyzed_text

    analyzed_text = ""

    if lineremove == "on":
        for char in text:
            if char != "\n" and char != "\r":
                analyzed_text += char
        action += "Next line remove "
        text = analyzed_text

    analyzed_text = ""

    if extraspace == "on":
        for index, char in enumerate(text):
            if not (text[index] == " " and text[index + 1] == " "):
                analyzed_text += char
        action += "Extra Space Remove "
        text = analyzed_text

    analyzed_text = ""

    if charcounter == "on":
        count = 0
        for char in text:
            if char != " ":
                count += 1
        analyzed_text = (
            "No of charechters in the following text : \n "
            + text
            + "\n is equal to "
            + str(count)
        )
        action += "Charechter Count "
        text = analyzed_text

    analyzed_text = ""
    
    if (
        remove_punc != "on"
        and caps != "on"
        and lineremove != "on"
        and extraspace != "on"
        and charcounter != "on"
    ):
        text = text
        action += "Nothing choosen"

    params = {"analysed": action, "analysed_text": text}
    return render(request, "analyzed.html", params)
