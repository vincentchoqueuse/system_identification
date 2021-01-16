all: json git


json:
	cd src; python main.py

git:
	git add .
	git commit -m "last"
	git push -u origin master

dev:
	python3 -m http.server