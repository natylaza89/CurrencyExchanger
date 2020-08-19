# Home Task of Currency Exchanger Console Application
In this home task, I used python in order to build a console application which communicate with rest api to get current currency and perform a conversion between 2 currencies.<br>
As part of the project's planning, I used Object Orieneted Programing, Design Patterns, Unit Test and Dependency Injection.


# How to Use
Requirements: Python must already be installed.
1. Run Application via CMD:
```
python main.py files\money.txt
```

###### output example:
![Main Application Results](https://github.com/natylaza89/CurrencyExchanger/blob/master/images/app_output.png)

2. Run Tests via CMD:
```
python -m unittest
```
###### output example:
![Unit Test Results](https://github.com/natylaza89/CurrencyExchanger/blob/master/images/test_output.png)

# How it works
1. Opens a text file.
2. Parse file's headers for base & target currency.
3. Using currency excanger API for current rate.
4. Convert each value from the text file into its target form
5. Print the output off converted values.