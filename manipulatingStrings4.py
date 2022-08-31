name = str(input('Your name: ')).upper().strip()
print("""
First Name: {}
Last Name: {}
"""
      .format(name[:name.find(" ")], name[name.rfind(" "):]))