from groq import Groq
import os


class ScriptGenerator:
    """Generates TikTok-style commentary scripts using Claude."""

    SYSTEM_PROMPT = """You are a viral TikTok/YouTube Shorts scriptwriter.
                        Your scripts follow this STRICT structure:

                        1. HOOK (1-2 sentences): Grab attention immediately. Use curiosity, shock, or a bold claim.
                        2. BODY (3-5 sentences): Explain the video briefly. Keep it fast-paced, punchy, no fluff.
                        3. OUTRO (1 sentence): End with a call to action or a punchline.

                        STRICT RULES:
                        - No timestamps
                        - No labels like "Hook:", "Body:", "Outro:" in the output
                        - No emojis
                        - No hashtags
                        - Speak directly to the viewer (use "you")
                        - Short sentences only. Max 15 words per sentence.
                        - Output ONLY the script. Nothing else."""
    

    def __init__(self, api_key: str, model: str = 'llama-3.3-70b-versatile'):

        self.client = Groq(api_key=api_key)
        self.model = model

    def generate(self, topic: str, style: str = "energetic and engaging") -> str:
        print(f"Generating script for: {topic}")

        response = self.client.chat.completions.create(
            model=self.model,
            max_tokens=512,
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": (
                        f"Write a {style} TikTok voiceover script about:\n\n"
                        f"{topic}\n\n"
                        f"Remember: Hook → Body → Outro. No labels. Just the script."
                    )
                }
            ]
        )

        script = response.choices[0].message.content.strip()
        return script


    def preview(self, topic: str, style: str = "energetic and engaging"):
        script = self.generate(topic, style)
        print("\n" + "="*50)
        print("GENERATED SCRIPT")
        print("="*50)
        print(script)
        print("="*50)
        print(f"Word count    : {len(script.split())}")
        print(f"Est. duration : ~{len(script.split()) // 3} seconds")
        print("="*50 + "\n")

        return script
    
def get_script(topic: str, style: str = "energetic and engaging", api_key: str = None) -> str:
    """Simple function to call from other scripts."""
    generator = ScriptGenerator(api_key=api_key)
    return generator.generate(topic, style)



if __name__ == '__main__':
    main()
