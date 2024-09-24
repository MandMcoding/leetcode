int minExtraChar(char * s, char ** dictionary, int dictionarySize){
    int total_length = 0;
    //for each word in dict
    for(int i = 0; i < dictionarySize; i++){
        //find length of word
        const char* letter = dictionary[i];
        while(*letter != '\0'){
            letter++;
        }
        int word_len = letter-dictionary[i];

        //loop through s 
        letter = s;
        const char* end = s+word_len;
        const char* dict_letters = dictionary[i];
        while(*end != '\0'){
            //checking for the word in s
            if(*letter == *dict_letters){ //first letters match
                const char* temp_letter = letter;
                const char* temp_dict_letter = dict_letters;
                for(int j = 0; j < word_len; j++){//check if there's a match
                    if(*temp_letter != *temp_dict_letter){//if not go to the letter++ line
                        break;
                    }
                    temp_letter++;
                    temp_dict_letter++;
                }
                //All characters match, sucsesfull find
                total_length += word_len; //count the length of each succsessfull find
                break;//leave checking loop
            }
            letter++;
            end++;
        }
    }
    //subtract the length of s with count
    int s_length = 0;//fucking getting s length bruh
    const char* letter = s;
    while(letter != '\0'){
        letter++;
        s_length++;
    }

    return s_length-total_length;
}