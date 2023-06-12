import morse_converter
import morse_dictionary
import program_handler

morse_convert =\
    morse_converter.MorseConverter(morse_dictionary.char_to_morse_dictionary)

program_manager = program_handler.ProgramHandler(morse_convert)
program_manager.execute_request()

