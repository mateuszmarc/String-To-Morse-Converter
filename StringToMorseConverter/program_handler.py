import morse_converter


class ProgramHandler:
    """
    Class responsible for handling users requests and delegate them
    to other objects.
    """

    def __init__(self, morse_translator: morse_converter.MorseConverter) -> None:
        """
        Initialize data attributes for ProgramHandler class.
        :param morse_translator: Instance of the MorseConverter class
            from morse_converter module.
        """

        self.morse_translator = morse_translator

    def execute_request(self) -> None:
        """
        Perform type of request the user wants to be performed.
        It might be to convert Morse code message to ASCII characters.
        It might be also to convert ASCII characters to Morse code
        and play it.
        """
        print("Welcome to Mateusz's Morse Converter! ")
        while True:
            print("What do you want me to do?:\n"
                  "1 - Convert ASCII message to Morse code and play it?\n"
                  "2 - Convert Morse Code message to ASCII characters?\n")
            request = input()
            if request == '1':
                ascii_message_list =\
                    self.morse_translator.validate_message(request)
                converted_message =\
                    self.morse_translator.string_to_morse(ascii_message_list)
                # self.morse_translator.display_morse(converted_message)
                self.morse_translator.play_morse(converted_message)

            elif request == '2':
                morse_message_list =\
                    self.morse_translator.validate_message(request)
                converted_message =\
                    self.morse_translator.morse_to_string(morse_message_list)
                self.morse_translator.display_ascii(converted_message)
            else:
                print("Invalid request.")
                continue

            more = input("Do you want to decode more messages?\n"
                         "Type 'y' if yes and 'n' if no:\n")
            if more == 'n':
                print("Thank you for using my Morse Converter!")
                break