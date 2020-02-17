"""
STEP FIVE

As a stretch goal, let's try saving the first 10 documents as Word documents instead of printing them out to the console.

For this goal we'll be using a third-party Python package called "python-docx", which knows how to create Word
documents. You'll first have to install python-docx in PyCharm so your program can find it.

(Python has lots of helpful third party packages like this! See https://xkcd.com/353/ for Randall Munroe's excitement
at discovering the python package ecosystem.)

Steps to install python-docx:

* Go to PyCharm preferences -> Project interpreter
* Click the + under the list of currently installed packages
* Search for "python-docx"
* Click "Install Package"

(If you don't see "python-docx" in the list, you may have to un-select the "Use Conda Package Manager" button next to
the "+" button on the project interpreter screen.)

Now that you've installed python-docx, it can be used in your python scripts with a line like
"from docx import Document".

Steps to complete this stretch goal:

* Copy and paste your code from the previous step.
* Modify that code so it only loops over the first ten members, using a slice -- for testing, we don't want to deal
    with 1000 word documents!
* Go to the python-docx documentation to see an example of how to create a Word document:
    https://python-docx.readthedocs.io/
* Try adapting that example code to save your demand letters as Word documents in the "letters" subfolder.

Hint: your code can be much simpler than the example code at python-docx.readthedocs.io. You should only need these
parts, somewhere in your code:

  from docx import Document
  document = Document()
  document.add_paragraph(<something>)
  document.save('letters/' + <something>)

In the example code above, notice that we can use 'letters/' in the path provided to the save() method
  so Word documents are saved to the "letters" subfolder.
"""


