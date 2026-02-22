import whisper

def syncAudio(audio):
    print("Starting alignment...")
    
    print("Loading Whisper model...")
    model = whisper.load_model("base")  #  tiny, base, small, medium, large

    # Transcribe audio with word timestamps
    print("Transcribing and aligning audio...")
    result = model.transcribe(audio, word_timestamps=True)
   
    print("Type of result:", type(result))
    print("\nKeys in result:", result.keys() if isinstance(result, dict) else "Not a dict")
    

    # Get segments with timing
    segments_with_timing = []
    for segment in result['segments']:
        segments_with_timing.append({
            'text': segment['text'].strip(),
            'start': segment['start'],
            'end': segment['end']
        })
   
            
    return segments_with_timing    
   

if __name__ == '__main__':
    main()
    
  