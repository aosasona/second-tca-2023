pack: # zip all files and exclude git folder and .DS_Store
	zip -r compressed.zip * -x ".git/*" -x ".DS_Store"
