init:
	mkdir dataset
	wget http://web.sfc.keio.ac.jp/~t13073si/summer_homework.zip
	mv summer_homework.zip ./dataset
	unzip dataset/summer_homework.zip -d dataset/
	rm -r dataset/summer_homework.zip
