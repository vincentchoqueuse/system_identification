all: json git


json:
	cd local; python main.py

git:
	git add .
	git commit -m "last"
	git push -u origin master