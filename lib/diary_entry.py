class DiaryEntry:
    def __init__(self, title, contents):
        if type(title) != str or type(contents) != str:
            raise Exception("Diary arg should not be int.")
        self.title = title
        self.contents = contents
        self.content_list = self.contents.split()

    def format(self):
        return f"{self.title}: {self.contents}"
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"

    def count_words(self):
        return len(self.content_list)

    def reading_time(self, wpm):
        if type(wpm) != int:
            raise Exception("wpm needs to be an int")
        return self.count_words() / wpm 

        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.

    def reading_chunk(self, wpm, minutes):
        #returns contents as a list

        #calculate number of words that can be read = x
        total_words_read = wpm * minutes

        #return list contents[:x + 1] 
        list_contents_to_read = self.content_list[:total_words_read]
        print(f'{len(list_contents_to_read)} should equal {len(["i", "am", "the", "contents"]*60)}')


        #join list back to string
        joint_list = " ".join(list_contents_to_read)
        print(f'{joint_list} should equal {"i am the contents "*60}')
        return joint_list



        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass