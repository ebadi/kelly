# 🇸🇪 Common Swedish Words and Conversations

This project provides tools to work with frequency-based Swedish vocabulary lists and generate example conversations using them. 
This project uses the [Swedish Kelly-list](https://spraakbanken.gu.se/en/resources/kelly), a free resource from Språkbanken (University of Gothenburg) containing modern Swedish words ordered by frequency of use.

## Features

* **Word List Generation**
  [`printable.py`](printable.py): Creates a frequency-ordered word list ready for printing. Example output: [`print.txt`](print.txt)

* **Conversation Prompt Builder**
  [`prompt.py`](prompt.py): Groups words into prompts for use with Large Language Models (LLMs) to generate example conversations. Example output: [`prompt.md`](prompt.md)


To reproduce:
```bash
git clone https://github.com/ebadi/kelly.git
cd kelly
python3 printable.py > print.txt
python3 prompt.py > prompt.md
```

## License

This project is licensed under the **LGPL-3.0** license. 
