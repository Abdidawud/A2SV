class Solution:
    def interpret(self, command: str) -> str:
        result=''
        for i in range(len(command)):
            if command[i]=='G':
                result += 'G'
                i+=1 
            elif command[i:i+2]=='()':
                result += 'o'
                i+=2
            elif command[i:i+4]=='(al)':
                result +='al'
                i+=4

            else:
                i+=1

        return result    