def on_button_pressed_a():
    global botMode_Int
    botMode_Int = 1
    basic.show_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

botMode_Int = 0
if True:
    quest_Note_3.quest_Show_String_For_Note_Small_Fn("Download/Flash Confirmation Icon")
    basic.show_icon(IconNames.HAPPY)
    quest_Note_3.quest_Show_String_For_Note_Small_Fn("Continue Current State for Time Below")
    quest_Timer.quest_Set_ContinueCurrentState_CountdownTimer_Fn(2, quest_Time_Units_Enum.SECONDS)
if True:
    quest_Note_3.quest_Show_String_For_Note_Small_Fn("Servo_Motors: All Stop")
    quest_Note_2.quest_Show_String_For_Note_Small_Fn("0% Power for Stop")
    quest_Motors.quest_Set_PowerMotorsViaBlueRedBlackPins_Fn(quest_PortGroup_BlueRedBlack_PortIds_Enum.S1_MOTORLEFT__S0_MOTORRIGHT,
        0,
        0)
    quest_Note_1.quest_Show_String_For_Note_Small_Fn("'micro:bit' Viewed Upside-Down, Same for LEDs Below")
    basic.show_leds("""
        . # . # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
if True:
    botMode_Int = 0

def on_forever():
    if botMode_Int == 2:
        if True:
            quest_Note_3.quest_Show_String_For_Note_Small_Fn("Servo_Motors: Left Only")
            quest_Note_2.quest_Show_String_For_Note_Small_Fn("50% Power for Medium Speed")
            quest_Note_2.quest_Show_String_For_Note_Small_Fn("0% Power for Stop")
            quest_Motors.quest_Set_PowerMotorsViaBlueRedBlackPins_Fn(quest_PortGroup_BlueRedBlack_PortIds_Enum.S1_MOTORLEFT__S0_MOTORRIGHT,
                50,
                0)
            quest_Note_1.quest_Show_String_For_Note_Small_Fn("'micro:bit' Viewed Upside-Down, Same for LEDs Below")
            basic.show_leds("""
                . # . # .
                . . . # .
                . . . # .
                . . # # #
                . . . # .
                """)
basic.forever(on_forever)
