# Notes — Week 2

## Instructions

* "Data" being the plural of "datum" was really driven into my head when writing papers for COMS 2200: Big Data and Society and TSES 3002: Energy and Sustainability.

## Installing Sublime Text

* I didn't encounter any issues installing Sublime Text. As I've used it in the past, I'll probably stick to using Visual Studio Code as it's also a pretty quick text/code editor. Notwithstanding, I'm impressed by the updates to Sublime Text in recent years.

## Setting up Anaconda

### Installing `conda`

* Installing Anaconda had no issues. At this point it's hard to tell whether it's worth using for this use case rather than installing software packages individually.

### PowerShell

* I'll probably use Anaconda PowerShell or `bash` for following most of the instructions, though I'd definitely rather use macOS's Terminal, which now uses the `zsh` shell by default.
* `echo`, `conda --version`, and `python --version` worked just fine in the default base (root) environment, which had a bunch of packages already installed. Probably explains Anaconda's huge install size, but now I know Anaconda was installed properly!
 * `conda --version` outputted `conda 4.8.2`.
 * `python --version` outputted `Python 3.7.6`.

### Navigating the command line

* I already knew about `pwd`, `ls`, `dir`, and `cd`, but I made sure they worked in Anaconda Powershell since there are some shells where they don't work. Learned that from trying to make my own shell in COMP 3000: Operating Systems. Though, as aforementioned, just like how you can make any HTML element in theory, you could theoretically also make a shell that's *missing* as many features and commands as you want.

## `wget`

### Installation

* I didn't know `wget` wasn't installed by default on macOS! Or maybe Homebrew helps you get a newer version than what's pre-installed.
* I needed to provide administrator permission to put the `wget` executable in C:\Windows. Makes sense; lots of important system files there. Normally, I would also add it to the system's PATH environment variable, but this way is simpler for now.

### Basic Usage

* I'm going to make this new directory in the folder with my weekly work.
* Running `wget http://activehistory.ca/papers/` downed the index.html for that webpage! This is an interesting case where "http://activehistory.ca/papers/index.html" isn't the same page as that one, and gives a HTTP 404 Not Found error. I don't know how the web hosting technology works server-side, but after using Chrome DevTools to see where the source of the page's HTML, it is in fact just "http://activehistory.ca/papers/" within that "papers" directory. There's no direct path ending in "index.html".
* I don't use `wget` enough; I've only looked up complex `wget` commands on Stack Overflow to download the entire tree / file structure of a course website at the end of a term before it was removed by the instructor (which was encouraged). I think this next command will be similar.
* Running `wget -r -np -w 2 --limit-rate=20k http://activehistory.ca/papers/` (without changing directories with `cd`) created an "activehistory.ca" directory with a "papers" directory containing all the pages under it; directories and their contents, like index.html. There are also some more technical website files like "robots.txt", [which hopes to limit site access by crawlers](https://support.google.com/webmasters/answer/6062608?hl=en). That worked surprisingly well, but probably due to the nature of how the website is set up. Like for those sites with Apache web servers where if you visit a directory, you can see the whole tree until you run into something you don't have permission to view, which would give an HTTP 403 Forbidden error. With many sites, you also have to know which URLs or subdirectories exist, else a simple `wget` command like this one won't download some pages. There's crawler software that exists to help guess where web pages be, but that's not nearly as easy or as fast as this.
 * Some of the requests resulted in an HTTP 404 Not Found error, but most gave a successful HTTP 200 OK response.
 * It was definitely a good ethical consideration to rate-limit this command out of respect for the website's owner. Maybe the bandwidth limit was too low, though. I'm going to continue on in another terminal while this continues to run.

### Using `wget` with a list of URLs

* I don't know too much about `wget`'s options, especially when they're the not-so-verbose single-letter flags/switches/options/arguments like `-i`. I'm going to guess that `-i` here stands for "iterate" or "item", since we're passing in a list of URLs to retrieve.
* I was wrong; the long form of it is `--input-file`. The answer is usually the most simple/common one, after all.
* I used `cd ..` to go up to my top-level repository directory, made a new directory "wget-url-list" with `mkdir`, used `cd wget-url-list` to enter it, then used `touch urls.txt` (in `bash`) to create a new file. I pasted the list of URLs in from the instructions and saved the file.
* As expected, `wget -i urls.txt -r --no-parent -nd -w 2 --limit-rate=100k` downloaded the four images from the URLs. Handy.
* The `wget` command from the previous step finished around this point; it took nearly six minutes to complete.

### Using `python` to generate a list of URLs

* Made a new "war-diaries" folder for this step along with a "generate-urls-file.py" to go in it.
* Referring to an empty declared variable as "bin" as a decent way of explaining things to non-programmers.
* Oops, wrong file name. From `bash`, I used `mv generate-urls-file.py urls.py` to rename the file.
* Looks like invoking the Python script generated a file with 81 URLs. I guess 29 to 109 inclusive is actually 81 numbers. Thanks to the \n in 
the script it seems there was already that new line at the end of the file that I mentioned last week. Nice!
* This time, `wget -i urls.txt -r --no-parent -nd -w 2 --limit-rate=100k` downloaded all the images from the URLs in the new urls.txt, so I got 81 images. Normally I wouldn't commit all these to a Git repository, but I will for this course. Surprisingly, `wget` says it was only 16 MB total! That was a lot of space back in the early 2000s, though.
* According to the [GNU Wget Manual](https://www.gnu.org/software/wget/manual/html_node/Directory-Options.html), the `-nd` (or `--no-directories`) option instructs `wget to "not create a hierarchy of directories when retrieving recursively`. Guess it wouldn't work without `-r`, or would be ignored otherwise, then.
 * I tested this out. Without `-r`, `-nd` is ignored, but the command proceeds as normal.

### Being a good digital citizen

* The instructions here are good advice, but I'm not so sure it could get you into trouble without malicious intent or very careless usage (e.g. [distributed denial-of-service (DDoS) attacks](https://en.wikipedia.org/wiki/Denial-of-service_attack#Distributed_DoS)). Though `wget` isn't something everyone will use, nowadays, it's probably the responsibility of the server/website owner to rate-limit incoming requests, rather than expecting users to rate-limit their own outgoing requests. I'm not a lawyer, though! It's a good ethical consideration to not make the assumption that the owner has protected against it, though, especially if it's an older website that hasn't changed in awhile.

## Application programming interfaces (APIs)

* Ah, APIs are something I need to spend more time with. Deceptively simple, but quite powerful. It's a broad field, technically, but knowing how RESTful APIs works even from a basic web development perspective could earn you an awesome career for life, and by extension, a lot of money for relatively little effort compared to other programming jobs. When using them doesn't work, it's important to push forward and try something else, as the instructions suggest.
 * Creating an API yourself is a different story, but is still really easy sometimes. It really depends on what you're working with, though. Luckily, it's a very well-documented subject.
 * When it comes to web-based APIs (as opposed to graphics APIs like Microsoft's DirectX or Apple's Metal), I wonder how many there are today compared to 20 years ago?
* Good thing I don't actually have to write any of my own code here, at least until Week 6. Despite the caution, everything here will probably just work as long as I can follow the instructions. But I should probably break out of my comfort zone and experiment with it more often!

### Getting material out of an API

* I moved the `wget` stuff to its own "wget" folder, and made an "apis" folder to put this work in.
* Interestingly, the installation of `python` I was accessing from `bash` couldn't find the `requests` module. Guess that exists on the Anaconda Powershell-installed Python, though, so I ran it there.
* Other than that, ca.py ran as expected. That's a ton of JSON on a single line. I'd use a beautifier/prettifier/pretty-printer if I wanted to read that. I used [this JSON formatter](https://jsonformatter.curiousconcept.com/) to check it out, and saved the result in data_pretty.json. Though with all that OCR'd text in those `ocr_eng` fields, it still ended up being 1101 lines! 
* JSON is a pretty great format. No really complaints about it other than that it disallows trailing commas. Maybe we'll see that change in the future.
* As mentioned in the instructions, converting JSON to CSV/XLS and vice-versa is also handy. It's a very common practice in the software industry; luckily, there are a lot of tools that make it easier to do programatically.

## Optical character recognition (OCR)

* This section's evidence is in the "ocr" folder.
* The instructions called it "Object Character Recognition", but I think "optical character recognition" is more common.
* Attempting to install RStudio in the base (root) environment of Anaconda Navigator ran indefinitely and never seemed to actually manipulate any files. Following the advice of peers in the class Discord server, I created a new environment "coolenv" and installed RStudio on it, as well as the Powershell Prompt. It worked painlessly after that!
* I've had potential reasons to use R in the past for courses that involved statistics (STAT 2507: Introduction to Statistical Modeling I, PSYC 2002: Introduction to Statistics in Psychology, COMP 3008: Human–Computer Interaction), but I didn't bother. Statistical modelling to this degree isn't really my thing, but it's undoubtedly useful. Because I've never actually used R and don't remember anything about R's syntax, this part won't be so familiar. R Studio seems like pretty good software, too.

### One file at a time

* I didn't have any issues having R output the text from the image, though I noticed I had to select the whole script before clicking "Run" to make R run the whole script a few lines at a time rather than one line at a time. Though it's nice to have an interactive mode like that, too.
* Interestingly, trying to view the output.txt from within R Studio made it appear as completely empty, but given its 1.6-kilobyte size it clearly wasn't. Luckily, the script worked as expected, and I was able to view the output from other text editors like Visual Studio Code.

### Looping over many files at once

* I saved the next five images in the series into a "many-pics" directory.
* As expected, running the script made "filename-ocr.txt" files for each of the images in the folder. Very clever and concise. My previous OCR strategy before was to use third-party software that takes a long time to run, or much more manual methods like the screenshot OCR tool in ShareX (the screenshot tool I mentioned in Week 1). The libraries used here also seem to offer more flexibility an options, as doing things programatically often does. But I recognize the `magick` and `tesseract` libraries here, so I guess it's up to third-party software developers to add options that make use of all of those libraries' options.

### Handwriting

* I don't know what OCR library ShareX uses, but it indeed tends to have trouble with English and Japanese handwriting. Good but possibly expensive idea to use Microsoft Azure technologies to do it. I believe an application of this was in the Cubari manga reader created by the creators of "Guya.moe", a fan site for a romantic comedy manga series.