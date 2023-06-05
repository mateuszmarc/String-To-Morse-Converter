import pygame

class MorseConverter:
    """
    Representation of the Class responsible for translation ASCII
    characters into the morse code and morse code to ASCII characters.
    """

    def __init__(self, morse_dict: dict) -> None:
        """
        Initialize data attributes of the MorseConverter class.
        :param morse_dict: Dictionary containing ASCII letters as
            the keys and tuple containing morse representation of the
            ASCII letter and file path to corresponding Morse code sound.
        """
        self.morse_dict = morse_dict

    def validate_message(self) -> list:
        """
        Get the message input from the user and check if characters used
        in the message are in our `morse_dict` keys. Return list of the
        characters from the message if all characters used are in
        `morse_dict` keys. If otherwise, inform user about the not
         allowed characters used and ask to retype message again.
        :return: List of characters from the message input.
        """
        while True:
            message = input("Please enter the message to be converted to the "
                            "Morse Code( you can use only these characters:\n")
            for character in self.morse_dict.keys():
                print(character, sep=', ')

            message_chars = message.split()
            # validate the message
            not_allowed = []
            for character in message_chars:
                if character not in self.morse_dict.keys():
                    not_allowed.append(character)

            if not_allowed:
                print("You used following characters outside from the "
                      "list:")
                for char in not_allowed:
                    print(char)
                continue
            else:
                return message_chars

    def string_to_morse(self, message: list) -> list:
        """
        Get the message from the user as a string and return converted
        to the Morse code message.
        :return: Morse code representation of the message got from the
            user.
        """
        converted_message = \
            [self.morse_dict[character] for character in message]
        return converted_message

    def display_morse(self, converted_message: list) -> None:
        """
        Display morse characters from the `converted_message`.
        :param converted_message: List of the tuples containing
            Morse characters and Morse code sound file paths got
            from the conversion of the  user's message.
        """
        for morse_char in converted_message:
            print(morse_char[0], sep=' ')


    def play_morse(self, converted_message: list) -> None:
        """

        :param converted_message:
        :return:
        """





























