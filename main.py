import json
import subprocess

import reddown
from edit import VideoEditor
import syncAudio
import argparse
from  llm_chat import get_script
import os
from dotenv import load_dotenv, find_dotenv
from tts import TTSEngine



class App:
    def __init__(self, args):
        self.url    = args.url
        self.video  = args.video
        self.audio  = args.audio
        self.script = args.script
        self.style  = args.style
        self.api_key =  None
    

        self.videoName = args.title if args.title else None
        self.subtitle  = []


    def run(self):
        print("Starting....")
        print("URL",self.url)
        print("Script",self.script)
        print("audio.",self.audio)
        print("self.video",self.video)
    

        load_dotenv("prop.env")
    
        self.api_key = os.getenv("API_KEY")

        if self.api_key:
            print(f"API Key successfully loaded and begins with: {self.api_key[:4]}****")
        else:
            print("API Key not found.")

        if self.url:
            self.process_url()
        elif not self.video:
            print("Error : provide --url or -video link")
            return

        
        
        self.process_script()
        self.process_a()
        self.process_v()

    def process_url(self):
        print(f"Processing URL: {self.url}")
        title = ""
        try:
            title = reddown.download(self.url)
        except:
            print("Video Download Error")

        if title:
            print("Title :", title )
            self.videoName = title
            self.video = title + "" + ".mp4"
            print("videoName:",self.videoName)


    def process_script(self):
        
        if self.script is True:
            self.script = get_script(self.videoName, self.style, self.api_key )
        elif self.script is False:
            return
        print("SCRIPT - ",self.script)
        ttsAud =  TTSEngine(voice='uk_male', rate='+10%')
        self.audio = ttsAud.synthesize(self.script)


    def process_v(self):
        print("Processing Video")
        
        print("self.videoName",self.videoName)
        print("audio.",self.audio)
        print("self.video",self.video)
        print("self.subtitle",self.subtitle)

        if not self.videoName:
            self.videoName = self.video[:-4]
        kwargs = {

        "videoName":self.video,
        "subtitle" :self.subtitle,
        "title"    :self.videoName

        }

        if self.audio:
            kwargs["audioSrc"] = self.audio

        # edit.editVideo(**kwargs)
        editor = VideoEditor(**kwargs)
        editor.renderVideo()
        
    def has_audio(self):
        result = subprocess.run(
            [
            "ffprobe", "-v", "error",
            "-select_streams", "a:0",
            "-show_entries", "stream=codec_type",
            "-of", "json",
            self.video
            ],
        capture_output=True, text=True
        )
        data = json.loads(result.stdout)
        return len(data.get("streams", [])) > 0


    def process_a(self):
        print("Processing audio")

        if self.audio:
            self.subtitle = syncAudio.syncAudio(self.audio)
        else:
            if self.has_audio():
                self.subtitle = syncAudio.syncAudio(self.video)
            else:
                print("No audio stream found, skipping.")
                return


def parse_args():
    print("Parsing")
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--url")
    parser.add_argument("-a","--audio")
    parser.add_argument("-v","--video")
    parser.add_argument("-t","--title")
    parser.add_argument("-s","--script", nargs='?', const=True, default=False)
    parser.add_argument("--style")

    return parser.parse_args()




if __name__ == '__main__':
    print("Enterd Main")
    args = parse_args()
    app = App(args)
    app.run()
