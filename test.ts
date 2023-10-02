basic.showIcon(IconNames.No)
basic.pause(2000)
basic.forever(function () {
	
})

input.onButtonPressed(Button.B, function () {
    botMode_Int = 2
    basic.showIcon(IconNames.Happy)
    basic.showNumber(2)
})

input.onButtonPressed(Button.AB, function () {
    botMode_Int = 3
    basic.showIcon(IconNames.Happy)
    basic.showNumber(3)
})


basic.forever(function () {
    if (botMode_Int == 1) {
        if (true) {
            quest_Note_3.quest_Show_String_For_Note_Small_Fn(
                "Servo_Motors: Right Only"
            )
            quest_Note_2.quest_Show_String_For_Note_Small_Fn(
                "50% Power for Medium Speed"
            )
            quest_Note_2.quest_Show_String_For_Note_Small_Fn(
                "0% Power for Stop"
            )
            quest_Motors.quest_Set_PowerMotorsViaBlueRedBlackPins_Fn(
                quest_PortGroup_BlueRedBlack_PortIds_Enum.S1_MotorLeft__S0_MotorRight,
                0,
                50
            )
            quest_Note_1.quest_Show_String_For_Note_Small_Fn(
                "'micro:bit' Viewed Upside-Down, Same for LEDs Below"
            )
            basic.showLeds(`
                . # . # .
                . . . # .
                . . . # .
                . . # # #
                . . . # .
                `)
        }
    }
})

basic.forever(function () {
    if (botMode_Int == 3) {
        if (true) {
            quest_Note_3.quest_Show_String_For_Note_Small_Fn(
                "Servo_Motors: All Stop"
            )
            quest_Motors.quest_Set_PowerMotorsViaBlueRedBlackPins_Fn(
                quest_PortGroup_BlueRedBlack_PortIds_Enum.S1_MotorLeft__S0_MotorRight,
                0,
                0
            )
            quest_Note_1.quest_Show_String_For_Note_Small_Fn(
                "'micro:bit' Viewed Upside-Down, Same for LEDs Below"
            )
            basic.showLeds(`
                . # . # .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
        }
    }
})
