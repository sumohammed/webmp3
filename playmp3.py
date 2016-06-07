import webbrowser
import os

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>mp3s</title>
	<link rel="stylesheet" href="Skeleton/css/normalize.css">
	<link rel="stylesheet" href="Skeleton/css/skeleton.css">
	<link rel="stylesheet" href="playmp3.css">
	<script src="Skeleton/js/jquery.js"></script>
	<script type="text/javascript" charset="utf-8">
		$(document).on('click', "li", function(event) {
		var data = $(this).attr("data-url")
		$('audio').attr('src', data)
		});
	</script>

</head>
'''

# mp3 list
main_page_content = '''
<body>
	<div class="container">
		<div class="row">
			<div class="twelve columns audio">
				<audio src="" controls="" autoplay="">
			</div>
		</div>
		<div class="row">
			<div class="twelve columns player">
				{mp3_s}
			</div>
		</div>
	</div>
</body>
'''

mp3_name = '''
<li data-url="{song_location}">
	{song_file}
</li>
'''

def create_mp3_content(songlist):
	content = ''
	for song in songlist:
		content += mp3_name.format(
			song_file=song.name,
			song_location=song.location
			)
	return content

def open_mp3_page(songlist):
	#create or overwrite the output file 
	output_file = open('playmp3.html', 'w')

	#replace the mp3 3ntry points wit generated document
	rendered_content = main_page_content.format(
		mp3_s=create_mp3_content(songlist))
		
	#outout the file 
	output_file.write(main_page_head + rendered_content)
	output_file.close()

	#open output file in browser
	url = os.path.abspath(output_file.name)
	webbrowser.open('file://' + url, new=2)