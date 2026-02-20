import whisper

def syncAudio(audio):
    print("Starting alignment...")
    
    print("Loading Whisper model...")
    model = whisper.load_model("base")  # Options: tiny, base, small, medium, large

    # Transcribe audio with word timestamps
    print("Transcribing and aligning audio...")
    result = model.transcribe(audio, word_timestamps=True)
    # print("result- ",result)
    # Debug: Print the result structure
    print("Type of result:", type(result))
    print("\nKeys in result:", result.keys() if isinstance(result, dict) else "Not a dict")
    # print("\nFull result:")
    # print(result)

    # Get segments with timing
    segments_with_timing = []
    for segment in result['segments']:
        segments_with_timing.append({
            'text': segment['text'].strip(),
            'start': segment['start'],
            'end': segment['end']
        })
        # print(f"[{segment['start']:.2f}s - {segment['end']:.2f}s]: {segment['text']}")
        # print("Type of segments_with_timing:", type(segments_with_timing))
        # for i, seg in enumerate(segments_with_timing, 1):
            # print(f"Segment {i}:")
            # print(f"  Text:     '{seg['text']}'")
            # print(f"  Start:    {seg['start']:.2f}s")
            # print(f"  End:      {seg['end']:.2f}s")
            # print(f"  Duration: {seg['end'] - seg['start']:.2f}s")
            # print()
            
    return segments_with_timing    
    # Create task configuration
    # config_string = "task_language=eng|is_text_type=plain|os_task_file_format=json"
    # Step 1: Save to temp file (Aeneas needs a file)
    # with open("temp_script.txt", "w", encoding="utf-8") as f:
        # f.write(script)
    # Create task
    # task = Task(config_string=config_string)
    # task.audio_file_path_absolute = audio
    # task.text_file_path_absolute = "temp_script.txt"  # Your script file
    # task.sync_map_file_path_absolute = "syncmap.json"

        # Execute alignment
    # ExecuteTask(task).execute()
    
    

    # Read the sync map
    # with open("syncmap.json") as f:
        # syncmap = json.load(f)
    
    # Use the timestamps
    # print("\nTimestamps generated:")
    # text_clips = []
    # for fragment in syncmap["fragments"]:
        # print(f"[{float(fragment['begin']):.2f}s - {float(fragment['end']):.2f}s]: {fragment['lines'][0]}")
        # txt = (TextClip(fragment["lines"][0], fontsize=55, color='white')
               # .with_position(('center', 1400))
               # .with_start(float(fragment["begin"]))
               # .with_duration(float(fragment["end"]) - float(fragment["begin"])))
        # text_clips.append(txt)
