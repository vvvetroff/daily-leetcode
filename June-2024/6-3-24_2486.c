/* 
 * 2486. Append Characters to 
 *       String to Make Subsequence
 *
 *  You are given two strings s and t,
 *  consisting of only lowercase English letters
 *
 *  Return the minimum number of characters
 *  that need to be appended to the end of s
 *  so that t becomes a subsequence of s.
 *
 *  A subsequence is a string that can be
 *  derived from another string by
 *  deleting some or no characters
 *  without changing the order of the 
 *  remaining characters.
 *
 *  Decided to write this in C 
 *  since the constraints to this
 *  problem were very slim, and 
 *  that the answer was ez.
 *  O(n) time, O(1) space
 * */
#include <string.h>

int appendCharacters(char* s, char* t) {
    unsigned int sp = 0;
    unsigned int tp = 0;
    unsigned int sn = strlen(s);
    unsigned int tn = strlen(t);

    while(sp < sn && tp < tn){
        if(s[sp] == t[tp]){
            sp++;
            tp++;
        } else sp++;
    }
    return tn - tp;
}



