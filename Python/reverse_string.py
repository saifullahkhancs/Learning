string = "my name is ali"
resulted_string = 'ym eman si ila'


full_string = ''

sub_string = ''
for i in string:
    
    if i == " ":
        full_string = full_string + sub_string
        full_string = full_string + " "
        sub_string = ''
    else:
        sub_string = i + sub_string
       

full_string = full_string + sub_string
print(full_string)


string = "my name is ali"
resulted_string = 'ali is name my'




