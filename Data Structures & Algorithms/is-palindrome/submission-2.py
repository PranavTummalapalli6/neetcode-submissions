class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = ""
        pattern = r"[^a-zA-Z0-9]"
        arr += re.sub(pattern, "", s).lower()
        left_ptr = 0
        right_ptr = int(len(arr) - 1)
        for i in range(int(len(arr)/2)):
            if arr[left_ptr] == arr[right_ptr]:
                left_ptr += 1
                right_ptr -= 1
            else:
                return(False)
        return(True)