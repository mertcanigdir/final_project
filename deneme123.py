import easyocr

reader = easyocr.Reader(['en','ch_tra'])


results = reader.readtext('test.jpg')

text = ''

for result in results:
    text += result[1] + ''


print(text)


