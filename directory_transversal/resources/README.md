# Directory Traversal Attack

## What is Directory Traversal?

[OWASP Directory Traversal Documentation](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/01-Testing_Directory_Traversal_File_Include)

Many web applications use server-side scripts to include files. The problem is when these applications don't properly validate user input (form parameters, URLs, cookies, etc.), attackers can manipulate file paths to access files outside the intended directory.


## How It Works
The basic idea is using `../` to navigate up directory levels and access The basic idea is using `../` to navigate up directory levels and sensitive files (for example, the common /etc/passwd file on a UNIX-like platform) 

```
Normal:     http://192.168.165.3/index.php?page=member
Attack:     http://192.168.165.3/index.php?page=../../../../../../../../../../../../../etc/passwd
```

## Finding the Flag

The website sends alerts whenever you type to `../` with messages such as **"Nope.."** or **"Almost"** when there's not enough `../`, explicitly confirming there's a flag there. After adding enough `../`, the website gives an alert with the flag