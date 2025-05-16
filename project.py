"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """

    # First check the lengths of the two inputs and determine the length of the shorter line.
    shorter_length = min(len(line1), len(line2))

    # Look for differences in the lines up to the last character in the shorter line.  
    index = 0
    for character in line1[0: shorter_length]:
        if character != line2[index]:
            return index
        index += 1

    # There are the two possible cases when no differences are found above: 
    # (1) the lines are the same length and (2) the lines are different lengths.
    
    if len(line1) == len(line2):
        return IDENTICAL
    else:
        return index

# # Simple test for singleline_diff(line1, line2)                                 
# string1 = "nowadays"
# string2 = "nowaday"
# print(singleline_diff(string1, string2))


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    shorter_length = min(len(line1), len(line2))
    
    if (line1.find("\n") != -1) or (line1.find("\r") != -1) or (line2.find("\n") != -1) or (line2.find("\r") != -1):
        return ""
    elif (idx < 0) or (idx > shorter_length):
        return ""
    else:
        separator_line = "=" * idx + "^"
        return line1 + "\n" + separator_line + "\n" + line2 + "\n"

# # Simple test for singleline_diff_format(line1, line2, idx)    
# string1 = "nowaday"
# string2 = "nopaday"
# index = 0
# print(singleline_diff_format(string1, string2, index))


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    # First check the lengths of the two lists and determine the length of the shorter lists. 
    shorter_list = min(len(lines1), len(lines2)) 
        
    list_index = 0
    for line in lines1[0 : shorter_list]:
        diff_index = singleline_diff(line, lines2[list_index])
        if diff_index != IDENTICAL:
            return (list_index, diff_index)
        list_index += 1
    
    if len(lines1) == len(lines2):
        return (IDENTICAL, IDENTICAL)
    else:
        return(shorter_list, 0)

# # Simple test for multiline_diff(lines1, lines2)  
# list1 = ["aaa", "bbb", "ccc"]
# list2 = ["aaa", "bbb", "ccc"]
# print(multiline_diff(list1, list2))


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    with open(filename, "rt") as lines_file:
        lines = lines_file.read()
        lines = lines.rstrip("\n")
        lines_list = lines.split("\n")
            
    return lines_list

# # Simple test for get_file_lines(filename)
# print(get_file_lines("file2.txt")) 


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)

    (list_index, diff_index) = multiline_diff(lines1, lines2)

    if (list_index, diff_index) == (IDENTICAL, IDENTICAL):
        return "No differences\n"
    else:
        return "Line " + str(list_index) + ":" "\n" + singleline_diff_format(lines1[list_index], lines2[list_index], diff_index)

# # Simple test for file_diff_format(filename1, filename2)
print(file_diff_format("file9.txt", "file10.txt"))