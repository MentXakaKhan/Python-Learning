PyCore

00
split_email = email.replace(".", "@")
lst = split_email.split("@")

00A
num = int(input("Enter a number: "))
mod3 = num % 3
mod5 = num % 5
s = ""
if mod3 != 0 and mod5 != 0:
    s = str(num)
if mod3 == 0:
    s += "fizz"
if mod5 == 0:
    s += "buzz"
print(s)

00B
def guess_number(n):
    while True:
        user_guess = int(input("Guess a number: "))
        if user_guess == n:
            print("WIN")
            break
        elif user_guess < n:
            print("too low")
        else:
            print("too high")

guess_number(23)

01
hello = "hello"
is_python_awesome=True
days_in_python=6
pie_size = 3.14

02
int_input = int("345")
pi_4 = float("3.1415")
hours_str = str(40)
hourly_rate = float(15)

03
x = 16
y = 3
xysum = x+y
xydiff = x - y
xyprod = x * y
xyquo = x / y
xyintquo = x // y
xymod = x % y

04 name = "Jerry"
greeting = "Sir"
time = "noon"
output = "Hello {}! {}, will you be arriving by {}?".format(name,greeting,time)

05
name = "Jerry"
greeting = "Sir"
time = "noon"
output = "Hello {}! {}, will you be arriving by {}?".format(name,greeting,time)

06
user_input = input("Enter Numbers: ")
print(user_input.replace(" ", "+"))

07
num = int(input("Enter a number: "))
if num == 0:
    print("Zero")
if num < 0:
    if num % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
elif num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")

08
def domath(num1, num2, num3):
    return (num1+num2)*num3

09
def reverseit():
    lst = []
    while True:
        inpt = input("Enter input: ")
        if inpt == "":def strings():
    return ("", "Physics is the universe's operating system")
            break
        else:
            lst.append(inpt[::-1])
    return lst

10
def leetString(s):
    strng = ""
    for i, x in enumerate(s):
        if i % 2 == 0:
            strng += x.upper()
        else:
            strng += x.lower()
    return strng

11
def evensandodds(first, last):
    evens = []
    odds = []
    for i in range(first, last + 1):
        if i % 2 == 0:
            evens.append(str(i))
        else:
            odds.append(str(i))
    even_s = "\n".join(evens) + "\n"
    odd_s = "\n".join(odds)
    print(even_s+odd_s)

13
def make_tuple():
    i = 1
    tup = []
    while 10 * i <= 100:
        tup.append((10 * i))
        i += 1
    return tuple(tup)
def strings():
    return ("", "Physics is the universe's operating system")
    return tuple(tup)

14
def strings():
    return ("", "Physics is the universe's operating system")

15
def disect(lst):
    i = len(lst) // 2
    return (lst[:i:], lst[i::])

16
def reverse_string(strng):
    return strng[::-1]

17
def code_points(strng):
    return [ord(x) for x in strng]

18
def linenums(inpath, outpath):
    fp_in = open(inpath)
    fp_out = open(outpath, "w")
    lines = fp_in.readlines()
    for i, l in enumerate(lines):
        fp_out.write(str(i+1) + ": " + l)
    fp_in.close()
    fp_out.close()

18-1
def tough_read(fname):
    fp = open(fname)
    lines = fp.readlines()
    fp.close()
    s_lst = [chr(int(l, 2)) for l in lines]
    return "".join(s_lst)

18-2
def log_to_file(fname, theme):
    with open(fname, "a") as fp:
        while True:
            sent = input("Write something: ")
            if sent == "":
                break
            fp.write(theme + ":"+sent + '\n')

18-3
def replace_in_file(in_path, out_path, reps):
    in_fp = open(in_path)
    in_s = "".join(in_fp.readlines())
    in_fp.close()
    for t in reps:
        in_s = in_s.replace(t[0], t[1])
    with open(out_path,"w") as out_fp:
        out_fp.write(in_s)

19
import random
def grab(lst):
  return random.choice(lst)

20
import hashlib
def get_hash(data="python"):
    d = data.encode()
    hash_obj = hashlib.sha3_256(d)
    return hash_obj.hexdigest()

21
def find_product(x, y):
    return x * y

if __name__ == "__main__":
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a second number: "))
    print(find_product(num1, num2))

22
def round_to_position(lst):
    an = []
    for i, n in enumerate(lst):
        an.append(round(n, i))
    return an

23
def get_type_str(obj):
    if type(obj) == str:
        return "string"
    elif type(obj) == bool:
        return "boolean"
    elif type(obj) == int:
        return "integer"
    elif type(obj) == float:
        return "float"
    elif type(obj) == list:
        return "list"
    elif type(obj) == tuple:
        return "tuple"
    else:
        return "unknown"

24
def diffwords(fname, words):
    fp = open(fname)
    data = fp.read()
    data = data.split()
    return [w for w in data if w not in words]

25
def count_words(filepath):
    fp = open(filepath)
    data  = fp.read()
    data = data.split()
    an = {}
    for w in data:
        if w in an:
            an[w] += 1
        else:
            an[w] = 1
    return an

26
def infinitearguments(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, val in sorted(kwargs.items()):
        print(key + "=" + str(val))

27
def sort_ascii(filepath):
    fp = open(filepath)
    data = fp.readlines()
    fp.close()
    data = [x.strip() for x in data]
    return sorted(data, key=str.casefold)

28
def sort_length(filepath):
    fp = open(filepath)
    data = fp.readlines()
    fp.close()
    data = [x.strip() for x in data]
    return sorted(data, key=len, reverse=True)

29
def sort_embedded(filepath):
    fp = open(filepath)
    data = fp.readlines()
    fp.close()
    data = [x.strip() for x in data]
    return sorted(data,key=lambda x: int(x[9:15:]))

120
def numsys(startint):
    return (bin(startint), oct(startint), hex(startint))

def getints(binnum, octnum, decnum, hexnum):
    return [int(binnum, 2), int(octnum, 8), int(decnum, 10), int(hexnum, 16)]

def literals():
    return [0b11110100001001000000, 0xf4240, 0o3641100, 1000000]

PyCore-10

100
def complexity(password):
    an = 0
    if len(password) > 14:
        an |= 0x1
    if any([c.isdigit() for c in password]):
        an |= 0x2
    if any([c.isupper() for c in password]):
        an |= 0x4
    if any([c.islower() for c in password]):
        an |= 0x8
    s = """~!"@#$%^&'*_-+=`|(){}[]:;<>,.?/"""
    if any([c for c in password if c in s]):
        an |= 0x10
    return an

101
def perms(mode):
    p = [(4, "r"), (2, "w"), (1, "x")]
    s = ""
    for digit in [int(n) for n in str(oct(mode)[2::])]:
        for key, value in p:
            if digit >= key:
                s += value
                digit -= key
            else:
                s += "-"
    return s

102
def crack(username):
    pin = 0
    while True:
        try:
            pin_s = f"{pin:04d}"
            login_attempt = login(username, pin_s)
            if login_attempt:
                break
        except PermissionError:
            pin += 1
            pass
    return f"{pin:04d}"

103
#!/usr/bin/env python3

class TicTacToe:

    def __init__(self):
        self.board = []
        self.player = "1"
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append('-')
            self.board.append(row)

    def move(self, row, col):
        # Raise an Exception for invalid moves
        if row < 0 or row > 2:
            raise Exception("Invalid move")
        if col < 0 or col > 2:
            raise Exception("Invalid move")
        if self.board[row][col] != "-":
            raise Exception("Invalid move")
        self.board[row][col] = self.player
        win = self.check_board()
        self.player = "1" if self.player == "2" else "2"
        return win

    def check_board(self):
        # Return 1 as an int if player 1 wins as a result of this move
        # Return 2 as an int if player 2 wins as a result of this move
        # Return 0 as an int if a draw results from this move
        # Return None if nothing results from this move
        win = None
        n = len(self.board)

        # check rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != self.player:
                    win = None
            if win:
                return 1 if self.player == "1" else 2

        # check columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != self.player:
                    win = None
            if win:
                return 1 if self.player == "1" else 2

        # check diagnols
        win = True
        for i in range(n):
            if self.board[i][i] != self.player:
                win = None
        if win:
            return 1 if self.player == "1" else 2

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != self.player:
                win = None
        if win:
            return 1 if self.player == "1" else 2

        # check draw
        win = True
        for i in range(n):
            for j in range(n):
                if self.board[i][j] == '-':
                    win = None
        if win:
            return 0
        return win

104
#!/usr/bin/env python3

class MacAddress:
    OUI = {
        bytes([0xda,0xa1,0x19]): 'Google, Inc.',
        bytes([0xca,0x12,0x5c]): 'Microsoft Corporation',
        bytes([0x3a,0x35,0x41]): 'Raspberry Pi (Trading) Ltd',
    }

    def __init__(self,mac):
        self.mac = mac
        self.mac_l = mac.split(":")
        mac_s = "".join(self.mac_l)
        self.mac_b = bytes.fromhex(mac_s)

    def is_multicast(self):
        # test case checks the LSB of last octet, not LSB of first octet
        return True if self.mac_b[len(self.mac_b) - 1] & 1 else False

    def organization(self):
        mac_oui = self.mac_b[:3]
        if mac_oui in self.OUI:
            return self.OUI[mac_oui]
        else:
            return "Unknown"

    def __str__(self):
        mac = ":".join(self.mac_l)
        org = self.organization()
        return "{} {}".format(mac,org)

105
#!/usr/bin/env python3

class Calculator:

    def __init__(self):
        self.memory = 0
        self.last_result = 0

    def add(self,a,b):
        op1 = self.get_operand(a)
        op2 = self.get_operand(b)
        self.last_result = op1+op2
        return self.last_result

    def sub(self,a,b):
        op1 = self.get_operand(a)
        op2 = self.get_operand(b)
        self.last_result = op1-op2
        return self.last_result

    def mul(self,a,b):
        op1 = self.get_operand(a)
        op2 = self.get_operand(b)
        self.last_result = op1*op2
        return self.last_result

    def div(self,a,b):
        op1 = self.get_operand(a)
        op2 = self.get_operand(b)
        self.last_result = op1/op2
        return self.last_result

    def store(self):
        self.memory = self.last_result

    def recall(self):
        self.last_result = self.memory

    def get_operand(self,a):
        op = a
        if a == "":
            op = self.last_result
        if a == "memory":
            op = self.memory
        return op

    def __str__(self):
        return str(self.last_result)

106
class Polygon:
    polygons = {
        3 : "triangle",
        4 : "quadrilateral",
        5 : "pentagon",
        6 : "hexagon",
        7 : "septagon",
        8 : "octagon",
        9 : "nonagon",
        10 : "decagon",
        11 : "undecagon",
        12 : "dodecagon",
        13 : "tridecagon",
        14 : "tetradecagon",
        15 : "pentadecagon",
        16 : "hexadecagon",
        17 : "heptadecagon",
        18 : "octadecagon",
        19 : "enneadecagon",
        20 : "icosagon"
    }
    def __init__(self):
        self.angles = []

    def add_angle(self, a):
        if a < 0 or a == 180 or a > 359:
            raise ValueError("Invalid angle")
        self.angles.append(a)

    def remove_angle(self, a):
        if a not in self.angles:
            raise ValueError("Angle not in list")
        self.angles.remove(a)

    def __str__(self):
        angle_sum = sum(self.angles)
        final_angle = ((((len(self.angles) + 1)) - 2) * 180) - angle_sum
        if final_angle < 0 or final_angle == 180 or final_angle > 359:
            raise ValueError("Invalid polygon")
        angle_list = [a for a in self.angles]
        angle_list.append(final_angle)
        return "{}: {}".format(self.polygons[len(angle_list)], angle_list)

PyPracticeV2

01
def q1(sentence):
    return " ".join(reversed(sentence.split()))

02
def q1(n):
    return "{:,}".format(n)

03
def q1(lst0, lst1):
    lst = lst0 + lst1
    lst = sorted(lst, reverse=True)
    return lst

04
def q1(s1,s2,s3):
    avg = (s1 + s2 + s3) / 3
    if avg > 50:
        return "GO"
    else:
        return "NOGO"

05
def q1(integer, limit):
    lst = []
    if integer != 0:
        lst.append(0)
    l = limit // integer
    for i in range(1, l + 1):
        num = integer * i
        if num % 2 == 0:
            lst.append(num)
    return lst

06
def q1(f0, f1):
    fp0 = open(f0)
    fp1 = open(f1)
    f0_lines = fp0.readlines()
    f1_lines = fp1.readlines()
    differ = []
    for i in range(len(f0_lines)):
        if f0_lines[i] != f1_lines[i]:
            differ.append(i)
    fp0.close()
    fp1.close()
    return differ

07
def q1(lst):
    dups = []
    for x in lst:
        if x in dups:
            return x
        dups.append(x)

08
def q1(strng):
    lst = strng.split()
    shortest = len(lst[0])
    for word in lst:
        if len(word) < shortest:
            shortest = len(word)
    return shortest

09
def q1(strng):
    s = ""
    for c in strng:
        if c.isdigit():
            s += c
    return chr(int(s))

10
def q1(arr):
    if len(arr) == 1:
        return arr[0]
    next_val = arr[0]
    for i in arr:
        if i != next_val:
            return i
        next_val = i + 1
    return None

PyPracticeV1-10

15
def q1(filename, overwrite, bytestowrite):
    x = 0
    if not filename:
        x |= 0x1
    if overwrite:
        x |= 0x10
    if bytestowrite > 1000000:
        x |= 0x20
    return x

PyPracticeV1

01
def q1(floatstr):
    return list(map(lambda x: float(x), floatstr.split(",")))

02
def q1(*args):
    avg = 0.0
    for num in args:
        avg += float(num)
    return avg / len(args)

03
def q1(lst,n):
    start = len(lst) - n
    return lst[start:len(lst)]

04
def q1(strng):
    lst = []
    for c in strng:
        lst.append(ord(c))
    return lst

05
def q1(strng):
    return tuple(strng.split())

06
def q6(catalog, order):
    total = 0.0
    for o in order:
        total = total + (catalog[o[0]] * o[1])
    return total

07
def q1(filename):
    line_len = 0
    with open(filename) as fp:
        line_len = len(fp.readline()) - 1
    return line_len

08
def q1(filename,lst):
    with open(filename, 'a') as fp:
        for line in lst:
            if line.lower() == "stop":
                break
            fp.write(line)
            fp.write('\n')

09
def q1(miltime):
    if miltime in range(0, 259):
        return "Good Night"
    elif miltime in range(300,1159):
        return "Good Morning"
    elif miltime in range(1200,1559):
        return "Good Afternoon"
    elif miltime in range(1600, 2059):
        return "Good Evening"
    elif miltime in range(2100,2359):
        return "Good Night"

10
def q1(numlist):
    positive = True
    for num in numlist:
        if num < 0:
            positive = False
    return positive
