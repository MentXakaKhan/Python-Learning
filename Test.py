https://cted.cybbh.io/tech-college/pns/public/pns/latest/guides/fg.html#_type_conversion

01 - Python Activity

Use python to produce code below that will create several named variables with the specified value:
Identifier	Value	Type
hello	hello	string
is_python_awesome	true	boolean
days_in_python	6	integer
pie_size	3.14	float




hello = "hello"
is_python_awesome = True
days_in_python = 6
pie_size = 3.14

///////////////////////////////////////////////////////////////////////////////////////////

02 - Python Activity

Use Python to produce code below that will convert the provided literal ("Starting Value"), convert it to the indicated data type by using the appropriate Python Built-in Function(s), and assign the output to the named variable as designated below.

string to int string to float int to string int to float
Identifier	Starting Value	Convert to Type
int_input	"345"	int
pi_4	"3.1415"	float
hours_str	40	string
hourly_rate	15	float


int_input = int("345")

pi_4 = float("3.1415")


hours_str = str(40)


hourly_rate = float(15)

/////////////////////////////////////////////////////////////////////////////////////////////////

03 - Python Activity
Use python to produce code below that will create several named variables with the specified value using math operators:

Identifier	Value	Type
x	16	integer
y	3	integer
xysum	sum of x and y	integer
xydiff	difference of x and y	integer
xyprod	product of x and y	integer
xyquo	quotient of x and y	float
xyintquo	integer quotient of x and y	integer
xymod	modulus of x and y	integer


x = 16
y = 3
xysum = x + y
xydiff = x - y
xyprod = x * y
xyquo = x / y
xyintquo = x // y
xymod = x % y


//////////////////////////////////////////////////////////////////////////////////////////////////

04 - Python Activity
Use python to produce code below that will create several named variables with the specified value using the str.format member function. You may assign any value for the variables other than output. The output variable must use the same boilerplate text and include the appropriate values assigned to the first three.

Identifier	Example Value	Type
name	Jerry	str
greeting	Sir	str
time	noon	str
output	Hello Jerry! Sir, will you be arriving by noon?	str



name = "Jerry"
greeting = "Sir"
time = "noon"

output = "Hello {}! {}, will you be arriving by {}?".format(name, greeting, time)


////////////////////////////////////////////////////////////////////////////////////////////////////

05 - Python Activity
Use python to produce code below that will perform the following:

Create a variable named sentence and assign the value 'good for all'
Turn the sentence variable into a list of individual characters and assign this to a variable named sent_list.
Change the first (index 0) character in the list to 'f'
Change the last (index -1) character in the list to '?'
Combine the list into a new string with periods ('.') in between each character and assign the result to a new variable named output.


sentence = "good for all"
sent_list = list(sentence)
sent_list[0] ="f"
sent_list[-1] = "?"
output = ".".join(sent_list)


//////////////////////////////////////////////////////////////////////////////////////////////////////////

00 - Mailbox Maintenance

Use python to produce code below that will:

Given an email address in email
Convert the email into a list name `lst'
The list will contain the individual parts of the email
Example: email = 'albert@genius.com' -> lst = ['albert', 'genius', 'com']
NOTE: A variable named email will be available to your code when running.
NOTE: You must create a variable named lst which contains the required data.
NOTE: Do not indent your code




notemail = email.replace('@','.')
lst = notemail.split('.')


/////////////////////////////////////////////////////////////////////////////////////////////////////////
06 - Python Activity

Use python to produce code below that will perform the following:

Read a string from the user, which is multiple numbers separated by spaces.
Change all spaces to a plus sign.
Print the resulting string to the user.


userstring = input()
userstring = userstring.replace(' ', '+')
print(userstring)


/////////////////////////////////////////////////////////////////////////////////////////////////////////

07 - Python Activity
10
coding python core
Use python to produce code below that will perform the following:

Read input from the user, the input will be an integer.
Determine which of the following categories the number fits into an print this to the user:
Negative Even
Negative Odd
Zero
Positive Even
Positive Odd


userinput = int(input())

if userinput > 0 and (userinput % 2) == 0:
    print('Positive Even')
elif userinput > 0 and (userinput % 2) != 0:
    print('Positive Odd')
elif userinput < 0 and (userinput % 2) != 0:
    print('Negative Odd')
elif userinput < 0 and (userinput % 2) == 0:
    print('Negative Even')
else:
    print('Zero')
    
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    
00A - Fizz Buzz
10
coding python core
FizzBuzz is an interview question that is said to filter out 99.5% of programming job candidates.

Add code so that it takes a number from the user and prints it (the number) if it isn’t divisible by 3 or 5. For multiples of 3 print 'fizz' instead. For multiples of 5 print 'buzz' instead. For multiples of 3 and 5 print 'fizzbuzz'.


usernumber = int(input())
if usernumber % 3 == 0 and usernumber % 5 == 0:
    print('fizzbuzz')
elif usernumber % 3 == 0:
    print('fizz')
elif usernumber % 5 == 0:
    print('buzz')
else:
    print(usernumber)
    
    
 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
 08 - Python Activity
10
coding python core
Use python to produce code below that will perform the following:

Create a function named domath that will accept 3 parameters.
The function will add the first two parameters and multiply this sum by the third parameter.
You can select the identifiers for each of the parameters.
The resulting product will be returned to the caller.



def domath(var1, var2, var3):
    num = (var1 + var2) * var3
    return num
    
//////////////////////////////////////////////////////////////////////////////////////////////////////////

  09 - Python Activity
10
coding python core
Use python to produce code below that will perform the following:

Read multiple lines from the user on standard input until an empty string is read.
Return a list of all these lines without line terminators
Each line should be reversed from how it is read in.




def reverseit():
    lst = []
    while True:
        userinput = input('Type in here:')
        if not userinput:
            break
        userinput = userinput[::-1]
        lst.append(userinput)
    return lst
            
            
 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
 
 00B - Guess Number
10
coding python core
Modify code below and implement guess_number so that it repeatedly asks the user for a number between 0 and 100, inclusive. If the user correctly guesses the value of the given argument n, print 'WIN' and return. Otherwise, indicate whether the guess was too high or too low.

def guess_number(n):
    while True:
        print('Guess a number between 0 and 100')
        userinput = int(input('Insert your guess:'))
        if userinput > 23:
            print('Too high')
        elif userinput < 23:
            print('Too low')
        elif userinput == 23:
            print('WIN')
            break
            return

guess_number(23)




////////////////////////////////////////////////////////////////////////////////////////////////////////////

10 - Python Activity
10
coding python core
Use python to produce code below that will perform the following:

Given a mixed case string as parameter s
Capitalize every letter with an even index within the string.
Lowercase every letter with an odd index within the string.
Return the resulting string.
Example - Given: "ABCDEF ghijkl" Return: "AbCdEf gHiJkL"
def leetString(s):
    pass 
    
    
    def leetString(s):
    empty = []
    for index in range(len(s)):
        if index % 2 == 0:
            empty.append(s[index].upper())
        else:
            empty.append(s[index].lower())
    return ''.join(empty)
    
 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 
 11 - Python Activity
10
coding python core
Use python to produce code below that will perform the following:

Print out every even number on a separate line from parameters first to last, inclusive.
Next, print out every odd number from first to last, inclusive.
def evensandodds(first, last):
    pass 
    
    
    
    def evensandodds(first, last):
    for num in range(first,last+1):
        if num % 2 == 0:
            print(num)
    for num in range(first,last+1):
        if num % 2 ==1:
            print(num)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
13 - Python Activity
10
coding python core
def make_tuple():
    '''
     Returns a tuple of the multiples of 10 from 1 to 100 inclusive.
     Args:
         None
     Returns:
         tuple: a tuple of the multiples of 10 from 1 to 100 inclusive
     '''
     pass    



atuple = []
def make_tuple():
    for num in range(0,101,10):
        if num % 10 == 0:
            atuple.append(num)
    del atuple[0]
    return tuple(atuple)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

13-1 - Python Activity
10
coding python core
def make_tuple(a,b):
    '''
    Returns a tuple of the multiples of 10 from a to b inclusive.
    Args:
        None
    Returns:
        tuple: a tuple of the multiples of 10 from a to b inclusive
    '''    


def make_tuple(a,b):
    atuple = []
    for num in range(a,b + 1):
        if num % 10 == 0:
            atuple.append(num)
        
    return tuple(atuple)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

14 - Python Activity
10
coding python core
def strings():
    '''
    Returns a tuple of the following strings:

    (empty string)

    Physics is the universe's operating system

    Args:
        None
    Returns:
        tuple: a tuple of strings
     '''
    pass
    
def strings():
    atuple = ['Physics is the universe\'s operating system']
    btuple = ['']
    return tuple(btuple + atuple)
   //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
   
 
 15 - Python Activity
10
coding python core
def disect(lst):
    '''
    Returns a tuple of the given list split into two equally sized halves.
    The given list will always consist of an even number of elements.
    Args:
        lst (lst): a list of elements
    Returns:
        tuple: a tuple of two lists
    '''
    pass    
    
    
def disect(lst):
    first, second = lst[:len(lst)//2], lst[len(lst)//2:]
    t = (first, second)
    return t
    
 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 
 16 - Python Activity
10
coding python core
def reverse_string(strng):
    '''
    Returns a copy of the given string reversed
    Args:
        strng (str): a string of alphanumeric characters
    Returns:
        str: a copy of the given string reversed
    '''    
    pass




def reverse_string(strng):
    strng = strng[::-1]
    return strng
    
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


17 - Python Activity
10
coding python core
def code_points(strng):
    '''
    Returns a list of ordinals for every character in the given string
    Args:
        strng (str): a string of alphanumeric characters
    Returns:
        list: ordinals of every character in the given string
    '''    
    pass
    



def code_points(strng):
    ordinals = [ord(strng[i]) for i in range (len(strng))]
    return ordinals
    
    
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

18 - Python Activity
10
coding python core
Use python to produce code below that will perform the following:

Read file specified by the path in inpath parameter and write all lines to the file specified by the outpath parameter.
Before writing out each line, add the line number starting with 1 follow by colon and space.


def linenums(inpath, outpath):
    f = open(inpath)
    lst = f.readlines() 
    output = list()
    n = 1
    for item in lst:
        output.append(str(n) + ": " + item)
        n = n + 1
    fs = open(outpath, 'w')
    fs.writelines(output)
 
 
 
 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 
 
 18-1 - The Little Orphan Annie Special
10
coding python core
"Sometimes my cousin is just mean. He sent me a file with a special message but made it into a crazy series of ones and zeros. He told me each letter was on its own line, and could be converted into an Unicode character. Can you help me by decoding his message?"

Each line will be a string character. You will need to convert the string Ones and Zeros into an integer (but these are not base 10, so keep that in mind) and then pass that data to code that will convert it to its corresponding Unicode character. Thanks to Python's "batteries included" philosophy, there are two Python built-in functions that can help handle this for you.

Hint: https://docs.python.org/3/library/functions.html#int
Hint: https://docs.python.org/3/library/functions.html#chr
def tough_read(fname):
     '''
     Args:
         fname (str): path to a file where the input is located
     Returns:
         str: Sentence that was decoded
     '''
     pass 
     
     
     
     
     
def tough_read(fname):
    with open(fname) as fp:
        answer = ''
        for line in fp:
            answer += chr(int(line,base=2))
        return answer
        
 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 
 18-2 Feeling Cute...Might Delete Later
10
coding python core
"You have a artist friend that likes to jot down some inspirational words when the mood strikes. These fits of inspiration always have a theme that they need to remember with the messages. Your friend needs some help keeping track. Read each of the inspirational messages from the user and write them to the end of the file specified by fname. Since the theme is important and must be remembered, add the theme and a colon before each message and ensure each inspirational message is on its own line. An empty input will indicate no more entries and the end of the theme."

Example:

If theme was "Razzmatazz", and the input from the user was "I like nonsense; it wakes up the brain cells. - Dr. Seuss", the resulting string would be formated as follows: Razzmatazz:I like nonsense; it wakes up the brain cells. - Dr. Seuss

Important:

What if there are other lines to be added? What else seperates lines in a file? What needs to be added to the example line above?
Do not overwrite the file. What mode should you open the file in?
def log_to_file(fname, theme):
     '''
     Args:
         fname (str): Path to an existing file that includes previous inspirational messages to keep.
         theme (str): Theme to be placed on each line.
     Returns:
         None
     '''
     pass 
     
     



def log_to_file(fname, theme):
    with open(fname, 'a') as fp:
        while True:
            line = input("please enter message: ")
            if not line:
                break
            fp.write('{}:{}\n'.format(theme,line))
            
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


18-3 The Replacements
10
coding python core
Replace all found instances of the individual tuple entries in the file found at in_path. Replacements will be in the list reps as a list of tuples. Each tuple entry will contain the 'find' as the first element and the 'replace' will be the second element. Write the result to the file specified with out_path.

Example:

List of Tuples example - [("taken","delivered"),("cat","dog"),("outside","beyond"),("straightaway","forthwith"),("possibly","perchance")]
Original string example - "The cat possibly needs to be taken outside, straightaway."
Changed string example - "The dog perchance needs to be delivered beyond, forthwith."
def replace_in_file(in_path, out_path, reps):
     '''
     Args:
         in_path (str): input file path
         out_path (str): output file path
         reps (list): list of tuples containing ("find", "replace") mappings
     Returns:
         None
     '''
     pass 
     
     
def replace_in_file(in_path, out_path, reps):
   fi = open(in_path)
   data = fi.read()
   fi.close()
   for f, r in reps:
       data = data.replace(f,r)
   fo = open(out_path)
   fo.write(data)
   fo.close()

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


19 - Python Activity
10
coding python core
def grab(lst):
    '''
    Returns a randomly chosen item from the given list (lst).
    Args:
        lst (list): a list of items
    Returns:
        item (?): an item from the list
        
        
def grab(lst):
    import random
    item = (random.choice(lst))
    return item
    
    
    
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


20 - Python Activity
10
coding python core
def get_hash(data="python"):
    '''
    Returns the SHA3 256-bit hash of the data provided.
    You will need to use the hashlib python library to complete this challenge.
       
    NOTE: The first call will use the string "python" later calls will use random strings
    NOTE: You can convert a string into a bytes-like object which is needed for hashing with: 
             
    data.encode("utf-8")
    
    NOTE: You can create a bytes-like object out of a literal by adding a b in front of the string, ie b"python" or b'python'
       
    Args:
        data (str): data to be encoded
    Returns:
        str : The SHA3 256-bit hash of the provided data
    '''    
    
    
    
def get_hash(data="python"):
    import hashlib
    j = data.encode()
    y = hashlib.sha3_256(j)
    return y.hexdigest()
    
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



21 - Python Activity
10
coding python core
Write a script that implements a function, find_product, which takes two numbers and returns the product. Use the name=='__main__' idiom to prompt the user for two integers and print the result of calling find_product using those integers.



def find_product(a,b):
        product = int(a*b)
        return product
if __name__ == '__main__':
     a = int(input('Enter first number: '))
     b = int(input('Enter second number: '))
     print(find_product(a,b))


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

22 - Python Activity
10
coding python core
Write a function, round_to_position, which takes a list of floats and returns a new list with the original floats each rounded to the number of digits of precision after the decimal point corresponding to the original float's position in the list.

def round_to_position(lst):
    pass
    
    


def round_to_position(lst):
    newlist = []
    for i in range(0, len(lst)):
        floaty = round(lst[i],i)
        newlist.append(floaty)
    return newlist
    
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

23 - Python Activity
10
coding python core
def get_type_str(obj):
    '''
    Returns the type of the parameter as a string.
    Possible types are:
    

      
string

      
boolean

      
integer

      
float

      
list

      
tuple

    

    NOTE: Any other types should be identified with 'unknown'
       
    Args:
        obj (?): The object that should be classified
    Returns:
        str : The type of the provided data
    '''   
    


def get_type_str(obj):
    if type(obj) == str:
        return ('string')
    elif type(obj) == bool:
        return ('boolean')
    elif type(obj) == int:
        return ('integer')
    elif type(obj) == float:
        return ('float')
    elif type(obj) == list:
        return ('list')
    elif type(obj) == tuple:
        return ('tuple')
    else:
        return ('unknown')
        
 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 
 24 - Python Activity
10
coding python core
Use python to produce code below that will perform the following:

A list of words is provided in the file specified by fname.
Another list of words is provided as the parameter words.
Return a list of all the words found in the file that are NOT contained in the list of words in parameter.
Each word in the file will be separated by at least one character of whitespace.
def diffwords(fname, words):
    pass 
    

def diffwords(fname, words):
    fjord = open(fname, 'r')
    rav = fjord.read()
    rav = rav.replace('\n', ' ')
    j = rav.split(' ')
    returnlst = []
    for value in j:
        if value not in words:
            returnlst.append(value)
    return returnlst
    
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


25 - Python Activity
10
coding python core
def count_words(filepath):
    '''
    Count the occurrences of each word in the file. Create a dictionary that contains each word in the file as a key
    and the value for each key will contain the number of times each words is found in the file. Words will be
    separated by one or more whitespace characters spread over multiple lines.
       
    Args:
        filepath (str): The path to the file
    Returns:
        dict : keys - words
               values - number of times each word appears
               
               


def count_words(filepath):
    text = open("filepath", "r")
    d = dict()
    for line in text:
        line = line.strip().lower()
        words = line.split(" ")
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
    return(d)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
26 - Python Activity
10
coding python core
Use python to produce code below that will perform the following:

Create a function called infinitearguments that will:
Print to standard output all positional arguments, in the order received, on separate lines.
Followed immediately by all keyword arguments in the form keyword=value in keyword alphabetic order.


def infinitearguments(*args, **kwargs):
    for i in args:
        print(i)
    for key, value in sorted(kwargs.items()):
        print("{}={}".format(key, value))
        
        
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

 
    27 - Python Activity
10
coding python core
def sort_ascii(filepath):
    '''
    Read all lines from file in `filepath` and return a list of all lines in case-insensitive ASCII order.
    Remove all linebreaks before sorting.
       
    Args:
        filepath (str): The path to the file
    Returns:
        list : lines from input file sorted into ASCII order without linebreaks
    '''
    
def sort_ascii(filepath):
    fjord = open(filepath, 'r')
    rav = fjord.readlines()
    lst = []
    for element in rav:
        lst.append(element.strip())
    return sorted(lst,key=str.lower)
    
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

28 - Python Activity
10
coding python core
def sort_length(filepath):
    '''
    Read all lines from file in `filepath` and return a list of all lines sorted longest to shortest.
    Remove all linebreaks before sorting.
       
    Args:
        filepath (str): The path to the file
    Returns:
        list : lines from input file sorted longest to shortest without linebreaks
    '''
    

def sort_length(filepath):
    q = open(filepath, 'r')
    e = q.read()
    r = e.split('\n')
    r.sort(key=len, reverse=True)
    return r
    
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


29 - Python Activity
10
coding python core
def sort_embedded(filepath):
    '''
    Read all lines from file in `filepath` and return a list of all lines sorted numerically by
    the number at character positions 10 to 15 in each line..
    Remove all linebreaks before sorting.
    
    Example: The embedded number is 561234 below.
    Here is a561234 long line of text from the file.
       
    Args:
        filepath (str): The path to the file
    Returns:
        list : lines from input file numerically sorted on the embedded number without linebreaks
    '''



def sort_embedded(filepath):
    fp = open(filepath, 'r')
    flist = fp.readlines()
    nlist = [line.strip() for line in flist]
    nlist.sort(key=lambda x: int(''.join(filter(str.isdigit,x))))
    return nlist

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

 120 - Like a million, literally
20
coding python core

def numsys(startint):
    """ Given an integer `startint`, convert this integer to its 
    binary version, octal version, and hexadecimal version and 
    return these as a tuple in the order given. """
    pass
    
def getints(binnum, octnum, decnum, hexnum):
    """ Given the string parameters `binnum` (binary number), 
    `octnum` (octal number), decnum` (decimal number), `hexnum` 
    (hexadecimal number), convert each of these  to an integer and 
    return them as a list in their parameter order. """
    pass
    
def literals():
    """ Create a list and set the value using literals and return 
    the list. All literals will represent the decimal integer value 
    1,000,000 (one million). You must use a literal to represent 
    the target value in binary, hexadecimal, decimal, and octal.
    The order is not important. """
    pass
    
 
def numsys(startint):
    binary = bin(startint)
    octal = oct(startint)
    hexad = hex(startint)
    return (binary, octal, hexad)
    
def getints(binnum, octnum, decnum, hexnum):
    binnum = int(binnum, 2)
    octnum = int(octnum, 8)
    decnum = int(decnum, 10)
    hexnum = int(hexnum, 16)
    return [binnum, octnum, decnum, hexnum]
def literals():
    return [0b11110100001001000000, 0o3641100, 1000000, 0xf4240]
    
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


01 - Mirror mirror
10
coding python
Given a string of multiple words separated by single spaces, return a new string with the sentence reversed. The words themselves should remain as they are.

For example, given 'it is accepted as a masterpiece on strategy', the returned string should be 'strategy on masterpiece a as accepted is it'.

def q1(sentence):
    pass
    


def q1(sentence):
    s = sentence.split(" ")
    left = 0
    right = len(s) - 1
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    s = " ".join(s)
    return s
    
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

02 - Sprinkle some commas in there
10
coding python
Given a positive integer, return its string representation with commas seperating groups of 3 digits.

For example, given 65535 the returned string should be '65,535'.

def q1(n):
    pass
 
 
 
 
    
def q1(n):
    return "{:,}".format(n)
    
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

03 - Bring it together and make it pretty
10
coding python
Given two lists of integers, return a sorted list that contains all integers from both lists in descending order.

For example, given [3,4,9] and [8,1,5] the returned list should be [9,8,5,4,3,1]. The returned list may contain duplicates.

def q1(lst0, lst1):
    pass
    
    
    
def q1(lst0, lst1):
    x=lst0+lst1
    #t=x.sorted(reverse=True)
    return sorted(lst0+lst1,reverse = True)
    
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

04 - Pass GO and collect $200
10
coding python
Given 3 scores in the range [0-100] inclusive, return 'GO' if the average score is greater than 50. Otherwise return 'NOGO'.

def q1(s1,s2,s3):
    pass
    
    
def q1(s1,s2,s3):
    b = (s1+s2+s3)/3
    if b > 50:
        return 'GO'
    else:
        return 'NOGO'
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


10 - In other words, non-sequential
10
coding python
Given a list of positive integers sorted in ascending order, return the first non-consecutive value. If all values are consecutive, return None.

For example, given [1,2,3,4,6,7], the returned value should be 6.

def q1(arr):
    pass
    
    


def q1(arr):
    i = 1
    for x in arr:
        if i < len(arr) and arr[i] - arr[i-1] != 1:
            return arr[i]
        i += 1
    return None
