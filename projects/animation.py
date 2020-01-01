import anki_vector

def main():

    with anki_vector.Robot() as robot:
        print("List all animation trigger names:")
        anim_trigger_names = robot.anim.anim_trigger_list
        for anim_trigger_name in anim_trigger_names:
            print(anim_trigger_name)

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.anim.play_animation_trigger('PRDemoGreeting')


if __name__ == "__main__":
    main()