#!/usr/bin/env python
# coding: utf-8
#
import ffmpeg
import os
import subprocess


if __name__ == '__main__':
    TEST_DIR = os.path.dirname(__file__)


    INPUT_FILE = os.path.join(TEST_DIR, 'temp/voice_5.mp3')

    print INPUT_FILE
    #
    #
    # subprocess.check_call(['ffmpeg', '-version'])
    #
    # stream = ffmpeg.input(INPUT_FILE)
    # stream = ffmpeg.hflip(stream)
    # # stream = ffmpeg.filter_(stream,'acodec',"pcm_s16le")
    # # stream = ffmpeg.filter_(stream,'f',"s16le")
    # # stream = ffmpeg.filter_(stream,'ac',1)
    # # stream = ffmpeg.filter_(stream,'ar',16000)
    # stream = ffmpeg.output(stream,"1223.pcm")
    # ffmpeg.run(stream)

    # subprocess.call(["./ffmpeg", "-y", "-i" , INPUT_FILE, "-acodec", "pcm_s16le", "-f" , "s16le", "-ac", "1" , "-ar" , "16000" , 'voice_1140481740763571900_track01.pcm'])


#"-f" , "s16le",

    subprocess.call(["./ffmpeg", "-y", "-i" , INPUT_FILE, "-acodec", "pcm_s16le", "-ac", "1" , "-ar" , "16000" , 'voice_1140481740763571900_track01.wav'])

    OUT_FILE = os.path