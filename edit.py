from moviepy import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip, CompositeAudioClip
import re




class VideoEditor:
    DEFAULT_FONT = 'D:/DP/pyTon Env Testing/Chunk Five Print.otf'
    OUTPUT_SIZE = (1080, 1920)

    def __init__(self,**kwargs):
        self.videoPath = kwargs.get('videoName')
        self.font = kwargs.get('font_path', self.DEFAULT_FONT)
        self.vidName  = kwargs.get('title')
        self.subtitles = kwargs.get('subtitles', [])
        self.titleClip = []
        self.audio_src = kwargs.get('audio_src', None)
        self.video = VideoFileClip(self.videoPath)

    def load_subtitles(self, subtitle: list[dict]):
        """load Segments"""
        self.subtitles = subtitle
        return self
    
    def load_commentary(self, audio_src: str):
        """Load optional commentary audio."""
        self.audio_src = audio_src
        return self
    
    def _crop_video(self):
        """Crop video to vertical (1080x1920) format."""
        resized = self.video.resized(height=self.OUTPUT_SIZE[1])
        return resized.cropped(
            x_center=resized.w / 2,
            y_center=resized.h / 2,
            width=self.OUTPUT_SIZE[0],
            height=self.OUTPUT_SIZE[1]
        )
    
    def _build_title(self):
        """add title"""
        title_clip = (TextClip(text=self.vidName, font_size=80, color='white',
                       stroke_color='black', stroke_width=3,
                       font= self.font,
                       method='caption', size=(1000, None))
              .with_position('center')  # Center of screen
              .with_start(0)  # Start at beginning
              .with_duration(4))  # Show for 4 seconds
        return title_clip
    
    def _build_subtitle(self):
        """Build subtitle TextClips from loaded subtitle segments."""
        text_clips = []
        for seg in self.subtitles:
            txt = (TextClip(text=seg['text'],font=self.font, font_size=70, color='white',stroke_color='black', stroke_width=2,method='caption', size=(1000, None))
            .with_position(('center', 1400))
            .with_start(seg['start'])
            .with_duration(seg['end'] - seg['start']))
            text_clips.append(txt)

        return text_clips

    def _build_audio(self):
        """Composite original + commentary audio."""
        print("Audio source:", self.audio_src)
        commentary = AudioFileClip(self.audio_src)
        return CompositeAudioClip([self.video.audio, commentary])
        
    

    def renderVideo(self, subtitles: list = None, audio_src: str =None):
        """Compose and export the final video."""
        print("Video : ",self.vidName)

        if self.video:
            print("Video Available")

        cropped = self._crop_video()
        title_clip = self._build_title()
        subtitle_clips = self._build_subtitle()
        final_video = CompositeVideoClip([cropped, title_clip] + subtitle_clips)

        if self.audio_src:
            print("Adding Audio : {audio_src}")
            final_audio = self._build_audio()
            final_video = final_video.with_audio(final_audio)
    

        # Export
        safe_filename = re.sub(r'[<>:"/\\|?*]', '', self.vidName)  # Remove invalid characters
        filename = f"{safe_filename}_1.mp4"
        final_video.write_videofile(filename, codec='libx264', audio_codec='aac', bitrate='550k')
        print(f"Exported: {filename}")
        return filename





if __name__ == '__main__':
    main()
