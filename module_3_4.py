def single_root_words(root_word,*other_words):
    same_words=[]
    a = root_word
    for i in other_words:
         if a.lower() in i.lower():
            same_words.append(i)
         if i.lower() in a.lower():
            same_words.append(i)
         else:
             continue
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)