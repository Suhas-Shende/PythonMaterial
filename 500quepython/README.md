### Table of content
<!-- TOC_START -->
| No. | Questions |
| --- | --------- |
| 1 | [What is Python?](#what-is-python) |
| 2 | [Why is Python so popular?](#why-is-python-so-popular) |
| 3 | [How to install Python?](#how-to-install-python) |
| 4 | [What are the applications of Python?](#what-are-the-applications-of-python) |
| 5 | [What are the advantages of Python?](#what-are-the-advantages-of-python) |
| 6 | [What are the limitations of Python?](#what-are-the-limitations-of-python) |
| 7 | [What are literals in Python?](#what-are-literals-in-python) |
| 8 | [What is PEP 8, and why is it important?](#what-is-pep-8-and-why-is-it-important) |
| 9 | [What is an interpreted language?](#what-is-an-interpreted-language) |
| 10 | [What is the difference between a compiled and an interpreted language?](#what-is-the-difference-between-a-compiled-and-an-interpreted-language) |
| 11 | [How to check the Python version on your system?](#how-to-check-the-python-version-on-your-system) |
| 12 | [What are keywords in Python?](#what-are-keywords-in-python) |
| 13 | [What is indentation, and why is it important in Python?](#what-is-indentation-and-why-is-it-important-in-python) |
| 14 | [What is the difference between == and = in Python?](#what-is-the-difference-between-==-and-=-in-python) |
| 15 | [How can you print without a newline in Python?](#how-can-you-print-without-a-newline-in-python) |
| 16 | [What are variables in Python?](#what-are-variables-in-python) |
| 17 | [What is dynamic typing in Python?](#what-is-dynamic-typing-in-python) |
| 18 | [What are built-in data types in Python?](#what-are-built-in-data-types-in-python) |
| 19 | [What is type casting in Python?](#what-is-type-casting-in-python) |
| 20 | [What are global and local variables?](#what-are-global-and-local-variables) |
| 21 | [What is the difference between a list and a tuple?](#what-is-the-difference-between-a-list-and-a-tuple) |
| 22 | [How do you create a tuple with one element?](#how-do-you-create-a-tuple-with-one-element) |
| 23 | [What is tuple unpacking?](#what-is-tuple-unpacking) |
| 24 | [How do you concatenate two lists in Python?](#how-do-you-concatenate-two-lists-in-python) |
| 25 | [What is a dictionary in Python?](#what-is-a-dictionary-in-python) |
| 26 | [How do you access elements in a dictionary?](#how-do-you-access-elements-in-a-dictionary) |
| 27 | [What is the difference between pop() and remove() in lists?](#what-is-the-difference-between-pop-and-remove-in-lists) |
| 28 | [What is the difference between append() and extend() in lists?](#what-is-the-difference-between-append-and-extend-in-lists) |
| 29 | [What is a set in Python?](#what-is-a-set-in-python) |
| 30 | [What is the difference between a set and a frozenset?](#what-is-the-difference-between-a-set-and-a-frozenset) |
| 31 | [What is a string in Python?](#what-is-a-string-in-python) |
| 32 | [How do you reverse a string in Python?](#how-do-you-reverse-a-string-in-python) |
| 33 | [What is string interpolation?](#what-is-string-interpolation) |
| 34 | [What is an f-string?](#what-is-an-f-string) |
| 35 | [How can you split a string into a list?](#how-can-you-split-a-string-into-a-list) |
| 36 | [How do you check if a string contains a substring?](#how-do-you-check-if-a-string-contains-a-substring) |
| 37 | [How do you replace a substring in a string?](#how-do-you-replace-a-substring-in-a-string) |
| 38 | [What is string slicing?](#what-is-string-slicing) |
| 39 | [What are negative indices in Python?](#what-are-negative-indices-in-python) |
| 40 | [What is the difference between str() and repr()?](#what-is-the-difference-between-str-and-repr) |
| 41 | [What are list comprehensions?](#what-are-list-comprehensions) |
| 42 | [What is the difference between list comprehension and a loop?](#what-is-the-difference-between-list-comprehension-and-a-loop) |
| 43 | [What are generators in Python?](#what-are-generators-in-python) |
| 44 | [What is the yield keyword?](#what-is-the-yield-keyword) |
| 45 | [What is a lambda function?](#what-is-a-lambda-function) |
| 46 | [What is the difference between map() and filter()?](#what-is-the-difference-between-map-and-filter) |
| 47 | [What is the difference between map() and list comprehension?](#what-is-the-difference-between-map-and-list-comprehension) |
| 48 | [What is the use of the zip() function?](#what-is-the-use-of-the-zip-function) |
| 49 | [What is a function in Python?](#what-is-a-function-in-python) |
| 50 | [How do you define a function in Python?](#how-do-you-define-a-function-in-python) |

| 51 | [What is a docstring?](#what-is-a-docstring) |
| 52 | [What is the difference between a function and a method?](#what-is-the-difference-between-a-function-and-a-method) |
| 53 | [What are default arguments?](#what-are-default-arguments) |
| 54 | [What are positional arguments?](#what-are-positional-arguments) |
| 55 | [What are keyword arguments?](#what-are-keyword-arguments) |
| 56 | [What are *args and **kwargs?](#what-are-args-and-kwargs) |
| 57 | [What is recursion in Python?](#what-is-recursion-in-python) |
| 58 | [What is the base case in recursion?](#what-is-the-base-case-in-recursion) |
| 59 | [How to avoid infinite recursion?](#how-to-avoid-infinite-recursion) |
| 60 | [What is a module in Python?](#what-is-a-module-in-python) |
| 61 | [How do you import a module?](#how-do-you-import-a-module) |
| 62 | [What is the difference between import and from import?](#what-is-the-difference-between-import-and-from-import) |
| 63 | [What is the __name__ variable?](#what-is-the-__name__-variable) |
| 64 | [What is the purpose of if __name__ == '__main__':?](#what-is-the-purpose-of-if-__name__--main) |
| 65 | [What are packages in Python?](#what-are-packages-in-python) |
| 66 | [What is the purpose of the __init__.py file?](#what-is-the-purpose-of-the-__init__.py-file) |
| 67 | [How do you install external packages using pip?](#how-do-you-install-external-packages-using-pip) |
| 68 | [What is file handling in Python?](#what-is-file-handling-in-python) |
| 69 | [How do you open a file in Python?](#how-do-you-open-a-file-in-python) |
| 70 | [What are the different file modes in Python?](#what-are-the-different-file-modes-in-python) |
| 71 | [How do you read from a file?](#how-do-you-read-from-a-file) |
| 72 | [How do you write to a file?](#how-do-you-write-to-a-file) |
| 73 | [How do you close a file?](#how-do-you-close-a-file) |
| 74 | [What is the with statement in file handling?](#what-is-the-with-statement-in-file-handling) |
| 75 | [What is exception handling?](#what-is-exception-handling) |
| 76 | [What are try, except, else, and finally blocks?](#what-are-try-except-else-and-finally-blocks) |
| 77 | [What is the difference between syntax errors and exceptions?](#what-is-the-difference-between-syntax-errors-and-exceptions) |
| 78 | [How do you raise an exception?](#how-do-you-raise-an-exception) |
| 79 | [What is the assert statement in Python?](#what-is-the-assert-statement-in-python) |
| 80 | [What is the purpose of the raise keyword?](#what-is-the-purpose-of-the-raise-keyword) |
| 81 | [What are built-in exceptions in Python?](#what-are-built-in-exceptions-in-python) |
| 82 | [How can you create a custom exception?](#how-can-you-create-a-custom-exception) |
| 83 | [What is a class in Python?](#what-is-a-class-in-python) |
| 84 | [What is an object in Python?](#what-is-an-object-in-python) |
| 85 | [How do you create a class?](#how-do-you-create-a-class) |
| 86 | [What is the __init__ method?](#what-is-the-__init__-method) |
| 87 | [What is self in Python?](#what-is-self-in-python) |
| 88 | [What are class variables and instance variables?](#what-are-class-variables-and-instance-variables) |
| 89 | [What is inheritance in Python?](#what-is-inheritance-in-python) |
| 90 | [What is single inheritance?](#what-is-single-inheritance) |
| 91 | [What is multiple inheritance?](#what-is-multiple-inheritance) |
| 92 | [What is multi-level inheritance?](#what-is-multi-level-inheritance) |
| 93 | [What is hybrid inheritance?](#what-is-hybrid-inheritance) |
| 94 | [What is polymorphism?](#what-is-polymorphism) |
| 95 | [What is method overloading?](#what-is-method-overloading) |
| 96 | [What is method overriding?](#what-is-method-overriding) |
| 97 | [What is encapsulation?](#what-is-encapsulation) |
| 98 | [What is abstraction?](#what-is-abstraction) |
| 99 | [What are access modifiers in Python?](#what-are-access-modifiers-in-python) |
| 100 | [What is the difference between public, protected, and private members?](#what-is-the-difference-between-public-protected-and-private-members) |


### 🚀 Intermediate Level Questions (101 - 250)
| No. | Questions |
| --- | --------- |
| 101 | [What is the importance of indentation in Python?](#what-is-the-importance-of-indentation-in-python) |
| 102 | [What are loops in Python?](#what-are-loops-in-python) |
| 103 | [What is the difference between for loop and while loop?](#what-is-the-difference-between-for-loop-and-while-loop) |
| 104 | [What is an infinite loop? How can you break out of it?](#what-is-an-infinite-loop-how-can-you-break-out-of-it) |
| 105 | [What is the role of the range() function in a for loop?](#what-is-the-role-of-the-range-function-in-a-for-loop) |
| 106 | [What are nested loops in Python?](#what-are-nested-loops-in-python) |
| 107 | [How can you use an else clause with loops?](#how-can-you-use-an-else-clause-with-loops) |
| 108 | [What are break, continue, and pass statements in Python?](#what-are-break-continue-and-pass-statements-in-python) |
| 109 | [What is the difference between break and continue?](#what-is-the-difference-between-break-and-continue) |
| 110 | [What is a list comprehension?](#what-is-a-list-comprehension) |
| 111 | [What is a dictionary comprehension?](#what-is-a-dictionary-comprehension) |
| 112 | [What are nested list comprehensions?](#what-are-nested-list-comprehensions) |
| 113 | [What is a lambda function?](#what-is-a-lambda-function) |
| 114 | [What are anonymous functions in Python?](#what-are-anonymous-functions-in-python) |
| 115 | [What is the difference between a lambda function and a normal function?](#what-is-the-difference-between-a-lambda-function-and-a-normal-function) |
| 116 | [What are higher-order functions in Python?](#what-are-higher-order-functions-in-python) |
| 117 | [What is the use of the map() function?](#what-is-the-use-of-the-map-function) |
| 118 | [What is the use of the filter() function?](#what-is-the-use-of-the-filter-function) |
| 119 | [What is the use of the reduce() function?](#what-is-the-use-of-the-reduce-function) |
| 120 | [What are decorators in Python?](#what-are-decorators-in-python) |
| 121 | [What is a function decorator?](#what-is-a-function-decorator) |
| 122 | [What is a class decorator?](#what-is-a-class-decorator) |
| 123 | [What is the purpose of the @property decorator?](#what-is-the-purpose-of-the-property-decorator) |
| 124 | [What is the use of the @staticmethod decorator?](#what-is-the-use-of-the-staticmethod-decorator) |
| 125 | [What is the use of the @classmethod decorator?](#what-is-the-use-of-the-classmethod-decorator) |
| 126 | [What are generators and how do they work?](#what-are-generators-and-how-do-they-work) |
| 127 | [What is the difference between a generator and an iterator?](#what-is-the-difference-between-a-generator-and-an-iterator) |
| 128 | [What is the use of the yield keyword?](#what-is-the-use-of-the-yield-keyword) |
| 129 | [What are coroutines in Python?](#what-are-coroutines-in-python) |
| 130 | [What is asynchronous programming?](#what-is-asynchronous-programming) |
| 131 | [What is the async and await syntax in Python?](#what-is-the-async-and-await-syntax-in-python) |
| 132 | [What is the asyncio library in Python?](#what-is-the-asyncio-library-in-python) |
| 133 | [What is a thread in Python?](#what-is-a-thread-in-python) |
| 134 | [What is multithreading in Python?](#what-is-multithreading-in-python) |
| 135 | [What is the Global Interpreter Lock (GIL)?](#what-is-the-global-interpreter-lock-gil) |





### 🚀 Intermediate Level Questions (136 - 250)
| No. | Questions |
| --- | --------- |
| 136 | [How do you create a thread using the threading module?](#how-do-you-create-a-thread-using-the-threading-module) |
| 137 | [What is the difference between threading and multiprocessing?](#what-is-the-difference-between-threading-and-multiprocessing) |
| 138 | [What is a process in Python?](#what-is-a-process-in-python) |
| 139 | [What is the use of the multiprocessing module?](#what-is-the-use-of-the-multiprocessing-module) |
| 140 | [How do you communicate between processes using a queue?](#how-do-you-communicate-between-processes-using-a-queue) |
| 141 | [What is the difference between a thread and a process?](#what-is-the-difference-between-a-thread-and-a-process) |
| 142 | [What are daemonic threads?](#what-are-daemonic-threads) |
| 143 | [What is the difference between synchronous and asynchronous programming?](#what-is-the-difference-between-synchronous-and-asynchronous-programming) |
| 144 | [What are futures and tasks in asyncio?](#what-are-futures-and-tasks-in-asyncio) |
| 145 | [What is the purpose of an event loop in asyncio?](#what-is-the-purpose-of-an-event-loop-in-asyncio) |
| 146 | [What is context switching in multithreading?](#what-is-context-switching-in-multithreading) |
| 147 | [What is context management in Python?](#what-is-context-management-in-python) |
| 148 | [What are context managers and how are they implemented?](#what-are-context-managers-and-how-are-they-implemented) |
| 149 | [What is the purpose of the with statement?](#what-is-the-purpose-of-the-with-statement) |
| 150 | [What are data classes in Python?](#what-are-data-classes-in-python) |
| 151 | [How do you create a data class?](#how-do-you-create-a-data-class) |
| 152 | [What are frozen data classes?](#what-are-frozen-data-classes) |
| 153 | [What is immutability in data classes?](#what-is-immutability-in-data-classes) |
| 154 | [What is the purpose of the slots attribute?](#what-is-the-purpose-of-the-slots-attribute) |
| 155 | [What are namedtuples in Python?](#what-are-namedtuples-in-python) |
| 156 | [How do you create a namedtuple?](#how-do-you-create-a-namedtuple) |
| 157 | [What are frozen sets?](#what-are-frozen-sets) |
| 158 | [What is the difference between set and frozenset?](#what-is-the-difference-between-set-and-frozenset) |
| 159 | [What are heap queues in Python?](#what-are-heap-queues-in-python) |
| 160 | [How do you use the heapq module?](#how-do-you-use-the-heapq-module) |
| 161 | [What are priority queues?](#what-are-priority-queues) |
| 162 | [What is the purpose of the bisect module?](#what-is-the-purpose-of-the-bisect-module) |
| 163 | [What is the use of the collections module?](#what-is-the-use-of-the-collections-module) |
| 164 | [What are Counters in Python?](#what-are-counters-in-python) |
| 165 | [What is the use of the deque data structure?](#what-is-the-use-of-the-deque-data-structure) |
| 166 | [What are ordered dictionaries?](#what-are-ordered-dictionaries) |
| 167 | [What is the difference between OrderedDict and dict?](#what-is-the-difference-between-ordereddict-and-dict) |
| 168 | [What are default dictionaries?](#what-are-default-dictionaries) |
| 169 | [What is the purpose of the ChainMap?](#what-is-the-purpose-of-the-chainmap) |
| 170 | [What are weak references in Python?](#what-are-weak-references-in-python) |
| 171 | [What is the weakref module?](#what-is-the-weakref-module) |
| 172 | [What is garbage collection in Python?](#what-is-garbage-collection-in-python) |
| 173 | [How does automatic garbage collection work in Python?](#how-does-automatic-garbage-collection-work-in-python) |
| 174 | [What is reference counting?](#what-is-reference-counting) |
| 175 | [What are circular references and how are they handled?](#what-are-circular-references-and-how-are-they-handled) |
| 176 | [What is memory management in Python?](#what-is-memory-management-in-python) |
| 177 | [What is the difference between deep copy and shallow copy?](#what-is-the-difference-between-deep-copy-and-shallow-copy) |
| 178 | [What is the copy module?](#what-is-the-copy-module) |
| 179 | [What are memory leaks and how do you detect them?](#what-are-memory-leaks-and-how-do-you-detect-them) |
| 180 | [What is the tracemalloc module?](#what-is-the-tracemalloc-module) |
| 181 | [How do you profile memory usage in Python?](#how-do-you-profile-memory-usage-in-python) |
| 182 | [What are serialization and deserialization?](#what-are-serialization-and-deserialization) |
| 183 | [What is the pickle module?](#what-is-the-pickle-module) |
| 184 | [What is JSON serialization?](#what-is-json-serialization) |
| 185 | [How do you parse a JSON string?](#how-do-you-parse-a-json-string) |

| 186 | [What is the difference between JSON and pickle?](#what-is-the-difference-between-json-and-pickle) |
| 187 | [What are CSV files and how do you read them?](#what-are-csv-files-and-how-do-you-read-them) |
| 188 | [What is the csv module?](#what-is-the-csv-module) |
| 189 | [How do you write to a CSV file?](#how-do-you-write-to-a-csv-file) |
| 190 | [What is XML parsing in Python?](#what-is-xml-parsing-in-python) |
| 191 | [What is the ElementTree library?](#what-is-the-elementtree-library) |
| 192 | [How do you parse HTML using BeautifulSoup?](#how-do-you-parse-html-using-beautifulsoup) |
| 193 | [What is web scraping and how is it done?](#what-is-web-scraping-and-how-is-it-done) |
| 194 | [What are APIs and how do you interact with them using requests?](#what-are-apis-and-how-do-you-interact-with-them-using-requests) |
| 195 | [What is RESTful API in Python?](#what-is-restful-api-in-python) |
| 196 | [What is an HTTP request?](#what-is-an-http-request) |
| 197 | [What is the difference between GET and POST requests?](#what-is-the-difference-between-get-and-post-requests) |
| 198 | [What are cookies and sessions in Python?](#what-are-cookies-and-sessions-in-python) |
| 199 | [What is the purpose of the requests module?](#what-is-the-purpose-of-the-requests-module) |
| 200 | [What is the difference between requests and urllib?](#what-is-the-difference-between-requests-and-urllib) |
| 201 | [What is the purpose of the urllib library?](#what-is-the-purpose-of-the-urllib-library) |
| 202 | [How do you download files using Python?](#how-do-you-download-files-using-python) |
| 203 | [What are logging and debugging in Python?](#what-are-logging-and-debugging-in-python) |
| 204 | [What is the logging module and how do you use it?](#what-is-the-logging-module-and-how-do-you-use-it) |
| 205 | [What are log levels and how do you set them?](#what-are-log-levels-and-how-do-you-set-them) |
| 206 | [What are log handlers and formatters?](#what-are-log-handlers-and-formatters) |
| 207 | [How do you write logs to a file?](#how-do-you-write-logs-to-a-file) |
| 208 | [What is the difference between print() and logging?](#what-is-the-difference-between-print-and-logging) |
| 209 | [What is unit testing in Python?](#what-is-unit-testing-in-python) |
| 210 | [What is the unittest framework?](#what-is-the-unittest-framework) |
| 211 | [How do you write a unit test in Python?](#how-do-you-write-a-unit-test-in-python) |
| 212 | [What are test cases and test suites?](#what-are-test-cases-and-test-suites) |
| 213 | [What is the difference between unittest and pytest?](#what-is-the-difference-between-unittest-and-pytest) |
| 214 | [What are fixtures in pytest?](#what-are-fixtures-in-pytest) |
| 215 | [What is test-driven development (TDD)?](#what-is-test-driven-development-tdd) |
| 216 | [What is behavior-driven development (BDD)?](#what-is-behavior-driven-development-bdd) |
| 217 | [What are mocks and stubs in testing?](#what-are-mocks-and-stubs-in-testing) |
| 218 | [What is mocking in Python?](#what-is-mocking-in-python) |
| 219 | [How do you use mock objects?](#how-do-you-use-mock-objects) |
| 220 | [What is the purpose of the patch() function?](#what-is-the-purpose-of-the-patch-function) |
| 221 | [What is performance profiling?](#what-is-performance-profiling) |
| 222 | [What is the timeit module?](#what-is-the-timeit-module) |
| 223 | [How do you measure the execution time of a code snippet?](#how-do-you-measure-the-execution-time-of-a-code-snippet) |
| 224 | [What is the cProfile module?](#what-is-the-cprofile-module) |
| 225 | [What are profilers and how do you use them?](#what-are-profilers-and-how-do-you-use-them) |
| 226 | [What is code optimization?](#what-is-code-optimization) |
| 227 | [What is linting and how does it help?](#what-is-linting-and-how-does-it-help) |
| 228 | [What are linters like pylint and flake8?](#what-are-linters-like-pylint-and-flake8) |
| 229 | [What is the black formatter?](#what-is-the-black-formatter) |
| 230 | [How do you format code using autopep8?](#how-do-you-format-code-using-autopep8) |
| 231 | [What is code coverage and why is it important?](#what-is-code-coverage-and-why-is-it-important) |
| 232 | [What is the difference between black and autopep8?](#what-is-the-difference-between-black-and-autopep8) |
| 233 | [How do you write a Python script to automate tasks?](#how-do-you-write-a-python-script-to-automate-tasks) |
| 234 | [What are command-line arguments?](#what-are-command-line-arguments) |
| 235 | [How do you use argparse for argument parsing?](#how-do-you-use-argparse-for-argument-parsing) |
| 236 | [What is the getopt module?](#what-is-the-getopt-module) |
| 237 | [What are environment variables?](#what-are-environment-variables) |
| 238 | [What is the os module used for?](#what-is-the-os-module-used-for) |
| 239 | [What is the subprocess module?](#what-is-the-subprocess-module) |
| 240 | [How do you execute shell commands using subprocess?](#how-do-you-execute-shell-commands-using-subprocess) |
| 241 | [What is the difference between os.system() and subprocess.run()?](#what-is-the-difference-between-os-system-and-subprocess-run) |
| 242 | [How do you handle process termination?](#how-do-you-handle-process-termination) |
| 243 | [What is a virtual environment?](#what-is-a-virtual-environment) |
| 244 | [How do you create and activate a virtual environment?](#how-do-you-create-and-activate-a-virtual-environment) |
| 245 | [What is pip and how do you manage packages?](#what-is-pip-and-how-do-you-manage-packages) |
| 246 | [How do you create a requirements.txt file?](#how-do-you-create-a-requirements-txt-file) |
| 247 | [How do you upgrade Python packages?](#how-do-you-upgrade-python-packages) |
| 248 | [What is the pyenv tool?](#what-is-the-pyenv-tool) |
| 249 | [What is pipenv and how does it differ from pip?](#what-is-pipenv-and-how-does-it-differ-from-pip) |
| 250 | [What is poetry in Python?](#what-is-poetry-in-python) |
