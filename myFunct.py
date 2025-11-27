import re
from fuzzywuzzy import fuzz


def clean(text, special_characters):
    # Function to clean text by removing punctuation marks , numbers and special symbols
    # Input: text (str) - The input text to be cleaned
    #        special_characters (list[str]) - List of characters to be removed
    # Output: str - The cleaned text
    cleaned_text = ''
    for chars in text:
        if chars not in special_characters:
            cleaned_text += chars
    return cleaned_text


def clear_space(text):
    # Function to clear extra spaces in the text
    # Input: text (str) - The input text with possible extra spaces
    # Output: str - The text with extra spaces replaced by a single space
    text = re.sub(r'\s+', ' ', text)
    return text


def tokenize(text):
    # Function to tokenize text into individual words
    # Input: text (str) - The input text to be tokenized
    # Output: list[str] - List of tokenized words
    tokenized_text = text.split(' ')
    return tokenized_text


def remove_sw_amharic(tokenized_text, amharic_sw):
    # Function to remove stop words from Amharic text
    # Input: tokenized_text (list[str]) - List of words to be processed
    #        amharic_sw (list[str]) - List of stop words to be removed
    # Output: list[str] - List of words with stop words removed
    removed_amharic_text = []
    for words in tokenized_text:
        if words not in amharic_sw:
            removed_amharic_text.append(words)
    return removed_amharic_text


def remove_sw_tigrigna(text, tigrigna_sw):
    # Function to remove stop words from Tigrigna text
    # Input: text (list[str]) - List of words to be processed
    #        tigrigna_sw (list[str]) - List of stop words to be removed
    # Output: list[str] - List of words with stop words removed
    removed_tigrigna_text = []
    for words in text:
        if words not in tigrigna_sw:
            removed_tigrigna_text.append(words)
    return removed_tigrigna_text

initials_amh = ['የ', 'ለ', 'በ', 'ከ']
lasts_amh = ['ህ', 'ም', 'ና', 'ን']


def lemmatize_amharic(text):
    # Function to lemmatize Amharic text by removing prefixes and suffixes
    # Input: text (list[str]) - List of words to be lemmatized
    # Output: list[str] - List of lemmatized words
    lemmatized_amharic_text = []
    for words in text:
        if words[0] in initials_amh and words[-1] in lasts_amh:
            lemmatized_amharic_text.append(words[1:-1])  # Remove both first and last characters
        elif words[0] in initials_amh:
            lemmatized_amharic_text.append(words[1:])     # Remove only the first character
        elif words[-1] in lasts_amh:
            lemmatized_amharic_text.append(words[:-1])    # Remove only the last character
        else:
            lemmatized_amharic_text.append(words)          # Leave unchanged if no condition is met
    return lemmatized_amharic_text

last2_amh = ['ውን', 'ዎች', 'ችን']


def lemmatize_amharic2(text):
    # Function to further lemmatize Amharic text by removing specific suffixes
    # Input: text (list[str]) - List of words to be further lemmatized
    # Output: list[str] - List of lemmatized words
    lemmatized_amharic_text = []
    for word in text:
        if word[-2:] in last2_amh:
            lemmatized_amharic_text.append(word[:-2])  # Remove the last two characters
        else:
            lemmatized_amharic_text.append(word)  # Leave unchanged if no condition is met
    return lemmatized_amharic_text

initials_tig = ['ብ', 'ዝ', 'የ']
lasts_tig = ['ና', 'ን']


def lemmatize_tigrigna(text):
    # Function to lemmatize Tigrigna text by removing prefixes and suffixes
    # Input: text (list[str]) - List of words to be lemmatized
    # Output: list[str] - List of lemmatized words
    lemmatized_tigrigna_text = []
    for words in text:
        if words[0] in initials_tig and words[-1] in lasts_tig:
            lemmatized_tigrigna_text.append(words[1:-1])  # Remove both first and last characters
        elif words[0] in initials_tig:
            lemmatized_tigrigna_text.append(words[1:])     # Remove only the first character
        elif words[-1] in lasts_tig:
            lemmatized_tigrigna_text.append(words[:-1])    # Remove only the last character
        else:
            lemmatized_tigrigna_text.append(words)          # Leave unchanged if no condition is met
    return lemmatized_tigrigna_text

last2_tig = ['ውን', 'ዎች']


def lemmatize_tigrigna2(text):
    # Function to further lemmatize Tigrigna text by removing specific suffixes
    # Input: text (list[str]) - List of words to be further lemmatized
    # Output: list[str] - List of lemmatized words
    lemmatized_tigrigna_text = []
    for word in text:
        if word[-2:] in last2_tig:
            lemmatized_tigrigna_text.append(word[:-2])  # Remove the last two characters
        else:
            lemmatized_tigrigna_text.append(word)  # Leave unchanged if no condition is met
    return lemmatized_tigrigna_text

def normalize(lemmatized_text):
# Function to normalize text by removing single-character words
# Input: lemmatized_text (list[str]) - List of lemmatized words
# Output: list[str] - List of normalized words with single-character words removed
    lemmatized_text = [word for word in lemmatized_text if len(word) > 1]
    return lemmatized_text

#### Further Partial Analysis of words by grouping in their similarity percentage ####

# Function to compare Amharic and Tigrigna words based on similarity percentage using fuzzywuzzy
# Input: amharic_words (list[str]) - List of Amharic words
#        tigrigna_words (list[str]) - List of Tigrigna words
# Output:  similarity results and total overlap percentage
def compare(amharic_words, tigrigna_words):
    similar_words = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': []}
    # Fuzzy matching and grouping by similarity percentage
    for amharic_word in amharic_words:
        best_match = None
        highest_similarity = 0
        for tigrigna_word in tigrigna_words:
            similarity = fuzz.ratio(amharic_word, tigrigna_word)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = tigrigna_word
        # Classifying based on the highest similarity percentage
        if highest_similarity > 90:
            similar_words['A'].append((amharic_word, best_match, highest_similarity))
        elif highest_similarity >= 80:
            similar_words['B'].append((amharic_word, best_match, highest_similarity))
        elif highest_similarity >= 70:
            similar_words['C'].append((amharic_word, best_match, highest_similarity))
        elif highest_similarity >= 60:
            similar_words['D'].append((amharic_word, best_match, highest_similarity))
        elif highest_similarity >= 50:
            similar_words['E'].append((amharic_word, best_match, highest_similarity))
        else:
            similar_words['F'].append((amharic_word, best_match, highest_similarity))

    
    for group, word_pairs in similar_words.items():
        # Output the number of elements in each group
        count = len(word_pairs)
        print(f"Group {group}: {count} elements")
    print()

   # the Output each amharic word and its best match from tigrigna in each group(A-F)
    #for group, word_pairs in similar_words.items():
        #print(f"Group {group}:")
        #for am_word, tg_word, score in word_pairs:
            #print(f"  Amharic: {am_word}, Best Tigrigna Match: {tg_word}, Similarity: {score}% ")
    
    # Calculate the total count of all groups
    count_A = len(similar_words['A'])
    count_B = len(similar_words['B'])
    count_C = len(similar_words['C'])
    count_D = len(similar_words['D'])
    count_E = len(similar_words['E'])
    count_F = len(similar_words['F'])
    total_word_count = count_A + count_B + count_C + count_D + count_E + count_F
    
    # Calculate the weighted sum using the average of each group's percentage range
    weighted_sum = (count_A * 100) + (count_B * 90) + (count_C * 80) + (count_D * 60) + (count_E * 30) + (count_F * 0)
    
    # Calculate the total overlap (average similarity percentage)
    try:
        total_overlap = weighted_sum / total_word_count
    except ZeroDivisionError:
        total_overlap = 0  # Handle the case where there are no matches
    
    # Output the total overlap percentage
    print(f"Word Level Overlap Percentage: {round(total_overlap, 2)}%")


def transcribe_words(word_list, transcription_dict):
    # Function to transcribe words using a transcription dictionary
    # Input: word_list (list[str]) - List of words to be transcribed
    # transcription_dict (dict[str, str]) - Dictionary for character to phoneme mapping
    # Output: list[str] - List of transcribed words
    transcribed_words = []
    for word in word_list:
        phonemes = []
        for char in word:
            # Look up each character in the transcription dictionary
            phoneme = transcription_dict.get(char, char)  # Use the character itself if not found
            phonemes.append(phoneme)
        
        # Join the list of phonemes into a single string
        transcribed_word = ''.join(phonemes)
        transcribed_words.append(transcribed_word)
    return transcribed_words


def count_character_frequency(words):
    # Function to count the frequency of each character in a list of words
    # Input: words (list[str]) - List of words to count character frequencies
    # Output: dict[str, int] - Dictionary with characters as keys and their frequencies as values
    frequency_dict = {}
    for word in words:
        for char in word:
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
    return frequency_dict


def compute_overlap(dict1, dict2):
    #Function to compute the overlap between two dictionaries of character frequencies
    # Input: dict1 (dict[str, int]) - Frequency dictionary of Amharic characters
    # dict2 (dict[str, int]) - Frequency dictionary of Tigrigna characters
    # Output: dict[str, dict[str, int]] - Dictionary of overlapping characters with their frequencies in both languages
    overlap = {}
    for char in dict1:
        if char in dict2:
            overlap[char] = {
                'frequency_in_am': dict1[char],
                'frequency_in_tig': dict2[char]
            }
    return overlap

def phoneme_overlap_percentage(dict1, dict2):
    #Function to calculate the percentage of overlapping phonemes between two dictionaries of character frequencies.
    #Input: dict1 (dict[str, int]): Frequency dictionary of Amharic characters.
    #       dict2 (dict[str, int]): Frequency dictionary of Tigrigna characters.
    # Output: float: Percentage of overlapping phonemes between the two input dictionaries, rounded to two decimal places.
    overlap = compute_overlap(dict1, dict2)
    total_unique_chars = len(set(dict1.keys()).union(set(dict2.keys())))
    total_overlap_chars = len(overlap)
    print(f"Total unique characters: { total_unique_chars}")
    print(f"Total overlapping characters: {total_overlap_chars}")
    if total_unique_chars == 0:
        return 0  # Avoid division by zero if both dictionaries are empty
    return round((total_overlap_chars / total_unique_chars) * 100,2)




