class stringCompressor:
    def __init__(self, s):
        self.s = s

    def compres(self):
        
        from collections import defaultdict

        chat_count = defaultdict(int)
        
        # instace of char
        i = 0

        # Total len of string
        n= len(self.s)

        while i<n:
            char = self.s[i]
            i +=1
            freq_start = i

            while i < n and self.s[i].isdigit():
                i+=1
                freq = int(self.s[freq_start: i])
                chat_count[char] += freq

        return ''.join(f"{char}{chat_count[char]}" for char in sorted(chat_count))

s = 'a2b3a1c2n1c4'
compressor = stringCompressor(s)
result = compressor.compres()
print(result)

