import myFunct 
import text_input as text
import SERA


punctuations={'<','>','.','፡','።','፦', '፣', '–','÷','፥','፤','!','[',']','#','*','?',"‘", "’",'“','”','/','\\','(',')',"-",'=','+','%',"'",'"','0','1','2','3','4','5','6','7','8','9','፩', '፪', '፫', '፬', '፭', '፮', '፯', '፰', '፱', '፲', '፳', '፴', '፵', '፶', '፷', '፸', '፹', '፺', '፻', '፼','I','V','x','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

cleaned_amharic_text= myFunct.clean(text.amharic_input_text, punctuations)
cleaned_tigrigna_text= myFunct.clean(text.tigrigna_input_text, punctuations)
'''
print(cleaned_amharic_text)
print(cleaned_tigrigna_text)
print(type(cleaned_amharic_text))
'''
cleared_amharic_text= myFunct.clear_space(cleaned_amharic_text)
cleared_tigrigna_text= myFunct.clear_space(cleaned_tigrigna_text)

'''
print(cleared_amharic_text)
print(cleared_tigrigna_text)
'''
tokenized_amharic_text= myFunct.tokenize(cleared_amharic_text)
tokenized_tigrigna_text= myFunct.tokenize(cleared_tigrigna_text)

'''
print(tokenized_amharic_text)
print(tokenized_tigrigna_text)
print (type(tokenized_amharic_text))
print (type(tokenized_tigrigna_text))
'''

amharic_stop_words={"እና", "ነው","እንዲሁም", "ላይ", "እስከ","ብቻ", "ወደ","ከዚህ","ወይም","ዓም","ዶር","ብቶ","ም", "አም", "ስለ", "ይህ", "እዚህ","እ","ኋላ", "ወይ"}
tigrigna_stop_words ={"ኣብ","ካብ", "እቲ", "ኣብዚ","ከዓ", "ድማ", "ብቻ","እንተ", "እዚ", "እዛ", "ዝኾነ","እዞም", "እቶም","እውን", "እንታይ", "ናይ", "ከም", "ንበለይ", "ናብ", "እሞ", "ናብዚ", "ከምዚ", "ከምኡ", "እንተንበለይ", "ወይ"}

removed_amharic_text= myFunct.remove_sw_amharic(tokenized_amharic_text, amharic_stop_words)
removed_tigrigna_text= myFunct.remove_sw_tigrigna(tokenized_tigrigna_text, tigrigna_stop_words)

'''
print(removed_amharic_text)
print()
print(removed_tigrigna_text)
'''

lemmatized_amharic_text=  myFunct.lemmatize_amharic(myFunct.lemmatize_amharic2 (removed_amharic_text))
lemmatized_tigrigna_text= myFunct.lemmatize_tigrigna(myFunct.lemmatize_tigrigna2(removed_tigrigna_text))

'''
print(lemmatized_amharic_text)
print()
print(lemmatized_tigrigna_text)
print()
print(type(lemmatized_amharic_text))
'''

normalized_amharic_text=myFunct.normalize(lemmatized_amharic_text)
normalized_tigrigna_text=myFunct.normalize(lemmatized_tigrigna_text)

#casting the type to Set in order to apply unique count
amharic_words=set(normalized_amharic_text)
tigrigna_words=set(normalized_tigrigna_text)

#Counting unique words from the list preprocessed words
amh_unique_wc=len(amharic_words)
tig_unique_wc=len(tigrigna_words)

total_words=len(normalized_amharic_text)+len(normalized_tigrigna_text)                                   #All words in the list
shared_words = amharic_words.intersection(tigrigna_words)                 #Only Shared Words
total_unique_words=amh_unique_wc+tig_unique_wc-len(shared_words)          #Only Unique words(without repetition)
Shared_percentage= (len(shared_words))/(total_unique_words) * 100                 

print()                                                            #New line for readability
print(f'The following are shared words in both languages from {total_words} words :\n{shared_words}')
print()
print(f'Number of Amharic Unique Words: {amh_unique_wc}')
print(f'Number of Tigrigna Unique Words: {tig_unique_wc}')    
print()  
print(f'The number of shared words in both languages from the text input is: {len(shared_words)}')                                                                                      #New line for readability
print(f'The Shared words percentage: {round(Shared_percentage,2)}%')
print()

#Computing overlap percentage
myFunct.compare(amharic_words,tigrigna_words)

#Transcription
transcribed_amh_words = myFunct.transcribe_words(lemmatized_amharic_text,SERA.transcription_dict)
transcribed_tig_words = myFunct.transcribe_words(lemmatized_tigrigna_text,SERA.transcription_dict)

print()
print(f' G2p Transcription of amharic words:\n {transcribed_amh_words}')
print()
print(f' G2p Transcription of amharic words:\n {transcribed_tig_words}')


am_character_frequency = myFunct.count_character_frequency(removed_amharic_text)
tig_character_frequency = myFunct.count_character_frequency(removed_tigrigna_text)

print(f' Amharic phoneme/Character frequency: \n{am_character_frequency}')
print(f' Tigrigna phoneme/Character frequency: \n{tig_character_frequency}')


overlap_dict = myFunct.compute_overlap(am_character_frequency, tig_character_frequency)

# Print the frequency dictionary for Tmharic and Tigrigna
'''
for char, frequencies in overlap_dict.items():
    print(f"Character: {char}, Amharic Frequency: {frequencies['frequency_in_am']}, Tigrinya Frequency: {frequencies['frequency_in_tig']}")
'''

print(f'phoneme level percentage overlap: {myFunct.phoneme_overlap_percentage(am_character_frequency, tig_character_frequency)}%')