init:
	mkdir dataset
	wget http://web.sfc.keio.ac.jp/~t13073si/summer_homework.zip
	mv summer_homework.zip ./dataset
	unzip dataset/summer_homework.zip -d dataset/
	rm -r dataset/summer_homework.zip


all-answer:
	python chr00.py
	python chr01.py
	python chr03.py
	python chr04.py
	python chr05.py
	python chr06.py
	python chr07.py
