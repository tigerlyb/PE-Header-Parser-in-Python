PE Header Based Antivirus Tool
==============================

In this project, I present a simple and faster apporach to distinguish between malware and legitimate .exe ﬁles by simply looking at the properties of the Windows Portable Executable (PE) headers, and develop a tool to detect malware from a large number of .exe files. We extract distinguishing features from the PE headers using the structural information standardized by the Miscrosoft Windows operating system for executables. 

Here are the following three major parts of this project: 

(1) collect a large dataset of malware .exe (given by the project advisor) and legitimate .exe from the two website, www.downloads.com and www.softpedia.com by writing a python script called "crawler.py" as a web spider to automatically download files from website;

(2) write three python scripts called "parse.py, parseM.py, parseN.py" to extract the features of each header ﬁeld, compare and ﬁnd the most signiﬁcant differences between malware and legitimate .exe ﬁles;

(3) write three python scripts called "icon.py, iconM.py, iconN.py" to extract the icons from the PE, and then ﬁnd the most prevalent icons from the malware .exe ﬁles by comparing from the legitimate .exe files.


Conclusion:

I have evaluated this apporach on a large dataset which contains 5598 malware samples and 1237 legitimate samples respectively. The result of our experiments show that the PE-Header-Based approach achieves more than 99% detection rate with less than 0.2% false positive for distinguishing between benign and malicious executables in less than 20 minutes. We have also found 3 most prevalent icons from malware that are seldom seen in legitimate PE ﬁles, and 8 types of misleading icons from malware. My results show that it is possible to identify the malware by simply looking at some key features from PE headers.
