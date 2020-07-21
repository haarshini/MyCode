def count_substring(s, b):
    a= len([i for i in range(len(s)) if s[i:i+len(b)] == b])
    return a
