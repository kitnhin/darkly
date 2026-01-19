## Overview
This page involves a feedback form with two input fields: name and message. I expected we are supposed to do XSS attack here, but the criteria to get the flag is somewhat unusual.

### XSS Attack Attempts
At first, various standard XSS payloads are tested such as:

```html
<script>alert("XSS")</script>
<img src=x onerror="alert('xss')"/>
" onfocus="alert(1)"
```

However, I noticed the form implements the following sanitization:

1. Content within angle brackets (`<...>`) is completely removed
   - Example: Typing `<test>` results in empty input

2. Double quotes are escaped with backslashes
   - Example: `"alert(1)"` becomes `\"alert(1)\"`


### Initial Finding
Gave up and was simply spamming things and somehow entered "a" in the name field and the flag is given immediately. Was confused, continued trying letters and found that some letters such as "i" and "e" also worked. 

### Frontend Analysis
Decided to go examine and frontend javascript code and found:

1. **`checkForm()`**: Called on form submission but is **undefined**
2. **`validate_form()`**: Only checks if fields are empty
   - And even the message check part doesnt work properly
3. Upon submission, a **POST request** is sent, indicating backend validation, hence unable to see why the flag is given

Upon research, found that normal XSS wouldnt work, but simply inputting words like `script` or `alert` works somehow.