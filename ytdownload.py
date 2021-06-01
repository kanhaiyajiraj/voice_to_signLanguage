import fetchLink
from pytube import YouTube
from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
import os
import re,wget


os.chdir(SAMPLE_INPUTS)
def downloader(word):
    word = list(word.split(" "))
    for w in word:
        link=fetchLink.getLink(w)
        if re.match('^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$',link):
            clip = YouTube(link)
            clip.streams.first().download()
        else:
            wget.download(link,out=SAMPLE_INPUTS)
