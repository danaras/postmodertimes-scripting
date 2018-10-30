import csv

htmlBeginning = """
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>Postmodern Times Script</title>
  <meta name="description" content="Postmodern Times Script">
  <meta name="author" content="MM">

  <style>
		body {
			font-family: courier;
		}
		.titles{
			text-align: left;
			margin-left: 1in;
			margin-bottom: 0.3in;
		}
		.fade {
			text-align: left;
			margin-bottom: 0.3in;

			<!-- text-translate: uppercase; -->
		}
		.description {
			text-align: left;
			margin-bottom: 0.3in;
		}
  </style>

</head>

<body>
"""

Html_file= open("scripts.html","w")
Html_file.write(htmlBeginning)
with open('scenes.csv', mode='r') as csv_file:
	csv_reader = csv.reader(csv_file)
	for row in csv_reader:
		div = '<div class="%s">%s</div>'+'\n'
		info = list(row)
		if info[0]=='fade':
			info[1]=info[1].upper()
		print (div %(info[0],info[1]))
		Html_file.write((div %(info[0],info[1])))
htmlEnd = """
</body>
</html>
"""
Html_file.write(htmlEnd)
Html_file.close()
