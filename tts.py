import asyncio
import edge_tts


class TTSEngine:
    """Converts script to speech using Edge TTS (Microsoft - Free, Neural Voices)."""

    # Popular voices — run list_voices() to see all 400+
    VOICES = {
        'us_male'      : 'en-US-GuyNeural',
        'us_female'    : 'en-US-JennyNeural',
        'uk_male'      : 'en-GB-RyanNeural',
        'uk_female'    : 'en-GB-SoniaNeural',
        'au_male'      : 'en-AU-WilliamNeural',
        'india_male'   : 'en-IN-PrabhatNeural',
    }


    def __init__(self, voice: str = 'us_male', rate: str = '+0%', pitch: str = '+0Hz'):
        """
        Args:
            voice   : Key from VOICES dict or a raw Edge TTS voice string
            rate    : Speed e.g. '+20%' faster, '-20%' slower
            pitch   : Pitch e.g. '+10Hz' higher, '-10Hz' lower
        """
        self.voice = self.VOICES.get(voice, voice)  # accepts both key and raw voice string
        self.rate  = rate
        self.pitch = pitch
        
    def synthesize(self, script: str, output_path: str = 'commentary.mp3') -> str:
        """Convert script to audio file. Returns path to saved file."""
        asyncio.run(self._synthesize(script, output_path))
        print(f"Audio saved to: {output_path}")
        return output_path

    async def _synthesize(self, script: str, output_path: str):
        """Internal async method for edge-tts."""
        communicate = edge_tts.Communicate(script, self.voice, rate=self.rate, pitch=self.pitch)
        await communicate.save(output_path)

    @staticmethod
    def list_voices():
        """Print all available voices."""
        async def _list():
            voices = await edge_tts.list_voices()
            for v in voices:
                print(f"{v['ShortName']:<40} | {v['Gender']:<10} | {v['Locale']}")
        asyncio.run(_list())




if __name__ == "__main__":
    main()

