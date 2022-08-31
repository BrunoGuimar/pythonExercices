city = str(input('Type your city name: '))
print('The city name is {}, and if she beggins with Santo in the name: {}, and if she have Santo in the name {}'
      .format(city, 'SANTO' in city[:city.find(" ")].upper(), 'SANTO' in city.upper()));