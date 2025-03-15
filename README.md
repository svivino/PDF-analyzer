# PDF-analyzer
To rate the Sentiment Polarity and Subjectivity of a pdf
Open terminal and paste then hit enter:

pip3 --version

if you see a verson number you're okay to continue if not paste and enter:

python3 -m ensurepip --default-pip

After pip3 is confirmed installed you need to install the libraries.
Copy and paste the bellow into ur terminal and hit enter. A bunch of text will start to show.

pip3 install PyPDF2 textblob tk

Wait till its done dumping a bunch of text at you it will likley say completed a few times.
If you're not sure if it all installed you can run(tbh only like 10% sure this actully checks):

python3 -c "import PyPDF2, textblob, tkinter; print('Libraries installed successfully!')"

Now it's ready to run! the above steps shouldn't have to be done again.

There is a few diffrent ways to run it. 
If you need to send screen shots to your teacher follow way 1.
If you just want it to be as easiy as posible follow way 2.


Way 1 terminal app:
whenever I say run I mean paste that command and hit enter
Open terminal run:

cd

This will take you to the main directory. To confirm run:

ls

ls is the command to list all the files of where you are.
You'll now need to use cd to get to the file that conatins main.py
You can either do it all in one go by putting the whole path to that file ex:

cd Documents/file1/file2

or you can do it one by one ex:

cd Documents
ls
cd file1
ls
cd file2
ls

(note each ls is just to check that you're going to the right place)

At this point you should see when you run ls the program "main.py" and the pdf file you wish to check.
Next go to finder in the same path that you just did in terminal. 
In here you should see not only main.py but the pdf file you wish to check.
Open main.py and edit line 23 to have the name of the pdf.
(note if the pdf is in the same file that you are running the code from in terminal you don't need the whole path)
You can either click save or use command+s to save. Make sure you don't do save as or change the name.
Now go back to terminal and run:

python3 main.py

You will need to re-edit the code and re-run through terminal each pdf file.

Way 2 GUI app
Like in way one use terminal to go to the file that conatins app.py
whenever I say run I mean paste that command and hit enter
Open terminal run:

cd

This will take you to the main directory. To confirm run:

ls

ls is the command to list all the files of where you are.
You'll now need to use cd to get to the file that conatins app.py
You can either do it all in one go by putting the whole path to that file ex:

cd Documents/file1/file2

or you can do it one by one ex:

cd Documents
ls
cd file1
ls
cd file2
ls

(note each ls is just to check that you're going to the right place)

Once in the file that conatins app.py you can run it with:

python3 app.py

Please note it might take a second to open.
Once open you should be able to click upload pdf anf it will show you the numbers.
Please note I only tested this with like 2 pdfs and have no idea what bugs might happen.
Things to check is if the numbers seem rigth and also I've only tested it upto 2 diffrent pdfs back to back.
So make sure each file is giving diffrent numbers each time.
If you need to close the program please refer back to the ls command in the terminal.
Using ls you'll be able to see if you're in the right file as you'll see app.py listed then can run:

python3 app.py
