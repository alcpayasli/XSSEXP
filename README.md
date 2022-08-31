# xssexp
Cross-Site-Scripting (XSS) Automatic Scanner

### Description
This tool is designed to test for xss vulnerabilities in web sites, it uses a list of payloads
to inject into parameters and check to see if they get reflected back.

    
### Getting Help
`python3 xssexp.py -h`

### Usage
 targeturl = http://ethical.com/xss/example1.php?name=hacker
 usage = python3 -u http://ethical.com/xss/example1.php?name=hackerINJECT -l payloads.txt
