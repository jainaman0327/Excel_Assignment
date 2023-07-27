#!/usr/bin/env python
# coding: utf-8

# 1. What does the dollar($) sign do?
# 
# Ans) In Excel, a dollar sign can denote a currency format, but it has another common use:
# indicating absolute cell references in formulas.
# 
# An absolute reference in Excel is a cell address with the dollar sign ($) in the row or column
# coordinates, like $A$1.
# 
# The dollar sign fixes the reference to a given cell, so that it remains unchanged no matter
# where the formula moves. In other words, using $ in cell references allows you to copy the
# formula in Excel without changing references. 
# 

# 2. How to Change the Reference from Relative to Absolute (or Mixed)?
# 
# Ans) To change the reference from relative to absolute, we need to add the dollar sign
# before the column notation and the row number. For example, A1 is a relative cell
# reference, and it would become absolute when we make it $A$1.
# 
# Short-cut Key: When we select a cell reference (in the formula bar or in the cell in edit
# mode) and press F4, it changes the reference.
# 
# Suppose you have the reference =A1 in a cell.
# 
# 1. Press F4 key once: The cell reference changes from A1 to $A$1 (becomes ‘absolute’
# from ‘relative’).
# 
# 2. Press F4 key two times: The cell reference changes from A1 to A$1 (changes to
# mixed reference where the row is locked).
# 
# 3. Press F4 key three times: The cell reference changes from A1 to $A1 (changes to
# mixed reference where the column is locked).
# 
# 4. Press F4 key four times: The cell reference becomes A1 again. 

# 3. Explain the order of operations in excel?
# 
# Ans) When evaluating a formula, Excel follows a standard math protocol called "order of
# operations". In general, Excel's order of operation follows the acronym PEMDAS
# (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction) but with some
# customization to handle the formula syntax in a spreadsheet.
# 
# Excel solves formulas in the following order:
# 
#  Parentheses
# 
#  Reference operators
# 
#  Exponents
# 
#  Negation
# 
#  Percent
# 
#  Multiplication and Division
# 
#  Addition and Subtraction
# 
#  Concatenation
# 
#  Logical operators
# 
# If a formula contains multiple operators with the same priority (e.g. multiplication and
# division, or addition and subtraction), Excel will evaluate the operators from left to right. 

# 4. What, according to you, are the top 5 functions in excel and write a basic syntax
# for any of two?
# 
# Ans) According to me, the top 5 functions in excel are:
# 
# a. SUMIF() function:
# 
#  The syntax of the SUMIF function is:
#  
#  =SUMIF(range,criteria, [sum_range])
#  
# b. VLOOKUP() function:
# 
#  The VLOOKUP function has the following syntax for its four arguments:
#  
#  = VLOOKUP(lookup_value,table_array,col_index_num,[range_lookup])
#  
# c. IF() function
# 
# d. COUNTIF() function
# 
# e. DATEDIF() function

# 5. When would you use the subtotal function?
# 
# Ans) The Excel SUBTOTAL function returns an aggregate calculation for supplied values.
# Despite the name, SUBTOTAL can perform a variety of calculations, including SUM,
# AVERAGE, COUNT, MAX, MIN, and others.
# 
# The SUBTOTAL function is used when we display a Total row in an Excel Table.Excel inserts
# the SUBTOTAL function automatically, and we can use a drop-down menu to switch
# behaviour and show max, min, average, etc. Excel uses SUBTOTAL for calculations in the
# Total row of an Excel Table because SUBTOTAL automatically excludes rows hidden by the
# filter controls at the top of the table. That is, as we filter rows in a table with a Total row,
# calculations automatically respect the filter.

# 6. What is the syntax of the vlookup function? Explain the terms in it?
# 
# Ans) The VLOOKUP function has the following syntax for its four arguments:
#  VLOOKUP(lookup_value,table_array,col_index_num,[range_lookup])
# 
# The first 3 are required arguments, and the last one is an optional argument:
# 
# 1. lookup_value: what it should look for, such as the product code — this can be a
# 
# value, or a cell reference.
# 
# 2. table_array: where the lookup data is located (2 or more columns) — this can be a
# 
# range reference or a range name, with 2 or more columns.
# 
# 3. col_index_num: the column that has the value you want returned, based on the
# 
# column number within the table.
# 
#  This column index number can be different from the worksheet column number
#  
# 4. [range_lookup]: for an exact match, use FALSE or 0; for an approximate match, use
# 
# TRUE or 1, with the lookup value column sorted in ascending order.
# 
#  If we omit the range_lookup argument, VLOOKUP will return an approximate match

# In[ ]:




