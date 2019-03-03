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
			font-size: 10pt;

		}
		.TitleCard{
			text-align: left;
			margin-bottom: 0.15in;
		}
		.SpokenText{
			text-align: center;
			margin-bottom: 0.15in;
		}

		.Scene {
			text-align: left;
			margin-bottom: 0.15in;

			<!-- text-translate: uppercase; -->
		}
		.Role {
			text-align: center;
			margin-bottom: 0.15in;
		}
		.Text {
			text-align: left;
			margin-bottom: 0.15in;
		}
		.fade_in {
			text-align: left;
			margin-bottom: 0.15in;
		}
		.cut_to {
			text-align: right;
			margin-bottom: 0.15in;
		}
		.dissolve_to {
			text-align: right;
			margin-bottom: 0.15in;
		}
		.close_on {
			text-align: left;
			margin-bottom: 0.15in;
		}
		.pull_back {
			text-align: right;
			margin-bottom: 0.15in;
		}
		.Out {
			text-align: right;
			margin-bottom: 0.15in;
		}
		.Reveal {
			margin-bottom: 0.15in;
		}
		pre{
		margin: unset;
		margin-bottom: 0.15in;
		font-family: courier;
		}

  </style>
</head>
<body>
"""

Html_file = open("final.html","w")
Html_file.write(htmlBeginning)
rightClasses = ['cut_to','dissolve_to']
divTitleCardNonSpoken = '<div class="TitleCard">Title card (Clip %s): %s</div>'+'\n'
divTitleCardSpoken = '<div><pre>Title card (Clip %s):			%s</pre></div>'+'\n'
divSpokenText = '<div class="SpokenText">%s</div>'+'\n'
divEditCameraIn = '<div class="%s">%s (Clip %s):</div>'+'\n'
divEditCameraOut = '<div class="Out">%s</div>\n'
divScene = '<div class="Scene">%s</div>\n'
divText = '<div class="Text">%s</div>\n'
divRole = '<div class="Role">%s</div>\n'
divAllin = '<div class="Text">%s (Clip %s): %s</div>\n'
divReveal = '<div class="Reveal">Reveal: %s</div>\n'

with open('final.csv', mode='r') as csv_file:
	firstline = True
	csv_reader = csv.reader(csv_file)
	for row in csv_reader:
		if firstline:
			firstline = False
			continue
		info = list(row)
		clipNo = info[0]
		isItTitle = info[3]
		editCameraIn = info[4]
		editCameraOut = info[6]
		scene = info[8]
		role = info[9]
		dialogue = info[10]
		text = info[11]
		#first check if it is a title
		if clipNo:
			if isItTitle.lower()=="title":
				# print info
				#check if it is not a spoken title
				if role in (None, ""):
					Html_file.write((divTitleCardNonSpoken %(clipNo,text)))
				else:
					Html_file.write((divTitleCardSpoken %(clipNo, role.upper())))

					if dialogue:
						if dialogue[0]!='"':
							dialogue = '"'+dialogue
						if dialogue[len(dialogue)-1]!='"':
							dialogue = dialogue+'"'
						Html_file.write((divSpokenText %(dialogue)))

			#if it is not title we check if there is a non default camera/edit instructions
			else:
				# print isItTitle
				#if the edit/camera column empty, we assume it is CUT TO
				if editCameraIn in (None, ""):
					editCameraIn = "CUT TO"
				editCameraInClass = editCameraIn.replace(" ","_").lower()
				if editCameraInClass in rightClasses:
					Html_file.write((divEditCameraIn %(editCameraInClass, editCameraIn.upper(), clipNo)))
					if scene not in (None, ""):
						Html_file.write(divScene %(scene.upper()))
					if role in (None,""):
						Html_file.write(divText %(text))
					else:
						Html_file.write((divRole %(role.upper())))
						if dialogue:
							if dialogue[0]!='"':
								dialogue = '"'+dialogue
							if dialogue[len(dialogue)-1]!='"':
								dialogue = dialogue+'"'
							Html_file.write((divSpokenText %(dialogue)))
				else:
					if scene in (None, ""):
						Html_file.write((divAllin %(editCameraIn.upper(), clipNo, text)))
					else:
						Html_file.write((divEditCameraIn %(editCameraInClass, editCameraIn.upper(), clipNo)))
						Html_file.write(divScene %(scene.upper()))
						if role in (None,""):
							Html_file.write(divText %(text))
						else:
							Html_file.write((divRole %(role.upper())))
							if dialogue:
								if dialogue[0]!='"':
									dialogue = '"'+dialogue
								if dialogue[len(dialogue)-1]!='"':
									dialogue = dialogue+'"'
								Html_file.write((divSpokenText %(dialogue)))

		else:
			if role:
				Html_file.write((divRole %(role.upper())))
				if dialogue:
					if dialogue[0]!='"':
						dialogue = '"'+dialogue
					if dialogue[len(dialogue)-1]!='"':
						dialogue = dialogue+'"'
					Html_file.write((divSpokenText %(dialogue)))
			else:
				if editCameraIn:
					if editCameraIn.lower() == "reveal":
						Html_file.write(divReveal %(text))
					else:
						print info
				else:
					Html_file.write(divText %(text))


		if editCameraOut not in (None,""):
			# editCameraOutClass = editCameraOut.replace(" ","_").lower()

			Html_file.write((divEditCameraOut %(editCameraOut.upper())))



htmlEnd = """
</body>
</html>
"""
Html_file.write(htmlEnd)
Html_file.close()
