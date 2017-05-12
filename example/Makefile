app: source.cpp data.cpp pastel.h
	g++ -o app source.cpp data.cpp
	rm data.cpp
	rm pastel.h
	rm pastel.py

data.cpp: pastel.h pastel.py
	python3 pastel.py -s source.cpp -t data.cpp --generate_header

pastel.h: pastel.py
	python3 pastel.py --generate_header

pastel.py:
	cp ../src/pastel.py pastel.py
