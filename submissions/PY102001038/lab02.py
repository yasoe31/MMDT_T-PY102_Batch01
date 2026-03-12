"""
Lab 02 — Stack & Queue Practice (4 Questions)

Rules:
- Do NOT use input() or print() in your solutions.
- Implement the functions below exactly with the given names.
- Use stack/queue operations (append/pop for stack; collections.deque for queue is recommended).

Questions:
  Q1) is_balanced_parentheses(s)
  Q2) next_greater_to_right(nums)

  Q3) first_non_repeating(stream)
  Q4) hot_potato(names, k)
"""

from collections import deque


# -------------------------
# Stack Questions (2)
# -------------------------

def is_balanced_parentheses(s: str) -> bool:
    """
    Return True if the string s has balanced brackets: (), {}, [].
    Ignore non-bracket characters.

    Examples:
      is_balanced_parentheses("([]){}") -> True
      is_balanced_parentheses("(]") -> False
      is_balanced_parentheses("a+(b*c)-{d/e}") -> True
    """
    # TODO: implement using a stack
    #raise NotImplementedError

    my_dict = {")":"(","}":"{","]":"["}
    local_list = []

    for char in s :
        if char in my_dict :
            if len(local_list) == 0 :
                return False
            last_char = local_list[-1]

            #This is o(n) because I have to loop through
            while last_char != my_dict[char] :
                local_list.pop()
                last_char = local_list[-1]

            if last_char == my_dict[char] :
                local_list.pop()

        else :
            local_list.append(char)

    if len(local_list) == 0 : #nothing left to check and expected result
        return True

    if len(local_list) > 0 : #something left and have to check whether there is any opening or closing

        reverse_my_dict = {v: k for k, v in my_dict.items()}
        for x in local_list :
            key_search = my_dict.get(x) # searching ), ] or }
            if key_search is not None:
                    return False # found one of ),} or ]

            value_search = reverse_my_dict.get(x) # searching (,[,{
            if value_search is not None :
                return False # found one of (,{,[

    return True


def next_greater_to_right(nums: list[int]) -> list[int]:
    """
    For each element, find the next greater element to its right.
    If none exists, output -1 for that position.

    Example:
      nums = [2, 1, 2, 4, 3]
      output -> [4, 2, 4, -1, -1]
    """
    # TODO: implement using a stack (monotonic stack)
    #raise NotImplementedError

    local_list = [-1] * len(nums)
    local_idx_list = []

    for i, num in enumerate(nums) :
        while local_idx_list and nums[local_idx_list[-1]] < num :
            pop_idx = local_idx_list.pop()
            local_list[pop_idx] = num
        local_idx_list.append(i)

    return local_list


# -------------------------
# Queue Questions (2)
# -------------------------

def first_non_repeating(stream: str) -> str:
    """
    Given a stream of lowercase letters, build a result string where each character
    is the first non-repeating character seen so far. If none exists, use '#'.

    Example:
      stream = "aabc"

      Process step by step:
      a → 'a'   # 'a' appears once, so it is the first non-repeating character
      a → '#'   # 'a' now appears twice; no character appears once, so use '#'
      b → 'b'   # 'b' appears once and is the first non-repeating character
      c → 'b'   # 'a' repeats, 'b' appears once, 'c' appears once;
                # 'b' appeared earlier than 'c', so output 'b'

      Output: "a#bb"
    """
    # TODO: implement using a queue + counts
    #raise NotImplementedError

    local_deque = deque()

    for i in range(len(stream)) :
        given_char = stream[:i+1]
        non_repeated = deque(ch for ch in given_char if given_char.count(ch) == 1)

        if non_repeated :
            non_rep_single_value = non_repeated.popleft()
            local_deque.append(non_rep_single_value)
        else :
            local_deque.append("#")

    return ''.join(local_deque)



def hot_potato(names: list[str], k: int) -> str:
    """
    Simulate the Hot Potato game.

    - names is a list of players in initial order.
    - The potato starts with the first person in the list.
    - Pass the potato exactly k times in a circular manner.
    - After the k-th pass, eliminate the person holding the potato.
    - The person immediately after the eliminated player
      (in circular order) holds the potato next.
    - Continue until one player remains. Return the winner's name.

    Example:
      names = ["A", "B", "C", "D"]
      k = 2
      1st round:
      - "A"--> "B-->C
      - C is eliminated.
      - Remaining: ["A", "B", "D"]
      - Next HOlder: "D"
      2nd round:
      - "D" --> "A" --> "B"
      - B is eliminated
      - Remaining: ["D", "A"]
      3rd round:
      - "D"--> "A" --> "D"
      - D is eliminated.

     Winner: "A"

    """
    # TODO: implement using a queue (deque)
    #raise NotImplementedError

    local_deque = deque(names)
    while len(local_deque) != 1 :
        local_deque.rotate(k)
        local_deque.popleft()
        k = k -1

    return local_deque.pop()




print(hot_potato(names = ["A", "B", "C", "D"],k=2))

#print(is_balanced_parentheses("(a)")) # expected True
#print(is_balanced_parentheses("((a)")) # expected False
#print(is_balanced_parentheses("{[(a)]}")) # expected True
#print(is_balanced_parentheses("a+(b*c)-{d/e}")) # expected True
#print(is_balanced_parentheses("{[(a)")) # expected False - {,[

#print(next_greater_to_right([2,1,2,4,3]))
#print(next_greater_to_right([2, 1, 3, 2]))

#print(first_non_repeating("aabc"))


def non_repeated_test(given) :

    non_repeated = {ch for ch in given if given.count(ch) == 1}

    return non_repeated

#non_repeated_test("12348546478")
