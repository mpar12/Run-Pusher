import sys
import re 
import os
import argparse

## Personas: The Terminator, David Goggins

wpm = 160 # words per minute

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


if __name__ == "__main__":
    main()
    sys.exit(0)

