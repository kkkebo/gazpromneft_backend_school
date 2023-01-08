def is_palindrome(s: str) -> bool:
    s = [i.lower() for i in s if i.isalnum()]
    return s == s[::-1]
