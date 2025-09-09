import sys
import re
import os
import argparse
from openai import OpenAI
import prompts
import utils

# Load environment variables from .env if available (non-fatal if missing)
try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass

## Personas: The Terminator, David Goggins --> Commenting these out for v0

wpm = 160  # words per minute





def take_arguments():
    parser = argparse.ArgumentParser(description='Run Pusher')
    parser.add_argument('--prompt', type=str, required=True, help='The prompt from the runner')
    parser.add_argument('--persona', type=str, required=False, choices=['Terminator', 'Goggins'], default='Goggins', help='The persona requested by the runner')
    parser.add_argument('--duration_mins', type=int, required=True, help='The duration of the run remaining in minutes')
    parser.add_argument('--technique_hint', type=str, required=False, help='The technique hint requested by the runner')
    return parser.parse_args()

def main():
    args = take_arguments()
    print("Prompt:", args.prompt)
    print("Persona:", args.persona)
    print("Duration (mins):", args.duration_mins)
    print("Technique Hint:", args.technique_hint)

    # try:
    #     # output_text = response(
    #     #     prompt=args.prompt,
    #     #     duration_mins=args.duration_mins,
    #     #     technique_hint=args.technique_hint,
    #     #     persona=args.persona,
    #     # )
    #     # print("\n--- Generated Script ---\n")
    #     # print(output_text)

    # except Exception as e:
    #     print("Error generating response:", str(e), file=sys.stderr)
    #     sys.exit(1)

def response(prompt: str, duration_mins: int, technique_hint: str | None = None, persona: str = 'Goggins') -> str:
    client = OpenAI()

    target_words = utils.estimate_target_words(duration_mins=duration_mins, wpm=wpm)
    formatted_system_prompt = prompts.SYSTEM_PROMPT.format(target_words=target_words)
    formatted_user_prompt = prompts.USER_PROMPT.format(
        prompt=prompt,
        persona=persona,
        duration_mins=duration_mins,
        technique_hint=technique_hint or "None",
        target_words=target_words,
        wpm=wpm,
    )

    resp = client.responses.create(
        model="gpt-4o-mini",
        instructions=formatted_system_prompt,
        input=formatted_user_prompt,
    )
    text = resp.output_text
    text_for_speech = utils.clamp_words(text, target_words)
    return text_for_speech




if __name__ == "__main__":
    main()
    sys.exit(0)
