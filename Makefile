install: 
	pip install -Ur requirements.txt
update-requirements:
	pip freeze > requirements.txt
uninstall:
	pip uninstall -r requirements.txt
clear:
	rm audio/*.wav speech/*.speech chat/*.chat
