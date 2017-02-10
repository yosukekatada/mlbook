try:
    print(not_found_name)
except NameError as err:
    print(err)  # => name 'not_found_name' is not defined

print(err)  # =>
            #Traceback (most recent call last):
            #  File "path/to/tryexcept_variable_sample.py", line 6, in <module>
            #    print(err)
            #NameError: name 'err' is not defined
