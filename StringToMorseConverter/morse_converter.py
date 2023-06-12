import winsound


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
        self.morse_to_char_dict = self.get_morse_to_char_dict()
        self.morse_sound_dict = self.get_morse_sound_dict()

    def get_morse_sound_dict(self) -> dict:
        """
        Create dictionary from `morse_dict` data attribute where keys
        are values on index position 0 of value from `morse_dict` and the
        values are the values on index position 1 from `morse_dict`.
        """
        return {value[0]: value[1] for value in self.morse_dict.values()}

    def get_morse_to_char_dict(self) -> dict:
        """
        Convert morse_dict that represents ASCII characters as the keys
        and corresponding tuples as values.

        Convert the `morse_dict` so the keys become values and values
        become keys. Then return new dictionary.

        :return: New dictionary made of `morse_dict` where values become
            keys and keys become values. So keys will are tuples where
            first item is the Morse code representing the ASCII
            character and second item is the file path to wav file of
            the Morse code sound.
        """

        new_keys = [value[0] for value in self.morse_dict.values()]
        new_values = [key for key in self.morse_dict.keys()]
        return dict(zip(new_keys, new_values))

    def validate_message(self, message_type: str) -> list:
        """
        Get the message from the user as an input.
        Depending on `message_type` validate message if all characters
        from the input message are in `morse_dict` or `morse_to_char_dict
        keys. If not then display character or Morse code signs that are
        invalid and prompt the user to type again.

        :return: List of characters from the message input.
        """
        if message_type == '1':
            prompt = "Please enter the message to be converted to the " \
                     "Morse Code. You can use only these characters:"
            dictionary_to_check = self.morse_dict
        else:
            prompt = "Please enter the Morse message to be converted to the " \
                     "ASCII letters. Use '*' for the space between symbols." \
                     "You can use only following codes:"
            dictionary_to_check = self.morse_to_char_dict
        while True:
            print(prompt)
            for character in dictionary_to_check.keys():
                print(character, end=', ')
            print()
            message = input()
            if message_type == '2' and '*' in message:
                message_chars = message.split('*')
            else:
                message_chars = [char for char in message.upper()]
            # validate the message
            not_allowed = []
            for character in message_chars:
                if character not in [key for key in dictionary_to_check.keys()]:
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
        to the Morse code list of message characters.

        :param message: Message returned by validate_message class method.
        :return: Morse code representation of the message got from the
            user.
        """
        converted_message = \
            [self.morse_dict[character] for character in message]
        return converted_message

    def play_morse(self, converted_message: list) -> None:
        """
        Use `winsound` module to play morse wav sounds from file_paths
        from `converted_message` list of tuples.

        :param converted_message: List of the tuples containing
            Morse characters and Morse code sound file paths got
            from the conversion of the  user's message.
        """

        for morse_char in converted_message:
            print(morse_char[0], end=' ')
        print()

        for morse_char in converted_message:
            print(morse_char[0], end=' ')
            winsound.PlaySound(morse_char[1], winsound.SND_FILENAME)
        print()

    def morse_to_string(self, message: list) -> list:
        """
        Get the Morse message from the user as a string and return
        converted to the ASCII list of message characters.

        :param message: Message returned by validate_message class method.
        """
        converted_message = \
            [self.morse_to_char_dict[character] for character in message]
        print(converted_message)
        return converted_message

    def display_ascii(self, converted_message: list) -> None:
        """
        Display ascii characters from the `converted_message`.

        :param converted_message: List of the tuples containing
            Morse characters and Morse code sound file paths got
            from the conversion of the  user's message.
        """
        print(''.join(converted_message))
