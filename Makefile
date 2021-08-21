install: 
	pip3 install -Ur requirements.txt
update-requirements: install
	pip3 freeze > requirements.txt
