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
		.TitleCard{
			text-align: left;
			margin-bottom: 0.3in;
		}
		.SpokenText{
			text-align: center;
			margin-bottom: 0.3in;
		}

		.Scene {
			text-align: left;
			margin-bottom: 0.3in;

			<!-- text-translate: uppercase; -->
		}
		.Role {
			text-align: center;
			margin-bottom: 0.3in;
		}
		.Text {
			text-align: left;
			margin-bottom: 0.3in;
		}
		.fade_in {
			text-align: left;
			margin-bottom: 0.3in;
		}
		.cut_to {
			text-align: right;
			margin-bottom: 0.3in;
		}
		.dissolve_to {
			text-align: right;
			margin-bottom: 0.3in;
		}
		.close_on {
			text-align: left;
			margin-bottom: 0.3in;
		}
		.pull_back {
			text-align: right;
			margin-bottom: 0.3in;
		}
		pre{
		margin: unset;
		margin-bottom: 0.3in;
		font-family: courier;
		}

  </style>

</head>

<body>
"""

Html_file= open("scriptTest.html","w")
Html_file.write(htmlBeginning)
rightClasses = ['cut_to','dissolve_to']
divTitleCardNonSpoken = '<div class="TitleCard">Title card (Clip %s): %s</div>'+'\n'
divTitleCardSpoken = '<div><pre>Title card (Clip %s):		%s</pre></div>'+'\n'
divSpokenText = '<div class="SpokenText">%s</div>'+'\n'
divEditCamera = '<div class="%s">%s (Clip %s):</div>'+'\n'
divScene = '<div class="Scene">%s</div>\n'
divText = '<div class="Text">%s</div>\n'
divRole = '<div class="Role">%s</div>\n'
divAllin = '<div class="Text">%s (Clip %s): %s</div>\n'
with open('test.csv', mode='r') as csv_file:
	firstline = True
	csv_reader = csv.reader(csv_file)
	for row in csv_reader:
		if firstline:
			firstline = False
			continue
		info = list(row)
		clipNo = info[3]
		isItTitle = info[4]
		editCamera = info[5]
		scene = info[6]
		role = info[7]
		text = info[8]
		#first check if it is a title
		if isItTitle.lower()=="title":
			#check if it is not a spoken title
			if role in (None, ""):
				Html_file.write((divTitleCardNonSpoken %(clipNo,text)))
			else:
				if text[0]!='"':
					text = '"'+text
				if text[len(text)-1]!='"':
					text = text+'"'
				Html_file.write((divTitleCardSpoken %(clipNo,role.upper())))
				Html_file.write((divSpokenText %(text)))
		#if it is not title we check if there is a non default camera/edit instructions
		else:
			#if the edit/camera column empty, we assume it is CUT TO
			if clipNo:
				if editCamera in (None, ""):
					editCamera = "CUT TO"
				editCameraClass = editCamera.replace(" ","_").lower()
				if editCameraClass in rightClasses:
					Html_file.write((divEditCamera %(editCameraClass, editCamera.upper(), clipNo)))
					if scene not in (None, ""):
						Html_file.write(divScene %(scene.upper()))
					if role in (None,""):
						Html_file.write(divText %(text))
					else:
						if text[0]!='"':
							text = '"'+text
						if text[len(text)-1]!='"':
							text = text+'"'
						Html_file.write((divTitleCardSpoken %(clipNo,role.upper())))
						Html_file.write((divSpokenText %(text)))
				else:
					if scene in (None, ""):
						Html_file.write((divAllin %(editCamera.upper(), clipNo, text)))
					else:
						Html_file.write((divEditCamera %(editCameraClass, editCamera.upper(), clipNo)))
						Html_file.write(divScene %(scene.upper()))
						if role in (None,""):
							Html_file.write(divText %(text))
						else:
							if text[0]!='"':
								text = '"'+text
							if text[len(text)-1]!='"':
								text = text+'"'
							Html_file.write((divTitleCardSpoken %(clipNo,role.upper())))
							Html_file.write((divSpokenText %(text)))





			else:
				if role in (None,""):
					Html_file.write(divText %(text))
				else:
					if text[0]!='"':
						text = '"'+text
					if text[len(text)-1]!='"':
						text = text+'"'
					Html_file.write((divRole %(role.upper())))
					Html_file.write((divSpokenText %(text)))

htmlEnd = """
</body>
</html>
"""
Html_file.write(htmlEnd)
Html_file.close()
