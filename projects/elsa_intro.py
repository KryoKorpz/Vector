""" 
Make Vector play fanfare and introduce Queen Anna
"""

import time
import anki_vector

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.audio.stream_wav_file("../sounds/intro_fanfare.wav", 50)
        time.sleep(1)
        print("Say 'Introducing, Queen Elsa of Arendelle'")
        robot.behavior.say_text("Introducing, Queen Elsa of erendel")

if __name__ == "__main__":
    main()