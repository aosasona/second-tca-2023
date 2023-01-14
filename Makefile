pack: # zip all files and exclude git folder and .DS_Store
	zip -r ayodejiOsasona.zip * -x ".git/*" -x ".DS_Store" -x "create_doc.py"

worddoc:
	python3 create_doc.py
