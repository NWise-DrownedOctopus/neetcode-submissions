class Solution:

    # For a first attempt I think we should first concatanate all of the strings together, but then somehow encode how to break them back apart
    # we could append some sort of header to the string that would contain all the relevent info needed to split apart the string 
    # once concatanated

    # What we know:
    # Our input strs will have less than 100 unique strings
    # each individual string within that input will be less than 200 characters

    # Header info needed. First we should encode how many unique strings are being concatanated. It will be an integer between 0 and 100
    # so the header will have three characters reserved for this.

    # After those three digits we should store the length of each individual string as an integer. Because it's length can be up to 200
    # I will also reserve three characters for each entry 

    # For example:
    # ["Hello","World"]
    # Header would be "002005005" 002 because there are 2 strings, and '005' '005' because hello and world are of length 5

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        header = ""
        body = ""

        body_length = len(strs)
        print("String List Length = " + str(body_length))

        header += self.formatInt(body_length)

        for string in strs:
            header_entry = self.formatInt(len(string))
            header += header_entry
            body += string

        return header + body
        

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        print(s)
        # First we grab the original length of the list of strings
        length = int(s[0:3])
        print("String List Length = " + str(length))

        # Now we can seperate the body from the header
        header_length = 3 * (length + 1) # we add one for header length at front
        header = s[3:header_length]
        body = s[header_length:]

        print("Header: " + header)
        print("Body: " + body)
        output = []

        i = 0
        while i < length:
            string_length = int(header[0:3])
            #if string_length == 0:
            #    output.append("")
            #    i += 1
                
            output.append(body[0:string_length])
            body = body[string_length:]
            header = header[3:]
            i += 1      
        
        return output

    def formatInt(self, i: int) -> str:
        output = ""
        if i < 10:
            output += "00"
            output += str(i)
        elif i < 100:
            output += "0"
            output += str(i)
        else:
            output += str(i)
        return output
