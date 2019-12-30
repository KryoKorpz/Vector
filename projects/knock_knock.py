"""
interact with vector to play complete a knock knock joke
"""

import threading

import anki_vector
from anki_vector.events import Events
from anki_vector.user_intent import UserIntent, UserIntentEvent

def main():

    def on_user_intent(robot, event_type, event, done):
        user_intent = UserIntent(event)
        if user_intent.intent_event is UserIntentEvent.knowledge_question:
            print(f"Received {user_intent.intent_event}")
            print(user_intent.intent_data)
            done.set()

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print("knock, knock")
        robot.behavior.say_text("Knock, Knock")
        done = threading.Event()
        robot.events.subscribe(on_user_intent, Events.user_intent, done)
        try:
            if not done.wait(timeout=3):
                robot.behavior.say_text("Vector")
        except KeyboardInterrupt:
            exit()
        try: 
            done = threading.Event()
            robot.events.subscribe(on_user_intent, Events.user_intent, done)
            if not done.wait(timeout=3):      
                robot.behavior.say_text("Vector is here")
        except KeyboardInterrupt:
            exit()

if __name__ == '__main__':
    main()

