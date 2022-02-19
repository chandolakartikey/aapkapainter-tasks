def anagram(s1, s2):
    
    if(sorted(s1.lower())== sorted(s2.lower())):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        

str ="Mary"
str1 ="army"
anagram(str, str1)
