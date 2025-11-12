def get_book_text(path_to_file):
       with open(path_to_file) as f:
              file_contents = f.read()
       
       return file_contents

def get_num_words(file_contents):
       words = file_contents.split()
       return len(words)

def get_character_counts(file_contents):
       words = file_contents.split()
       character_count = {a:0, b:0}
       for w in words:
              word = words[w]
