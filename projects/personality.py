
import threading

import anki_vector
from anki_vector.events import Events
from anki_vector.user_intent import UserIntent, UserIntentEvent

def main():
    def on_user_intent(robot, event_type, event, done):
        user_intent = UserIntent(event)
        print(f"Received {user_intent.intent_event}")
        print(user_intent.intent_data)

        if user_intent.intent_event is UserIntentEvent.greeting_hello:
            robot.behavior.say_text("hello, jesse")

        done.set()

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        done = threading.Event()
        robot.events.subscribe(on_user_intent, Events.user_intent, done)

        print('------ Vector is waiting for a voice command like "Hey Vector!  What time is it?" Press ctrl+c to exit early ------')

        try:
            if not done.wait(timeout=10):
                print('------ Vector never heard a voice command ------')
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    while True:
        main()
