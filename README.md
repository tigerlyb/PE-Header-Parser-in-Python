PE-Header-Based-Antivirus-Tool
==============================

Course Project

In this project, I present a simple and faster apporach
to distinguish between malware and legitimate .exe ﬁles by simply
looking at properties of the MS Windows Portable Executable
(PE) headers. We extract distinguishing features from the PEheaders
using the structural information standardized by the
Miscrosoft Windows operating system for executables. I use
the following three methodology: 
(1) collect a large dataset of malware .exe and legitimate .exe from the two website,
www.downloads.com and www.softpedia.com by using a WebSpider, 
(2) use a PE-Header-Parser to extract the features of each header ﬁeld, 
compare and ﬁnd the most signiﬁcant difference between malware and legitimate .exe ﬁles, 
(3) use a Icon-Extractor to extract the icons from the PE, ﬁnd the most prevalent icons from the malware .exe ﬁles.

I have evaluated our apporach on a large dataset which
contains 5598 malware samples and 1237 legitimate samples
respectively. The result of our experiments show that the PE-Header-Based 
approach achieves more than 99% detection rate
with less than 0.2% false positive for distinguishing between
benign and malicious executables in less than 20 minutes. We
have also found 3 most prevalent icons from malware that are
seldom seen in legitimate PE ﬁles, and 8 types of misleading icons
from malware. My results show that it is possible to identify the
malware by simply looking at some key features from PE headers
