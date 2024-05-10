__Video link__ https://youtu.be/csbV0rv38nA 

# Variables
__Memory location__
b = 3.14
print(b)


# Data Types
__4 Data types__  \
name = "gaju" ```#string``` - everything is calculated as string \
age = 73 ```int``` - whole number \
salary = 0.0 ```float``` - decimal point \
smoker = False ```boolean``` - only True or False

__See types__
```type(name)``` \
```type(age)``` \
```type(salary)``` \
```type(smoker)``` \


# Type Casting
__Change from one type to another__ \
```age = input("Enter your age")``` \
```age#string``` - converts int to string \
```int(age)``` - back to int \

__Examples__ \
```q = 878``` \
```str(q)``` \
```int(98.44)``` - will output 98 as a whole number \
```float(789789)``` - will output 789789.0 \
```float("67)``` - will output 67.0 \

__Boolean__ \
__Int__ \
```bool(589)``` - True \
```bool(-32423)``` - True \
```bool(0)``` - False. Python sees it as nothing \
```bool(0.00)``` - False. Python sees it as nothing \
```bool("")``` - False. Python sees it as nothing. Empty string \
```bool(" ")``` - True. It has a space in the string. \

# Operators
__Common__ \
```+ - / *```

__% Modulus__ \
Used to get gt the remainder \
```10%3``` - 10 / 3. Remainder =1 \

__Floor Division__ \
Floor is always down \
```10//3``` - Will give you 3, not 3.33333333 

__Exponential__ \
```2**5``` - Gives you 32. 2 to the power of 5 

__Importance__ \
B - Brackets \
O - Order \
D - Division \
M - Multiplication \
A - Add \
S - Subtraction \
<br/>

See https://docs.python.org/3/library/operator.html \
<table class="docutils align-default">
<thead>
<tr class="row-odd"><th class="head"><p>Operation</p></th>
<th class="head"><p>Syntax</p></th>
<th class="head"><p>Function</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Addition</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">+</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">add(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Concatenation</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">seq1</span> <span class="pre">+</span> <span class="pre">seq2</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">concat(seq1,</span> <span class="pre">seq2)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Containment Test</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">obj</span> <span class="pre">in</span> <span class="pre">seq</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">contains(seq,</span> <span class="pre">obj)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Division</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">/</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">truediv(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Division</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">//</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">floordiv(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Bitwise And</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">&amp;</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">and_(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Bitwise Exclusive Or</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">^</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">xor(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Bitwise Inversion</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">~</span> <span class="pre">a</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">invert(a)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Bitwise Or</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">|</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">or_(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Exponentiation</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">**</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">pow(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Identity</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">is</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">is_(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Identity</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">is</span> <span class="pre">not</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">is_not(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Indexed Assignment</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">obj[k]</span> <span class="pre">=</span> <span class="pre">v</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">setitem(obj,</span> <span class="pre">k,</span> <span class="pre">v)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Indexed Deletion</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">del</span> <span class="pre">obj[k]</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">delitem(obj,</span> <span class="pre">k)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Indexing</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">obj[k]</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">getitem(obj,</span> <span class="pre">k)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Left Shift</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">&lt;&lt;</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">lshift(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Modulo</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">%</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">mod(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Multiplication</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">*</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">mul(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Matrix Multiplication</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">@</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">matmul(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Negation (Arithmetic)</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">-</span> <span class="pre">a</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">neg(a)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Negation (Logical)</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">not</span> <span class="pre">a</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">not_(a)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Positive</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">+</span> <span class="pre">a</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">pos(a)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Right Shift</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">&gt;&gt;</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rshift(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Slice Assignment</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">seq[i:j]</span> <span class="pre">=</span> <span class="pre">values</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">setitem(seq,</span> <span class="pre">slice(i,</span> <span class="pre">j),</span> <span class="pre">values)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Slice Deletion</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">del</span> <span class="pre">seq[i:j]</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">delitem(seq,</span> <span class="pre">slice(i,</span> <span class="pre">j))</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Slicing</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">seq[i:j]</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">getitem(seq,</span> <span class="pre">slice(i,</span> <span class="pre">j))</span></code></p></td>
</tr>
<tr class="row-even"><td><p>String Formatting</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">s</span> <span class="pre">%</span> <span class="pre">obj</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">mod(s,</span> <span class="pre">obj)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Subtraction</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">-</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">sub(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Truth Test</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">obj</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">truth(obj)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Ordering</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">&lt;</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">lt(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Ordering</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">&lt;=</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">le(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Equality</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">==</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">eq(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Difference</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">!=</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">ne(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Ordering</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">&gt;=</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">ge(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Ordering</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">a</span> <span class="pre">&gt;</span> <span class="pre">b</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">gt(a,</span> <span class="pre">b)</span></code></p></td>
</tr>
</tbody>
</table>

# Data Structures
A way to store, organize and retrive data \
A list starts with 0 as the first position \
You can have a list in a list

__List__ 
 - Inside ```[ 'square' ]``` 
 - Can have duplicates 
 - Any data type 
 - Ordered (Indexed)
 - Can change the data 

***Examples*** \
```a = [ 'Apple', 'Orange', 'Pear', 'Banana']``` \
```a & tab``` - Will give you all the available functions \
```help(list.append)``` - Help command to see what he function does \
```a.append('Plum')``` - Will add one item \
```a.extend([ 'Lemon', 'Grape ])``` - Will add more than one item to a list \
```a.remove('Plum')``` - Removes the first occurance of a value \
```a.insert(2, 'Grapefruit')``` - Insert the value in the position you want it. E.g. third is 2. \
```a.pop(2)``` - Remove and return item at index. (Default is last) \

__Tuples__
Read only nature after created \

- Inside ```('round')```
- Can have duplicates
- Any data type
- Ordered (Indexed)
- Cannot be changed

# Packing and Unpacking
Multiple values \
```a, b, c = 10, 20, 30``` - Will give you ```(10, 20, 30)``` \
a = 10 \
b = 20 \
c = 30 \
Python default list is Tuple \

# Sets 
- Inside {}
- No duplicates
- Not ordered. Cannot index it

***Examples*** \
```a = {}'black', 'blue', 'green', 'red'}``` \
```voda = {'gaju', 'aju', 'maju', 'ajinder', 'kimal}``` \
```JIO = {'gaju', 'aman', 'harman', 'ajindar'}``` \
```voda.intersection(JIO)``` - Result = ```{'ajinder', 'gaju'}``` they are in both sets \
```voda.difference(JIO)``` - Will give the items that are only in vode \

# Dictionary
- In ```{ 'Dictionary'}``` \
- ```{key: value}``` \
- Mutable \
- Ordered \
- Can add

***Examples*** \
```d = {}``` - Default is dict \
```d = {'Hindi':1}``` - Str is key, value is int \
```d = { 1: 'Hindi'}``` - Int is key, value is str \
```d = { 78.9: True}``` - Float is key, value is boolean \
```d = { True: 89.3}``` - Boolean is key, value is ffloat \

# Control Structures
You give Python control \

***Examples*** 
```
age = 19 
if age >= 18: 
  print('Vote') 
  # What ever is written in the indentation will be executed
else: 
  print('You cannot vote')  
```
```
marks = 67
if marks >= 75: 
  print('Excellent') 
if marks >= 50: 
  print('Good') 
if marks >= 35: 
  print('Average') 
else: 
  print('Not a good fit')  
```

# For Loop
Repeat anything we use \


***Examples***
```
for i in range(100):
  print('Dancing)
```
This will print Dancing 100 times \

# Questions
## Write a Python program to search a given number from a list

```
value_tobe_found = 34
l1 = [3, 5, 723, 2, 34, 234, 346, 345]
for counter, i in enumerate(l1):
  if value_tobe_found == i:
  print('Found: ', counter)
  break
else:
  print('Not found')
```
This will print ```Found: 4```. It counts how many times 34 appears in the list \

## Create a new list from two lists using the following ccondition.
__Given two lists of numbers, write a Python program to create a new list so that the new list should contain odd numbers from the first list and even numbers from the second list.__
```
l1 = [2345, 2345, 2345, 2345, 234, 234, 23, 46, 56, 75678, 45]
l2 = [5, 6745, 345, 3456, 345, 8, 67, 34, 34, 2345, 2345, 4567, 5]
l3 = []

for i in l1:
  if i%2! = 0 # odd numbers
   l3.append(i)
for i in l2:
  if i% == 0: # even numbers
  l3.append(i)
print(l3)
```
This will print ```[2345, 2345, 2345, 2345, 23, 45, 3456, 8, 34]```

## Write a program to print all the unique combinations of two digits from 1 to 4 for e.g. (1, 2), (2, 3)...
```
for i in range(1, 5):
  for j in range(1, 5):
  print(i, j)
```
This wil print all the possible combinations. But will e.g. have 1 1, 2 2 in it \
```
for i in range(1, 5):
  for j in range(1, 5):
  if i != j
   print(i, j)
```
This wil print all the possible combinations. But will not have e.g. 1 1, 2 2 in it. But will have 1 2, 21, etc. \
```
for i in range(1, 5):
  for j in range(i +1, 5):
  if i != j
   print(i, j)
```
This wil print all the possible unique combinations. 