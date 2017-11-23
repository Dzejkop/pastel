app: source.cpp test.cpp data.cpp pastel.h
	g++ -o app source.cpp test.cpp data.cpp
	rm data.cpp
	rm pastel.py

# Generate the data
data.cpp: pastel.h pastel.py source.cpp test.cpp
	python3 pastel.py -s source.cpp -s test.cpp -t data.cpp --verbose

# Generate pastel.h header
pastel.h: pastel.py
	python3 pastel.py --generate_header --verbose

# Copy the pastel.py script into the directory
pastel.py:
	cp ../src/pastel.py pastel.py

clean:
	rm pastel.h
	rm app
