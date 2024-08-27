class Helper():
    @staticmethod
    def convert_keys_to_strings(move_dict):
        # Convert the dictionary keys from tuples to strings
        converted_dict = {
            team: {str(key): value for key, value in moves.items()}
            for team, moves in move_dict.items()
        }
        
        return converted_dict
    @staticmethod
    def convert_keys_to_tuples(retrieved_move_dict):
        def string_to_tuple(key_str):
            # Converts a string like "(1, 2)" to a tuple (1, 2)
            return tuple(map(int, key_str.strip('()').split(',')))

        # Convert the dictionary keys from strings back to tuples
        moveDict = {
            team: {string_to_tuple(key): value for key, value in moves.items()}
            for team, moves in retrieved_move_dict.items()
        }
        
        return moveDict