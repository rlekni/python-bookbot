def count_words(contents):
    split_words = contents.split()
    return len(split_words)

def count_chars(input):
    results = {}
    for c in input:
        lowered = c.lower()
        if lowered in results:
            results[lowered] += 1
        else:
            results[lowered] = 1
    return results

def sort_on(dict):
    return dict["count"]

def sort_results(char_dic):
    results = []
    for ch in char_dic:
        dic = {"char": ch, "count": char_dic[ch]}
        results.append(dic)
    results.sort(reverse=True, key=sort_on)
    return results