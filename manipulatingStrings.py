name = str(input('Type a name: '))
nameSplitJoin = name.split()
nameSplitJoin = "".join(nameSplitJoin)
firstName = name[:name.find(" ")]
print('Uppercase name: {}'.format(name.upper()))
print('Uppercase name: {}'.format(name.lower()))
print('The name size without space was: {}'.format(len(nameSplitJoin)))
print('The first name has {} letters and is {}'.format(len(firstName), firstName))