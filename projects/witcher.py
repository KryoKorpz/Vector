""" 
Have Vector change face to witcher coin and play Valley of plenty
"""

import os
import sys
import time

try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import anki_vector
from anki_vector.util import degrees


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.set_head_angle(degrees(45))
        robot.behavior.set_lift_height(0.0)

        current_directory = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(current_directory, "..", "face_images", "witcher_coin.jpg")

        # Load an image
        image_file = Image.open(image_path)

        # Convert the image to the format used by the Screen
        print("Display image on Vector's face...")
        screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)

        duration_s = 15
        robot.screen.set_screen_with_image_data(screen_data, duration_s)
        robot.audio.stream_wav_file("../sounds/coin.wav", 10)
        robot.anim.play_animation_trigger('PRDemoGreeting')


if __name__ == "__main__":
    main()