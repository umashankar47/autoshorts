import reddown
import edit
import syncAudio
import argparse


class App:
    def __init__(self, args):
        self.url    = args.url
        self.video  = args.video
        self.audio  = args.audio

        self.videoName = args.video
        self.subtitle  = []


    def run(self):
        print("Enterd def Run")
        if self.url:
            self.process_url()
        elif not self.video:
            print("Error : provide --url or -video link")
            return

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
            self.videoName = title + "" + ".mp4"
            print("videoName:",self.videoName)




    def process_v(self):
        print("Processing Video")
        kwargs = {

        "videoName":self.videoName,
        "subtitle" : self.subtitle,

        }

        if self.audio:
            kwargs["audioSrc"] = self.audio

        edit.editVideo(**kwargs)

    def process_a(self):
        print("Processing audio")

        if self.audio:
            self.subtitle = syncAudio.syncAudio(self.audio)
        else:
            self.subtitle = syncAudio.syncAudio(self.videoName)


def parse_args():
    print("Parsing")
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--url")
    parser.add_argument("-a","--audio")
    parser.add_argument("-v","--video")
    return parser.parse_args()




if __name__ == '__main__':
    print("Enterd Main")
    args = parse_args()
    app = App(args)
    app.run()
