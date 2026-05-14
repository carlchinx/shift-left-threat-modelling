# Threat Model Report: Gemini File Search - Managed RAG API

## Description

Threat model for Gemini File Search RAG API

## Summary Statistics

- Total findings: **275**
- Very High: **20**
- High: **93**
- Medium: **144**
- Low: **14**
- Very Low: **4**

## Findings

### Severity: Very High

#### F105 (AC06) — Using Malicious Files

- **Target:** Auth & Billing Service
- **Details:** An attack of this type exploits a system's configuration that allows an attacker to either directly access an executable file, for example through shell access; or in a possible worst case allows an attacker to upload a file and then execute it. Web servers, ftp servers, and message oriented middleware systems which have many integration points are particularly vulnerable, because both the programmers and the administrators must be in synch regarding the interfaces and the correct privileges for each interface.
- **Mitigations:** Design: Enforce principle of least privilegeDesign: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.
- **References:** https://capec.mitre.org/data/definitions/17.html, http://cwe.mitre.org/data/definitions/732.html, http://cwe.mitre.org/data/definitions/272.html, http://cwe.mitre.org/data/definitions/270.html

#### F061 (AC06) — Using Malicious Files

- **Target:** Gemini API Gateway
- **Details:** An attack of this type exploits a system's configuration that allows an attacker to either directly access an executable file, for example through shell access; or in a possible worst case allows an attacker to upload a file and then execute it. Web servers, ftp servers, and message oriented middleware systems which have many integration points are particularly vulnerable, because both the programmers and the administrators must be in synch regarding the interfaces and the correct privileges for each interface.
- **Mitigations:** Design: Enforce principle of least privilegeDesign: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.
- **References:** https://capec.mitre.org/data/definitions/17.html, http://cwe.mitre.org/data/definitions/732.html, http://cwe.mitre.org/data/definitions/272.html, http://cwe.mitre.org/data/definitions/270.html

#### F173 (AC06) — Using Malicious Files

- **Target:** Gemini LLM
- **Details:** An attack of this type exploits a system's configuration that allows an attacker to either directly access an executable file, for example through shell access; or in a possible worst case allows an attacker to upload a file and then execute it. Web servers, ftp servers, and message oriented middleware systems which have many integration points are particularly vulnerable, because both the programmers and the administrators must be in synch regarding the interfaces and the correct privileges for each interface.
- **Mitigations:** Design: Enforce principle of least privilegeDesign: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.
- **References:** https://capec.mitre.org/data/definitions/17.html, http://cwe.mitre.org/data/definitions/732.html, http://cwe.mitre.org/data/definitions/272.html, http://cwe.mitre.org/data/definitions/270.html

#### F017 (AC06) — Using Malicious Files

- **Target:** Gemini SDK / REST Client
- **Details:** An attack of this type exploits a system's configuration that allows an attacker to either directly access an executable file, for example through shell access; or in a possible worst case allows an attacker to upload a file and then execute it. Web servers, ftp servers, and message oriented middleware systems which have many integration points are particularly vulnerable, because both the programmers and the administrators must be in synch regarding the interfaces and the correct privileges for each interface.
- **Mitigations:** Design: Enforce principle of least privilegeDesign: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.
- **References:** https://capec.mitre.org/data/definitions/17.html, http://cwe.mitre.org/data/definitions/732.html, http://cwe.mitre.org/data/definitions/272.html, http://cwe.mitre.org/data/definitions/270.html

#### F132 (AC17) — Session Hijacking - ServerSide

- **Target:** Auth & Billing Service
- **Details:** This type of attack involves an adversary that exploits weaknesses in an application's use of sessions in performing authentication. The advarsary is able to steal or manipulate an active session and use it to gain unathorized access to the application.
- **Mitigations:** Properly encrypt and sign identity tokens in transit, and use industry standard session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf. Utilize a session timeout for all sessions. If the user does not explicitly logout, terminate their session after this period of inactivity. If the user logs back in then a new session key should be generated.
- **References:** https://capec.mitre.org/data/definitions/593.html

#### F088 (AC17) — Session Hijacking - ServerSide

- **Target:** Gemini API Gateway
- **Details:** This type of attack involves an adversary that exploits weaknesses in an application's use of sessions in performing authentication. The advarsary is able to steal or manipulate an active session and use it to gain unathorized access to the application.
- **Mitigations:** Properly encrypt and sign identity tokens in transit, and use industry standard session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf. Utilize a session timeout for all sessions. If the user does not explicitly logout, terminate their session after this period of inactivity. If the user logs back in then a new session key should be generated.
- **References:** https://capec.mitre.org/data/definitions/593.html

#### F200 (AC17) — Session Hijacking - ServerSide

- **Target:** Gemini LLM
- **Details:** This type of attack involves an adversary that exploits weaknesses in an application's use of sessions in performing authentication. The advarsary is able to steal or manipulate an active session and use it to gain unathorized access to the application.
- **Mitigations:** Properly encrypt and sign identity tokens in transit, and use industry standard session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf. Utilize a session timeout for all sessions. If the user does not explicitly logout, terminate their session after this period of inactivity. If the user logs back in then a new session key should be generated.
- **References:** https://capec.mitre.org/data/definitions/593.html

#### F044 (AC17) — Session Hijacking - ServerSide

- **Target:** Gemini SDK / REST Client
- **Details:** This type of attack involves an adversary that exploits weaknesses in an application's use of sessions in performing authentication. The advarsary is able to steal or manipulate an active session and use it to gain unathorized access to the application.
- **Mitigations:** Properly encrypt and sign identity tokens in transit, and use industry standard session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf. Utilize a session timeout for all sessions. If the user does not explicitly logout, terminate their session after this period of inactivity. If the user logs back in then a new session key should be generated.
- **References:** https://capec.mitre.org/data/definitions/593.html

#### F096 (HA01) — Path Traversal

- **Target:** Auth & Billing Service
- **Details:** An adversary uses path manipulation methods to exploit insufficient input validation of a target to obtain access to data that should be not be retrievable by ordinary well-formed requests. A typical variety of this attack involves specifying a path to a desired file together with dot-dot-slash characters, resulting in the file access API or function traversing out of the intended directory structure and into the root file system. By replacing or modifying the expected path information the access function or API retrieves the file desired by the attacker. These attacks either involve the attacker providing a complete path to a targeted file or using control characters (e.g. path separators (/ or ) and/or dots (.)) to reach desired directories or files.
- **Mitigations:** Design: Configure the access control correctly. Design: Enforce principle of least privilege. Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution. Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement. Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host. 6. Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands. Implementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin. Implementation: Perform input validation for all remote content, including remote and user-generated content. Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables. Implementation: Use indirect references rather than actual file names. Implementation: Use possible permissions on file access when developing and deploying web applications. Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification -- whitelisting approach.
- **References:** https://capec.mitre.org/data/definitions/126.html, http://cwe.mitre.org/data/definitions/22.html

#### F052 (HA01) — Path Traversal

- **Target:** Gemini API Gateway
- **Details:** An adversary uses path manipulation methods to exploit insufficient input validation of a target to obtain access to data that should be not be retrievable by ordinary well-formed requests. A typical variety of this attack involves specifying a path to a desired file together with dot-dot-slash characters, resulting in the file access API or function traversing out of the intended directory structure and into the root file system. By replacing or modifying the expected path information the access function or API retrieves the file desired by the attacker. These attacks either involve the attacker providing a complete path to a targeted file or using control characters (e.g. path separators (/ or ) and/or dots (.)) to reach desired directories or files.
- **Mitigations:** Design: Configure the access control correctly. Design: Enforce principle of least privilege. Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution. Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement. Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host. 6. Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands. Implementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin. Implementation: Perform input validation for all remote content, including remote and user-generated content. Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables. Implementation: Use indirect references rather than actual file names. Implementation: Use possible permissions on file access when developing and deploying web applications. Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification -- whitelisting approach.
- **References:** https://capec.mitre.org/data/definitions/126.html, http://cwe.mitre.org/data/definitions/22.html

#### F164 (HA01) — Path Traversal

- **Target:** Gemini LLM
- **Details:** An adversary uses path manipulation methods to exploit insufficient input validation of a target to obtain access to data that should be not be retrievable by ordinary well-formed requests. A typical variety of this attack involves specifying a path to a desired file together with dot-dot-slash characters, resulting in the file access API or function traversing out of the intended directory structure and into the root file system. By replacing or modifying the expected path information the access function or API retrieves the file desired by the attacker. These attacks either involve the attacker providing a complete path to a targeted file or using control characters (e.g. path separators (/ or ) and/or dots (.)) to reach desired directories or files.
- **Mitigations:** Design: Configure the access control correctly. Design: Enforce principle of least privilege. Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution. Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement. Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host. 6. Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands. Implementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin. Implementation: Perform input validation for all remote content, including remote and user-generated content. Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables. Implementation: Use indirect references rather than actual file names. Implementation: Use possible permissions on file access when developing and deploying web applications. Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification -- whitelisting approach.
- **References:** https://capec.mitre.org/data/definitions/126.html, http://cwe.mitre.org/data/definitions/22.html

#### F008 (HA01) — Path Traversal

- **Target:** Gemini SDK / REST Client
- **Details:** An adversary uses path manipulation methods to exploit insufficient input validation of a target to obtain access to data that should be not be retrievable by ordinary well-formed requests. A typical variety of this attack involves specifying a path to a desired file together with dot-dot-slash characters, resulting in the file access API or function traversing out of the intended directory structure and into the root file system. By replacing or modifying the expected path information the access function or API retrieves the file desired by the attacker. These attacks either involve the attacker providing a complete path to a targeted file or using control characters (e.g. path separators (/ or ) and/or dots (.)) to reach desired directories or files.
- **Mitigations:** Design: Configure the access control correctly. Design: Enforce principle of least privilege. Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution. Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement. Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host. 6. Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands. Implementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin. Implementation: Perform input validation for all remote content, including remote and user-generated content. Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables. Implementation: Use indirect references rather than actual file names. Implementation: Use possible permissions on file access when developing and deploying web applications. Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification -- whitelisting approach.
- **References:** https://capec.mitre.org/data/definitions/126.html, http://cwe.mitre.org/data/definitions/22.html

#### F090 (INP05) — Command Line Execution through SQL Injection

- **Target:** Auth & Billing Service
- **Details:** An attacker uses standard SQL injection methods to inject data into the command line for execution. This could be done directly through misuse of directives such as MSSQL_xp_cmdshell or indirectly through injection of data into the database that would be interpreted as shell commands. Sometime later, an unscrupulous backend application (or could be part of the functionality of the same application) fetches the injected data stored in the database and uses this data as command line arguments without performing proper validation. The malicious data escapes that data plane by spawning new commands to be executed on the host.
- **Mitigations:** Disable MSSQL xp_cmdshell directive on the databaseProperly validate the data (syntactically and semantically) before writing it to the database. Do not implicitly trust the data stored in the database. Re-validate it prior to usage to make sure that it is safe to use in a given context (e.g. as a command line argument).
- **References:** https://capec.mitre.org/data/definitions/108.html, http://cwe.mitre.org/data/definitions/89.html, http://cwe.mitre.org/data/definitions/74.html, http://cwe.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/78.html, http://cwe.mitre.org/data/definitions/114.html

#### F046 (INP05) — Command Line Execution through SQL Injection

- **Target:** Gemini API Gateway
- **Details:** An attacker uses standard SQL injection methods to inject data into the command line for execution. This could be done directly through misuse of directives such as MSSQL_xp_cmdshell or indirectly through injection of data into the database that would be interpreted as shell commands. Sometime later, an unscrupulous backend application (or could be part of the functionality of the same application) fetches the injected data stored in the database and uses this data as command line arguments without performing proper validation. The malicious data escapes that data plane by spawning new commands to be executed on the host.
- **Mitigations:** Disable MSSQL xp_cmdshell directive on the databaseProperly validate the data (syntactically and semantically) before writing it to the database. Do not implicitly trust the data stored in the database. Re-validate it prior to usage to make sure that it is safe to use in a given context (e.g. as a command line argument).
- **References:** https://capec.mitre.org/data/definitions/108.html, http://cwe.mitre.org/data/definitions/89.html, http://cwe.mitre.org/data/definitions/74.html, http://cwe.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/78.html, http://cwe.mitre.org/data/definitions/114.html

#### F158 (INP05) — Command Line Execution through SQL Injection

- **Target:** Gemini LLM
- **Details:** An attacker uses standard SQL injection methods to inject data into the command line for execution. This could be done directly through misuse of directives such as MSSQL_xp_cmdshell or indirectly through injection of data into the database that would be interpreted as shell commands. Sometime later, an unscrupulous backend application (or could be part of the functionality of the same application) fetches the injected data stored in the database and uses this data as command line arguments without performing proper validation. The malicious data escapes that data plane by spawning new commands to be executed on the host.
- **Mitigations:** Disable MSSQL xp_cmdshell directive on the databaseProperly validate the data (syntactically and semantically) before writing it to the database. Do not implicitly trust the data stored in the database. Re-validate it prior to usage to make sure that it is safe to use in a given context (e.g. as a command line argument).
- **References:** https://capec.mitre.org/data/definitions/108.html, http://cwe.mitre.org/data/definitions/89.html, http://cwe.mitre.org/data/definitions/74.html, http://cwe.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/78.html, http://cwe.mitre.org/data/definitions/114.html

#### F002 (INP05) — Command Line Execution through SQL Injection

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker uses standard SQL injection methods to inject data into the command line for execution. This could be done directly through misuse of directives such as MSSQL_xp_cmdshell or indirectly through injection of data into the database that would be interpreted as shell commands. Sometime later, an unscrupulous backend application (or could be part of the functionality of the same application) fetches the injected data stored in the database and uses this data as command line arguments without performing proper validation. The malicious data escapes that data plane by spawning new commands to be executed on the host.
- **Mitigations:** Disable MSSQL xp_cmdshell directive on the databaseProperly validate the data (syntactically and semantically) before writing it to the database. Do not implicitly trust the data stored in the database. Re-validate it prior to usage to make sure that it is safe to use in a given context (e.g. as a command line argument).
- **References:** https://capec.mitre.org/data/definitions/108.html, http://cwe.mitre.org/data/definitions/89.html, http://cwe.mitre.org/data/definitions/74.html, http://cwe.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/78.html, http://cwe.mitre.org/data/definitions/114.html

#### F107 (SC02) — XSS Targeting Non-Script Elements

- **Target:** Auth & Billing Service
- **Details:** This attack is a form of Cross-Site Scripting (XSS) where malicious scripts are embedded in elements that are not expected to host scripts such as image tags (<img>), comments in XML documents (< !-CDATA->), etc. These tags may not be subject to the same input validation, output validation, and other content filtering and checking routines, so this can create an opportunity for an attacker to tunnel through the application's elements and launch a XSS attack through other elements. As with all remote attacks, it is important to differentiate the ability to launch an attack (such as probing an internal network for unpatched servers) and the ability of the remote attacker to collect and interpret the output of said attack.
- **Mitigations:** In addition to the traditional input fields, all other user controllable inputs, such as image tags within messages or the likes, must also be subjected to input validation. Such validation should ensure that content that can be potentially interpreted as script by the browser is appropriately filtered.All output displayed to clients must be properly escaped. Escaping ensures that the browser interprets special scripting characters literally and not as script to be executed.
- **References:** https://capec.mitre.org/data/definitions/18.html, http://cwe.mitre.org/data/definitions/80.html

#### F063 (SC02) — XSS Targeting Non-Script Elements

- **Target:** Gemini API Gateway
- **Details:** This attack is a form of Cross-Site Scripting (XSS) where malicious scripts are embedded in elements that are not expected to host scripts such as image tags (<img>), comments in XML documents (< !-CDATA->), etc. These tags may not be subject to the same input validation, output validation, and other content filtering and checking routines, so this can create an opportunity for an attacker to tunnel through the application's elements and launch a XSS attack through other elements. As with all remote attacks, it is important to differentiate the ability to launch an attack (such as probing an internal network for unpatched servers) and the ability of the remote attacker to collect and interpret the output of said attack.
- **Mitigations:** In addition to the traditional input fields, all other user controllable inputs, such as image tags within messages or the likes, must also be subjected to input validation. Such validation should ensure that content that can be potentially interpreted as script by the browser is appropriately filtered.All output displayed to clients must be properly escaped. Escaping ensures that the browser interprets special scripting characters literally and not as script to be executed.
- **References:** https://capec.mitre.org/data/definitions/18.html, http://cwe.mitre.org/data/definitions/80.html

#### F175 (SC02) — XSS Targeting Non-Script Elements

- **Target:** Gemini LLM
- **Details:** This attack is a form of Cross-Site Scripting (XSS) where malicious scripts are embedded in elements that are not expected to host scripts such as image tags (<img>), comments in XML documents (< !-CDATA->), etc. These tags may not be subject to the same input validation, output validation, and other content filtering and checking routines, so this can create an opportunity for an attacker to tunnel through the application's elements and launch a XSS attack through other elements. As with all remote attacks, it is important to differentiate the ability to launch an attack (such as probing an internal network for unpatched servers) and the ability of the remote attacker to collect and interpret the output of said attack.
- **Mitigations:** In addition to the traditional input fields, all other user controllable inputs, such as image tags within messages or the likes, must also be subjected to input validation. Such validation should ensure that content that can be potentially interpreted as script by the browser is appropriately filtered.All output displayed to clients must be properly escaped. Escaping ensures that the browser interprets special scripting characters literally and not as script to be executed.
- **References:** https://capec.mitre.org/data/definitions/18.html, http://cwe.mitre.org/data/definitions/80.html

#### F019 (SC02) — XSS Targeting Non-Script Elements

- **Target:** Gemini SDK / REST Client
- **Details:** This attack is a form of Cross-Site Scripting (XSS) where malicious scripts are embedded in elements that are not expected to host scripts such as image tags (<img>), comments in XML documents (< !-CDATA->), etc. These tags may not be subject to the same input validation, output validation, and other content filtering and checking routines, so this can create an opportunity for an attacker to tunnel through the application's elements and launch a XSS attack through other elements. As with all remote attacks, it is important to differentiate the ability to launch an attack (such as probing an internal network for unpatched servers) and the ability of the remote attacker to collect and interpret the output of said attack.
- **Mitigations:** In addition to the traditional input fields, all other user controllable inputs, such as image tags within messages or the likes, must also be subjected to input validation. Such validation should ensure that content that can be potentially interpreted as script by the browser is appropriately filtered.All output displayed to clients must be properly escaped. Escaping ensures that the browser interprets special scripting characters literally and not as script to be executed.
- **References:** https://capec.mitre.org/data/definitions/18.html, http://cwe.mitre.org/data/definitions/80.html

### Severity: High

#### F118 (AA03) — Exploitation of Trusted Credentials

- **Target:** Auth & Billing Service
- **Details:** Attacks on session IDs and resource IDs take advantage of the fact that some software accepts user input without verifying its authenticity. For example, a message queuing system that allows service requesters to post messages to its queue through an open channel (such as anonymous FTP), authorization is done through checking group or role membership contained in the posted message. However, there is no proof that the message itself, the information in the message (such group or role membership), or indeed the process that wrote the message to the queue are authentic and authorized to do so. Many server side processes are vulnerable to these attacks because the server to server communications have not been analyzed from a security perspective or the processes trust other systems because they are behind a firewall. In a similar way servers that use easy to guess or spoofable schemes for representing digital identity can also be vulnerable. Such systems frequently use schemes without cryptography and digital signatures (or with broken cryptography). Session IDs may be guessed due to insufficient randomness, poor protection (passed in the clear), lack of integrity (unsigned), or improperly correlation with access control policy enforcement points. Exposed configuration and properties files that contain system passwords, database connection strings, and such may also give an attacker an edge to identify these identifiers. The net result is that spoofing and impersonation is possible leading to an attacker's ability to break authentication, authorization, and audit controls on the system.
- **Mitigations:** Design: utilize strong federated identity such as SAML to encrypt and sign identity tokens in transit.Implementation: Use industry standards session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf.Implementation: If the session identifier is used for authentication, such as in the so-called single sign on use cases, then ensure that it is protected at the same level of assurance as authentication tokens.Implementation: If the web or application server supports it, then encrypting and/or signing the session ID (such as cookie) can protect the ID if intercepted.Design: Use strong session identifiers that are protected in transit and at rest.Implementation: Utilize a session timeout for all sessions, for example 20 minutes. If the user does not explicitly logout, the server terminates their session after this period of inactivity. If the user logs back in then a new session key is generated.Implementation: Verify of authenticity of all session IDs at runtime.
- **References:** https://capec.mitre.org/data/definitions/21.html, http://cwe.mitre.org/data/definitions/290.html, http://cwe.mitre.org/data/definitions/346.html, http://cwe.mitre.org/data/definitions/664.html

#### F074 (AA03) — Exploitation of Trusted Credentials

- **Target:** Gemini API Gateway
- **Details:** Attacks on session IDs and resource IDs take advantage of the fact that some software accepts user input without verifying its authenticity. For example, a message queuing system that allows service requesters to post messages to its queue through an open channel (such as anonymous FTP), authorization is done through checking group or role membership contained in the posted message. However, there is no proof that the message itself, the information in the message (such group or role membership), or indeed the process that wrote the message to the queue are authentic and authorized to do so. Many server side processes are vulnerable to these attacks because the server to server communications have not been analyzed from a security perspective or the processes trust other systems because they are behind a firewall. In a similar way servers that use easy to guess or spoofable schemes for representing digital identity can also be vulnerable. Such systems frequently use schemes without cryptography and digital signatures (or with broken cryptography). Session IDs may be guessed due to insufficient randomness, poor protection (passed in the clear), lack of integrity (unsigned), or improperly correlation with access control policy enforcement points. Exposed configuration and properties files that contain system passwords, database connection strings, and such may also give an attacker an edge to identify these identifiers. The net result is that spoofing and impersonation is possible leading to an attacker's ability to break authentication, authorization, and audit controls on the system.
- **Mitigations:** Design: utilize strong federated identity such as SAML to encrypt and sign identity tokens in transit.Implementation: Use industry standards session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf.Implementation: If the session identifier is used for authentication, such as in the so-called single sign on use cases, then ensure that it is protected at the same level of assurance as authentication tokens.Implementation: If the web or application server supports it, then encrypting and/or signing the session ID (such as cookie) can protect the ID if intercepted.Design: Use strong session identifiers that are protected in transit and at rest.Implementation: Utilize a session timeout for all sessions, for example 20 minutes. If the user does not explicitly logout, the server terminates their session after this period of inactivity. If the user logs back in then a new session key is generated.Implementation: Verify of authenticity of all session IDs at runtime.
- **References:** https://capec.mitre.org/data/definitions/21.html, http://cwe.mitre.org/data/definitions/290.html, http://cwe.mitre.org/data/definitions/346.html, http://cwe.mitre.org/data/definitions/664.html

#### F186 (AA03) — Exploitation of Trusted Credentials

- **Target:** Gemini LLM
- **Details:** Attacks on session IDs and resource IDs take advantage of the fact that some software accepts user input without verifying its authenticity. For example, a message queuing system that allows service requesters to post messages to its queue through an open channel (such as anonymous FTP), authorization is done through checking group or role membership contained in the posted message. However, there is no proof that the message itself, the information in the message (such group or role membership), or indeed the process that wrote the message to the queue are authentic and authorized to do so. Many server side processes are vulnerable to these attacks because the server to server communications have not been analyzed from a security perspective or the processes trust other systems because they are behind a firewall. In a similar way servers that use easy to guess or spoofable schemes for representing digital identity can also be vulnerable. Such systems frequently use schemes without cryptography and digital signatures (or with broken cryptography). Session IDs may be guessed due to insufficient randomness, poor protection (passed in the clear), lack of integrity (unsigned), or improperly correlation with access control policy enforcement points. Exposed configuration and properties files that contain system passwords, database connection strings, and such may also give an attacker an edge to identify these identifiers. The net result is that spoofing and impersonation is possible leading to an attacker's ability to break authentication, authorization, and audit controls on the system.
- **Mitigations:** Design: utilize strong federated identity such as SAML to encrypt and sign identity tokens in transit.Implementation: Use industry standards session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf.Implementation: If the session identifier is used for authentication, such as in the so-called single sign on use cases, then ensure that it is protected at the same level of assurance as authentication tokens.Implementation: If the web or application server supports it, then encrypting and/or signing the session ID (such as cookie) can protect the ID if intercepted.Design: Use strong session identifiers that are protected in transit and at rest.Implementation: Utilize a session timeout for all sessions, for example 20 minutes. If the user does not explicitly logout, the server terminates their session after this period of inactivity. If the user logs back in then a new session key is generated.Implementation: Verify of authenticity of all session IDs at runtime.
- **References:** https://capec.mitre.org/data/definitions/21.html, http://cwe.mitre.org/data/definitions/290.html, http://cwe.mitre.org/data/definitions/346.html, http://cwe.mitre.org/data/definitions/664.html

#### F030 (AA03) — Exploitation of Trusted Credentials

- **Target:** Gemini SDK / REST Client
- **Details:** Attacks on session IDs and resource IDs take advantage of the fact that some software accepts user input without verifying its authenticity. For example, a message queuing system that allows service requesters to post messages to its queue through an open channel (such as anonymous FTP), authorization is done through checking group or role membership contained in the posted message. However, there is no proof that the message itself, the information in the message (such group or role membership), or indeed the process that wrote the message to the queue are authentic and authorized to do so. Many server side processes are vulnerable to these attacks because the server to server communications have not been analyzed from a security perspective or the processes trust other systems because they are behind a firewall. In a similar way servers that use easy to guess or spoofable schemes for representing digital identity can also be vulnerable. Such systems frequently use schemes without cryptography and digital signatures (or with broken cryptography). Session IDs may be guessed due to insufficient randomness, poor protection (passed in the clear), lack of integrity (unsigned), or improperly correlation with access control policy enforcement points. Exposed configuration and properties files that contain system passwords, database connection strings, and such may also give an attacker an edge to identify these identifiers. The net result is that spoofing and impersonation is possible leading to an attacker's ability to break authentication, authorization, and audit controls on the system.
- **Mitigations:** Design: utilize strong federated identity such as SAML to encrypt and sign identity tokens in transit.Implementation: Use industry standards session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf.Implementation: If the session identifier is used for authentication, such as in the so-called single sign on use cases, then ensure that it is protected at the same level of assurance as authentication tokens.Implementation: If the web or application server supports it, then encrypting and/or signing the session ID (such as cookie) can protect the ID if intercepted.Design: Use strong session identifiers that are protected in transit and at rest.Implementation: Utilize a session timeout for all sessions, for example 20 minutes. If the user does not explicitly logout, the server terminates their session after this period of inactivity. If the user logs back in then a new session key is generated.Implementation: Verify of authenticity of all session IDs at runtime.
- **References:** https://capec.mitre.org/data/definitions/21.html, http://cwe.mitre.org/data/definitions/290.html, http://cwe.mitre.org/data/definitions/346.html, http://cwe.mitre.org/data/definitions/664.html

#### F121 (AA04) — Exploiting Trust in Client

- **Target:** Auth & Billing Service
- **Details:** An attack of this type exploits vulnerabilities in client/server communication channel authentication and data integrity. It leverages the implicit trust a server places in the client, or more importantly, that which the server believes is the client. An attacker executes this type of attack by placing themselves in the communication channel between client and server such that communication directly to the server is possible where the server believes it is communicating only with a valid client. There are numerous variations of this type of attack.
- **Mitigations:** Design: Ensure that client process and/or message is authenticated so that anonymous communications and/or messages are not accepted by the system.Design: Do not rely on client validation or encoding for security purposes.Design: Utilize digital signatures to increase authentication assurance.Design: Utilize two factor authentication to increase authentication assurance.Implementation: Perform input validation for all remote content.
- **References:** https://capec.mitre.org/data/definitions/22.html, http://cwe.mitre.org/data/definitions/287.html

#### F077 (AA04) — Exploiting Trust in Client

- **Target:** Gemini API Gateway
- **Details:** An attack of this type exploits vulnerabilities in client/server communication channel authentication and data integrity. It leverages the implicit trust a server places in the client, or more importantly, that which the server believes is the client. An attacker executes this type of attack by placing themselves in the communication channel between client and server such that communication directly to the server is possible where the server believes it is communicating only with a valid client. There are numerous variations of this type of attack.
- **Mitigations:** Design: Ensure that client process and/or message is authenticated so that anonymous communications and/or messages are not accepted by the system.Design: Do not rely on client validation or encoding for security purposes.Design: Utilize digital signatures to increase authentication assurance.Design: Utilize two factor authentication to increase authentication assurance.Implementation: Perform input validation for all remote content.
- **References:** https://capec.mitre.org/data/definitions/22.html, http://cwe.mitre.org/data/definitions/287.html

#### F189 (AA04) — Exploiting Trust in Client

- **Target:** Gemini LLM
- **Details:** An attack of this type exploits vulnerabilities in client/server communication channel authentication and data integrity. It leverages the implicit trust a server places in the client, or more importantly, that which the server believes is the client. An attacker executes this type of attack by placing themselves in the communication channel between client and server such that communication directly to the server is possible where the server believes it is communicating only with a valid client. There are numerous variations of this type of attack.
- **Mitigations:** Design: Ensure that client process and/or message is authenticated so that anonymous communications and/or messages are not accepted by the system.Design: Do not rely on client validation or encoding for security purposes.Design: Utilize digital signatures to increase authentication assurance.Design: Utilize two factor authentication to increase authentication assurance.Implementation: Perform input validation for all remote content.
- **References:** https://capec.mitre.org/data/definitions/22.html, http://cwe.mitre.org/data/definitions/287.html

#### F033 (AA04) — Exploiting Trust in Client

- **Target:** Gemini SDK / REST Client
- **Details:** An attack of this type exploits vulnerabilities in client/server communication channel authentication and data integrity. It leverages the implicit trust a server places in the client, or more importantly, that which the server believes is the client. An attacker executes this type of attack by placing themselves in the communication channel between client and server such that communication directly to the server is possible where the server believes it is communicating only with a valid client. There are numerous variations of this type of attack.
- **Mitigations:** Design: Ensure that client process and/or message is authenticated so that anonymous communications and/or messages are not accepted by the system.Design: Do not rely on client validation or encoding for security purposes.Design: Utilize digital signatures to increase authentication assurance.Design: Utilize two factor authentication to increase authentication assurance.Implementation: Perform input validation for all remote content.
- **References:** https://capec.mitre.org/data/definitions/22.html, http://cwe.mitre.org/data/definitions/287.html

#### F131 (AC16) — Session Credential Falsification through Prediction

- **Target:** Auth & Billing Service
- **Details:** This attack targets predictable session ID in order to gain privileges. The attacker can predict the session ID used during a transaction to perform spoofing and session hijacking.
- **Mitigations:** Use a strong source of randomness to generate a session ID.Use adequate length session IDs. Do not use information available to the user in order to generate session ID (e.g., time).Ideas for creating random numbers are offered by Eastlake [RFC1750]. Encrypt the session ID if you expose it to the user. For instance session ID can be stored in a cookie in encrypted format.
- **References:** https://capec.mitre.org/data/definitions/59.html

#### F087 (AC16) — Session Credential Falsification through Prediction

- **Target:** Gemini API Gateway
- **Details:** This attack targets predictable session ID in order to gain privileges. The attacker can predict the session ID used during a transaction to perform spoofing and session hijacking.
- **Mitigations:** Use a strong source of randomness to generate a session ID.Use adequate length session IDs. Do not use information available to the user in order to generate session ID (e.g., time).Ideas for creating random numbers are offered by Eastlake [RFC1750]. Encrypt the session ID if you expose it to the user. For instance session ID can be stored in a cookie in encrypted format.
- **References:** https://capec.mitre.org/data/definitions/59.html

#### F199 (AC16) — Session Credential Falsification through Prediction

- **Target:** Gemini LLM
- **Details:** This attack targets predictable session ID in order to gain privileges. The attacker can predict the session ID used during a transaction to perform spoofing and session hijacking.
- **Mitigations:** Use a strong source of randomness to generate a session ID.Use adequate length session IDs. Do not use information available to the user in order to generate session ID (e.g., time).Ideas for creating random numbers are offered by Eastlake [RFC1750]. Encrypt the session ID if you expose it to the user. For instance session ID can be stored in a cookie in encrypted format.
- **References:** https://capec.mitre.org/data/definitions/59.html

#### F043 (AC16) — Session Credential Falsification through Prediction

- **Target:** Gemini SDK / REST Client
- **Details:** This attack targets predictable session ID in order to gain privileges. The attacker can predict the session ID used during a transaction to perform spoofing and session hijacking.
- **Mitigations:** Use a strong source of randomness to generate a session ID.Use adequate length session IDs. Do not use information available to the user in order to generate session ID (e.g., time).Ideas for creating random numbers are offered by Eastlake [RFC1750]. Encrypt the session ID if you expose it to the user. For instance session ID can be stored in a cookie in encrypted format.
- **References:** https://capec.mitre.org/data/definitions/59.html

#### F103 (CR03) — Dictionary-based Password Attack

- **Target:** Auth & Billing Service
- **Details:** An attacker tries each of the words in a dictionary as passwords to gain access to the system via some user's account. If the password chosen by the user was a word within the dictionary, this attack will be successful (in the absence of other mitigations). This is a specific instance of the password brute forcing attack pattern.
- **Mitigations:** Create a strong password policy and ensure that your system enforces this policy.Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-02.
- **References:** https://capec.mitre.org/data/definitions/16.html, http://cwe.mitre.org/data/definitions/521.html, http://cwe.mitre.org/data/definitions/262.html, http://cwe.mitre.org/data/definitions/263.html

#### F059 (CR03) — Dictionary-based Password Attack

- **Target:** Gemini API Gateway
- **Details:** An attacker tries each of the words in a dictionary as passwords to gain access to the system via some user's account. If the password chosen by the user was a word within the dictionary, this attack will be successful (in the absence of other mitigations). This is a specific instance of the password brute forcing attack pattern.
- **Mitigations:** Create a strong password policy and ensure that your system enforces this policy.Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-02.
- **References:** https://capec.mitre.org/data/definitions/16.html, http://cwe.mitre.org/data/definitions/521.html, http://cwe.mitre.org/data/definitions/262.html, http://cwe.mitre.org/data/definitions/263.html

#### F171 (CR03) — Dictionary-based Password Attack

- **Target:** Gemini LLM
- **Details:** An attacker tries each of the words in a dictionary as passwords to gain access to the system via some user's account. If the password chosen by the user was a word within the dictionary, this attack will be successful (in the absence of other mitigations). This is a specific instance of the password brute forcing attack pattern.
- **Mitigations:** Create a strong password policy and ensure that your system enforces this policy.Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-02.
- **References:** https://capec.mitre.org/data/definitions/16.html, http://cwe.mitre.org/data/definitions/521.html, http://cwe.mitre.org/data/definitions/262.html, http://cwe.mitre.org/data/definitions/263.html

#### F015 (CR03) — Dictionary-based Password Attack

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker tries each of the words in a dictionary as passwords to gain access to the system via some user's account. If the password chosen by the user was a word within the dictionary, this attack will be successful (in the absence of other mitigations). This is a specific instance of the password brute forcing attack pattern.
- **Mitigations:** Create a strong password policy and ensure that your system enforces this policy.Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-02.
- **References:** https://capec.mitre.org/data/definitions/16.html, http://cwe.mitre.org/data/definitions/521.html, http://cwe.mitre.org/data/definitions/262.html, http://cwe.mitre.org/data/definitions/263.html

#### F204 (CR06) — Communication Channel Manipulation

- **Target:** API key/token
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F269 (CR06) — Communication Channel Manipulation

- **Target:** API response
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F259 (CR06) — Communication Channel Manipulation

- **Target:** Context + prompt
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F274 (CR06) — Communication Channel Manipulation

- **Target:** Display response
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F219 (CR06) — Communication Channel Manipulation

- **Target:** File to API
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F214 (CR06) — Communication Channel Manipulation

- **Target:** File upload
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F264 (CR06) — Communication Channel Manipulation

- **Target:** LLM response
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F244 (CR06) — Communication Channel Manipulation

- **Target:** Prompt to API
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F249 (CR06) — Communication Channel Manipulation

- **Target:** Query vectors
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F254 (CR06) — Communication Channel Manipulation

- **Target:** Relevant chunks
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F224 (CR06) — Communication Channel Manipulation

- **Target:** Store file
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F234 (CR06) — Communication Channel Manipulation

- **Target:** Store vectors
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F209 (CR06) — Communication Channel Manipulation

- **Target:** Token validation
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F229 (CR06) — Communication Channel Manipulation

- **Target:** Trigger embedding
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F239 (CR06) — Communication Channel Manipulation

- **Target:** User prompt
- **Details:** An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.
- **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
- **References:** https://capec.mitre.org/data/definitions/216.html

#### F136 (DE04) — Audit Log Manipulation

- **Target:** User File Store
- **Details:** The attacker injects, manipulates, deletes, or forges malicious log entries into the log file, in an attempt to mislead an audit of the log file or cover tracks of an attack. Due to either insufficient access controls of the log files or the logging mechanism, the attacker is able to perform such actions.
- **Mitigations:** Use Principle of Least Privilege to avoid unauthorized access to log files leading to manipulation/injection on those files. Do not allow tainted data to be written in the log file without prior input validation. Whitelisting may be used to properly validate the data. Use synchronization to control the flow of execution. Use static analysis tool to identify log forging vulnerabilities. Avoid viewing logs with tools that may interpret control characters in the file, such as command-line shells.
- **References:** https://capec.mitre.org/data/definitions/268.html, https://capec.mitre.org/data/definitions/93.html

#### F148 (DE04) — Audit Log Manipulation

- **Target:** Vector Store
- **Details:** The attacker injects, manipulates, deletes, or forges malicious log entries into the log file, in an attempt to mislead an audit of the log file or cover tracks of an attack. Due to either insufficient access controls of the log files or the logging mechanism, the attacker is able to perform such actions.
- **Mitigations:** Use Principle of Least Privilege to avoid unauthorized access to log files leading to manipulation/injection on those files. Do not allow tainted data to be written in the log file without prior input validation. Whitelisting may be used to properly validate the data. Use synchronization to control the flow of execution. Use static analysis tool to identify log forging vulnerabilities. Avoid viewing logs with tools that may interpret control characters in the file, such as command-line shells.
- **References:** https://capec.mitre.org/data/definitions/268.html, https://capec.mitre.org/data/definitions/93.html

#### F089 (INP03) — Server Side Include (SSI) Injection

- **Target:** Auth & Billing Service
- **Details:** An attacker can use Server Side Include (SSI) Injection to send code to a web application that then gets executed by the web server. Doing so enables the attacker to achieve similar results to Cross Site Scripting, viz., arbitrary code execution and information disclosure, albeit on a more limited scale, since the SSI directives are nowhere near as powerful as a full-fledged scripting language. Nonetheless, the attacker can conveniently gain access to sensitive files, such as password files, and execute shell commands.
- **Mitigations:** Set the OPTIONS IncludesNOEXEC in the global access.conf file or local .htaccess (Apache) file to deny SSI execution in directories that do not need them. All user controllable input must be appropriately sanitized before use in the application. This includes omitting, or encoding, certain characters or strings that have the potential of being interpreted as part of an SSI directive. Server Side Includes must be enabled only if there is a strong business reason to do so. Every additional component enabled on the web server increases the attack surface as well as administrative overhead.
- **References:** https://capec.mitre.org/data/definitions/101.html, http://cwe.mitre.org/data/definitions/97.html, http://cwe.mitre.org/data/definitions/74.html, http://cwe.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/713.html

#### F045 (INP03) — Server Side Include (SSI) Injection

- **Target:** Gemini API Gateway
- **Details:** An attacker can use Server Side Include (SSI) Injection to send code to a web application that then gets executed by the web server. Doing so enables the attacker to achieve similar results to Cross Site Scripting, viz., arbitrary code execution and information disclosure, albeit on a more limited scale, since the SSI directives are nowhere near as powerful as a full-fledged scripting language. Nonetheless, the attacker can conveniently gain access to sensitive files, such as password files, and execute shell commands.
- **Mitigations:** Set the OPTIONS IncludesNOEXEC in the global access.conf file or local .htaccess (Apache) file to deny SSI execution in directories that do not need them. All user controllable input must be appropriately sanitized before use in the application. This includes omitting, or encoding, certain characters or strings that have the potential of being interpreted as part of an SSI directive. Server Side Includes must be enabled only if there is a strong business reason to do so. Every additional component enabled on the web server increases the attack surface as well as administrative overhead.
- **References:** https://capec.mitre.org/data/definitions/101.html, http://cwe.mitre.org/data/definitions/97.html, http://cwe.mitre.org/data/definitions/74.html, http://cwe.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/713.html

#### F157 (INP03) — Server Side Include (SSI) Injection

- **Target:** Gemini LLM
- **Details:** An attacker can use Server Side Include (SSI) Injection to send code to a web application that then gets executed by the web server. Doing so enables the attacker to achieve similar results to Cross Site Scripting, viz., arbitrary code execution and information disclosure, albeit on a more limited scale, since the SSI directives are nowhere near as powerful as a full-fledged scripting language. Nonetheless, the attacker can conveniently gain access to sensitive files, such as password files, and execute shell commands.
- **Mitigations:** Set the OPTIONS IncludesNOEXEC in the global access.conf file or local .htaccess (Apache) file to deny SSI execution in directories that do not need them. All user controllable input must be appropriately sanitized before use in the application. This includes omitting, or encoding, certain characters or strings that have the potential of being interpreted as part of an SSI directive. Server Side Includes must be enabled only if there is a strong business reason to do so. Every additional component enabled on the web server increases the attack surface as well as administrative overhead.
- **References:** https://capec.mitre.org/data/definitions/101.html, http://cwe.mitre.org/data/definitions/97.html, http://cwe.mitre.org/data/definitions/74.html, http://cwe.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/713.html

#### F001 (INP03) — Server Side Include (SSI) Injection

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker can use Server Side Include (SSI) Injection to send code to a web application that then gets executed by the web server. Doing so enables the attacker to achieve similar results to Cross Site Scripting, viz., arbitrary code execution and information disclosure, albeit on a more limited scale, since the SSI directives are nowhere near as powerful as a full-fledged scripting language. Nonetheless, the attacker can conveniently gain access to sensitive files, such as password files, and execute shell commands.
- **Mitigations:** Set the OPTIONS IncludesNOEXEC in the global access.conf file or local .htaccess (Apache) file to deny SSI execution in directories that do not need them. All user controllable input must be appropriately sanitized before use in the application. This includes omitting, or encoding, certain characters or strings that have the potential of being interpreted as part of an SSI directive. Server Side Includes must be enabled only if there is a strong business reason to do so. Every additional component enabled on the web server increases the attack surface as well as administrative overhead.
- **References:** https://capec.mitre.org/data/definitions/101.html, http://cwe.mitre.org/data/definitions/97.html, http://cwe.mitre.org/data/definitions/74.html, http://cwe.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/713.html

#### F098 (INP08) — Format String Injection

- **Target:** Auth & Billing Service
- **Details:** An adversary includes formatting characters in a string input field on the target application. Most applications assume that users will provide static text and may respond unpredictably to the presence of formatting character. For example, in certain functions of the C programming languages such as printf, the formatting character %s will print the contents of a memory location expecting this location to identify a string and the formatting character %n prints the number of DWORD written in the memory. An adversary can use this to read or write to memory locations or files, or simply to manipulate the value of the resulting text in unexpected ways. Reading or writing memory may result in program crashes and writing memory could result in the execution of arbitrary code if the adversary can write to the program stack.
- **Mitigations:** Limit the usage of formatting string functions. Strong input validation - All user-controllable input must be validated and filtered for illegal formatting characters.
- **References:** https://capec.mitre.org/data/definitions/135.html, http://cwe.mitre.org/data/definitions/134.html, http://cwe.mitre.org/data/definitions/133.html

#### F150 (INP08) — Format String Injection

- **Target:** Context Injection Engine
- **Details:** An adversary includes formatting characters in a string input field on the target application. Most applications assume that users will provide static text and may respond unpredictably to the presence of formatting character. For example, in certain functions of the C programming languages such as printf, the formatting character %s will print the contents of a memory location expecting this location to identify a string and the formatting character %n prints the number of DWORD written in the memory. An adversary can use this to read or write to memory locations or files, or simply to manipulate the value of the resulting text in unexpected ways. Reading or writing memory may result in program crashes and writing memory could result in the execution of arbitrary code if the adversary can write to the program stack.
- **Mitigations:** Limit the usage of formatting string functions. Strong input validation - All user-controllable input must be validated and filtered for illegal formatting characters.
- **References:** https://capec.mitre.org/data/definitions/135.html, http://cwe.mitre.org/data/definitions/134.html, http://cwe.mitre.org/data/definitions/133.html

#### F138 (INP08) — Format String Injection

- **Target:** Embedding Service
- **Details:** An adversary includes formatting characters in a string input field on the target application. Most applications assume that users will provide static text and may respond unpredictably to the presence of formatting character. For example, in certain functions of the C programming languages such as printf, the formatting character %s will print the contents of a memory location expecting this location to identify a string and the formatting character %n prints the number of DWORD written in the memory. An adversary can use this to read or write to memory locations or files, or simply to manipulate the value of the resulting text in unexpected ways. Reading or writing memory may result in program crashes and writing memory could result in the execution of arbitrary code if the adversary can write to the program stack.
- **Mitigations:** Limit the usage of formatting string functions. Strong input validation - All user-controllable input must be validated and filtered for illegal formatting characters.
- **References:** https://capec.mitre.org/data/definitions/135.html, http://cwe.mitre.org/data/definitions/134.html, http://cwe.mitre.org/data/definitions/133.html

#### F054 (INP08) — Format String Injection

- **Target:** Gemini API Gateway
- **Details:** An adversary includes formatting characters in a string input field on the target application. Most applications assume that users will provide static text and may respond unpredictably to the presence of formatting character. For example, in certain functions of the C programming languages such as printf, the formatting character %s will print the contents of a memory location expecting this location to identify a string and the formatting character %n prints the number of DWORD written in the memory. An adversary can use this to read or write to memory locations or files, or simply to manipulate the value of the resulting text in unexpected ways. Reading or writing memory may result in program crashes and writing memory could result in the execution of arbitrary code if the adversary can write to the program stack.
- **Mitigations:** Limit the usage of formatting string functions. Strong input validation - All user-controllable input must be validated and filtered for illegal formatting characters.
- **References:** https://capec.mitre.org/data/definitions/135.html, http://cwe.mitre.org/data/definitions/134.html, http://cwe.mitre.org/data/definitions/133.html

#### F166 (INP08) — Format String Injection

- **Target:** Gemini LLM
- **Details:** An adversary includes formatting characters in a string input field on the target application. Most applications assume that users will provide static text and may respond unpredictably to the presence of formatting character. For example, in certain functions of the C programming languages such as printf, the formatting character %s will print the contents of a memory location expecting this location to identify a string and the formatting character %n prints the number of DWORD written in the memory. An adversary can use this to read or write to memory locations or files, or simply to manipulate the value of the resulting text in unexpected ways. Reading or writing memory may result in program crashes and writing memory could result in the execution of arbitrary code if the adversary can write to the program stack.
- **Mitigations:** Limit the usage of formatting string functions. Strong input validation - All user-controllable input must be validated and filtered for illegal formatting characters.
- **References:** https://capec.mitre.org/data/definitions/135.html, http://cwe.mitre.org/data/definitions/134.html, http://cwe.mitre.org/data/definitions/133.html

#### F010 (INP08) — Format String Injection

- **Target:** Gemini SDK / REST Client
- **Details:** An adversary includes formatting characters in a string input field on the target application. Most applications assume that users will provide static text and may respond unpredictably to the presence of formatting character. For example, in certain functions of the C programming languages such as printf, the formatting character %s will print the contents of a memory location expecting this location to identify a string and the formatting character %n prints the number of DWORD written in the memory. An adversary can use this to read or write to memory locations or files, or simply to manipulate the value of the resulting text in unexpected ways. Reading or writing memory may result in program crashes and writing memory could result in the execution of arbitrary code if the adversary can write to the program stack.
- **Mitigations:** Limit the usage of formatting string functions. Strong input validation - All user-controllable input must be validated and filtered for illegal formatting characters.
- **References:** https://capec.mitre.org/data/definitions/135.html, http://cwe.mitre.org/data/definitions/134.html, http://cwe.mitre.org/data/definitions/133.html

#### F099 (INP09) — LDAP Injection

- **Target:** Auth & Billing Service
- **Details:** An attacker manipulates or crafts an LDAP query for the purpose of undermining the security of the target. Some applications use user input to create LDAP queries that are processed by an LDAP server. For example, a user might provide their username during authentication and the username might be inserted in an LDAP query during the authentication process. An attacker could use this input to inject additional commands into an LDAP query that could disclose sensitive information. For example, entering a * in the aforementioned query might return information about all users on the system. This attack is very similar to an SQL injection attack in that it manipulates a query to gather additional information or coerce a particular return value.
- **Mitigations:** Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as LDAP content. Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the LDAP or application.
- **References:** https://capec.mitre.org/data/definitions/136.html, http://cwe.mitre.org/data/definitions/77.html, http://cwe.mitre.org/data/definitions/90.html, http://cwe.mitre.org/data/definitions/20.html

#### F055 (INP09) — LDAP Injection

- **Target:** Gemini API Gateway
- **Details:** An attacker manipulates or crafts an LDAP query for the purpose of undermining the security of the target. Some applications use user input to create LDAP queries that are processed by an LDAP server. For example, a user might provide their username during authentication and the username might be inserted in an LDAP query during the authentication process. An attacker could use this input to inject additional commands into an LDAP query that could disclose sensitive information. For example, entering a * in the aforementioned query might return information about all users on the system. This attack is very similar to an SQL injection attack in that it manipulates a query to gather additional information or coerce a particular return value.
- **Mitigations:** Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as LDAP content. Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the LDAP or application.
- **References:** https://capec.mitre.org/data/definitions/136.html, http://cwe.mitre.org/data/definitions/77.html, http://cwe.mitre.org/data/definitions/90.html, http://cwe.mitre.org/data/definitions/20.html

#### F167 (INP09) — LDAP Injection

- **Target:** Gemini LLM
- **Details:** An attacker manipulates or crafts an LDAP query for the purpose of undermining the security of the target. Some applications use user input to create LDAP queries that are processed by an LDAP server. For example, a user might provide their username during authentication and the username might be inserted in an LDAP query during the authentication process. An attacker could use this input to inject additional commands into an LDAP query that could disclose sensitive information. For example, entering a * in the aforementioned query might return information about all users on the system. This attack is very similar to an SQL injection attack in that it manipulates a query to gather additional information or coerce a particular return value.
- **Mitigations:** Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as LDAP content. Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the LDAP or application.
- **References:** https://capec.mitre.org/data/definitions/136.html, http://cwe.mitre.org/data/definitions/77.html, http://cwe.mitre.org/data/definitions/90.html, http://cwe.mitre.org/data/definitions/20.html

#### F011 (INP09) — LDAP Injection

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker manipulates or crafts an LDAP query for the purpose of undermining the security of the target. Some applications use user input to create LDAP queries that are processed by an LDAP server. For example, a user might provide their username during authentication and the username might be inserted in an LDAP query during the authentication process. An attacker could use this input to inject additional commands into an LDAP query that could disclose sensitive information. For example, entering a * in the aforementioned query might return information about all users on the system. This attack is very similar to an SQL injection attack in that it manipulates a query to gather additional information or coerce a particular return value.
- **Mitigations:** Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as LDAP content. Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the LDAP or application.
- **References:** https://capec.mitre.org/data/definitions/136.html, http://cwe.mitre.org/data/definitions/77.html, http://cwe.mitre.org/data/definitions/90.html, http://cwe.mitre.org/data/definitions/20.html

#### F101 (INP11) — Relative Path Traversal

- **Target:** Auth & Billing Service
- **Details:** An attacker exploits a weakness in input validation on the target by supplying a specially constructed path utilizing dot and slash characters for the purpose of obtaining access to arbitrary files or resources. An attacker modifies a known path on the target in order to reach material that is not available through intended channels. These attacks normally involve adding additional path separators (/ or ) and/or dots (.), or encodings thereof, in various combinations in order to reach parent directories or entirely separate trees of the target's directory structure.
- **Mitigations:** Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement. Implementation: Perform input validation for all remote content, including remote and user-generated content. Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification -- whitelisting approach. Implementation: Prefer working without user input when using file system calls. Implementation: Use indirect references rather than actual file names. Implementation: Use possible permissions on file access when developing and deploying web applications.
- **References:** https://capec.mitre.org/data/definitions/139.html, http://cwe.mitre.org/data/definitions/23.html

#### F057 (INP11) — Relative Path Traversal

- **Target:** Gemini API Gateway
- **Details:** An attacker exploits a weakness in input validation on the target by supplying a specially constructed path utilizing dot and slash characters for the purpose of obtaining access to arbitrary files or resources. An attacker modifies a known path on the target in order to reach material that is not available through intended channels. These attacks normally involve adding additional path separators (/ or ) and/or dots (.), or encodings thereof, in various combinations in order to reach parent directories or entirely separate trees of the target's directory structure.
- **Mitigations:** Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement. Implementation: Perform input validation for all remote content, including remote and user-generated content. Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification -- whitelisting approach. Implementation: Prefer working without user input when using file system calls. Implementation: Use indirect references rather than actual file names. Implementation: Use possible permissions on file access when developing and deploying web applications.
- **References:** https://capec.mitre.org/data/definitions/139.html, http://cwe.mitre.org/data/definitions/23.html

#### F169 (INP11) — Relative Path Traversal

- **Target:** Gemini LLM
- **Details:** An attacker exploits a weakness in input validation on the target by supplying a specially constructed path utilizing dot and slash characters for the purpose of obtaining access to arbitrary files or resources. An attacker modifies a known path on the target in order to reach material that is not available through intended channels. These attacks normally involve adding additional path separators (/ or ) and/or dots (.), or encodings thereof, in various combinations in order to reach parent directories or entirely separate trees of the target's directory structure.
- **Mitigations:** Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement. Implementation: Perform input validation for all remote content, including remote and user-generated content. Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification -- whitelisting approach. Implementation: Prefer working without user input when using file system calls. Implementation: Use indirect references rather than actual file names. Implementation: Use possible permissions on file access when developing and deploying web applications.
- **References:** https://capec.mitre.org/data/definitions/139.html, http://cwe.mitre.org/data/definitions/23.html

#### F013 (INP11) — Relative Path Traversal

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker exploits a weakness in input validation on the target by supplying a specially constructed path utilizing dot and slash characters for the purpose of obtaining access to arbitrary files or resources. An attacker modifies a known path on the target in order to reach material that is not available through intended channels. These attacks normally involve adding additional path separators (/ or ) and/or dots (.), or encodings thereof, in various combinations in order to reach parent directories or entirely separate trees of the target's directory structure.
- **Mitigations:** Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement. Implementation: Perform input validation for all remote content, including remote and user-generated content. Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification -- whitelisting approach. Implementation: Prefer working without user input when using file system calls. Implementation: Use indirect references rather than actual file names. Implementation: Use possible permissions on file access when developing and deploying web applications.
- **References:** https://capec.mitre.org/data/definitions/139.html, http://cwe.mitre.org/data/definitions/23.html

#### F151 (INP12) — Client-side Injection-induced Buffer Overflow

- **Target:** Context Injection Engine
- **Details:** This type of attack exploits a buffer overflow vulnerability in targeted client software through injection of malicious content from a custom-built hostile service.
- **Mitigations:** The client software should not install untrusted code from a non-authenticated server. The client software should have the latest patches and should be audited for vulnerabilities before being used to communicate with potentially hostile servers. Perform input validation for length of buffer inputs. Use a language or compiler that performs automatic bounds checking. Use an abstraction library to abstract away risky APIs. Not a complete solution. Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution. Ensure all buffer uses are consistently bounds-checked. Use OS-level preventative functionality. Not a complete solution.
- **References:** https://capec.mitre.org/data/definitions/14.html, http://cwe.mitre.org/data/definitions/74.html, http://cwe.mitre.org/data/definitions/353.html

#### F139 (INP12) — Client-side Injection-induced Buffer Overflow

- **Target:** Embedding Service
- **Details:** This type of attack exploits a buffer overflow vulnerability in targeted client software through injection of malicious content from a custom-built hostile service.
- **Mitigations:** The client software should not install untrusted code from a non-authenticated server. The client software should have the latest patches and should be audited for vulnerabilities before being used to communicate with potentially hostile servers. Perform input validation for length of buffer inputs. Use a language or compiler that performs automatic bounds checking. Use an abstraction library to abstract away risky APIs. Not a complete solution. Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution. Ensure all buffer uses are consistently bounds-checked. Use OS-level preventative functionality. Not a complete solution.
- **References:** https://capec.mitre.org/data/definitions/14.html, http://cwe.mitre.org/data/definitions/74.html, http://cwe.mitre.org/data/definitions/353.html

#### F152 (INP13) — Command Delimiters

- **Target:** Context Injection Engine
- **Details:** An attack of this type exploits a programs' vulnerabilities that allows an attacker's commands to be concatenated onto a legitimate command with the intent of targeting other resources such as the file system or database. The system that uses a filter or a blacklist input validation, as opposed to whitelist validation is vulnerable to an attacker who predicts delimiters (or combinations of delimiters) not present in the filter or blacklist. As with other injection attacks, the attacker uses the command delimiter payload as an entry point to tunnel through the application and activate additional attacks through SQL queries, shell commands, network scanning, and so on.
- **Mitigations:** Design: Perform whitelist validation against a positive specification for command length, type, and parameters.Design: Limit program privileges, so if commands circumvent program input validation or filter routines then commands do not running under a privileged accountImplementation: Perform input validation for all remote content.Implementation: Use type conversions such as JDBC prepared statements.
- **References:** https://capec.mitre.org/data/definitions/15.html, http://cwe.mitre.org/data/definitions/146.html, http://cwe.mitre.org/data/definitions/77.html, http://cwe.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/154.html

#### F140 (INP13) — Command Delimiters

- **Target:** Embedding Service
- **Details:** An attack of this type exploits a programs' vulnerabilities that allows an attacker's commands to be concatenated onto a legitimate command with the intent of targeting other resources such as the file system or database. The system that uses a filter or a blacklist input validation, as opposed to whitelist validation is vulnerable to an attacker who predicts delimiters (or combinations of delimiters) not present in the filter or blacklist. As with other injection attacks, the attacker uses the command delimiter payload as an entry point to tunnel through the application and activate additional attacks through SQL queries, shell commands, network scanning, and so on.
- **Mitigations:** Design: Perform whitelist validation against a positive specification for command length, type, and parameters.Design: Limit program privileges, so if commands circumvent program input validation or filter routines then commands do not running under a privileged accountImplementation: Perform input validation for all remote content.Implementation: Use type conversions such as JDBC prepared statements.
- **References:** https://capec.mitre.org/data/definitions/15.html, http://cwe.mitre.org/data/definitions/146.html, http://cwe.mitre.org/data/definitions/77.html, http://cwe.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/154.html

#### F110 (INP16) — PHP Remote File Inclusion

- **Target:** Auth & Billing Service
- **Details:** In this pattern the adversary is able to load and execute arbitrary code remotely available from the application. This is usually accomplished through an insecurely configured PHP runtime environment and an improperly sanitized include or require call, which the user can then control to point to any web-accessible file. This allows adversaries to hijack the targeted application and force it to execute their own instructions.
- **Mitigations:** Implementation: Perform input validation for all remote content, including remote and user-generated contentImplementation: Only allow known files to be included (whitelist)Implementation: Make use of indirect references passed in URL parameters instead of file namesConfiguration: Ensure that remote scripts cannot be include in the include or require PHP directives
- **References:** https://capec.mitre.org/data/definitions/193.html, http://cwe.mitre.org/data/definitions/98.html, http://cwe.mitre.org/data/definitions/80.html, http://cwe.mitre.org/data/definitions/714.html

#### F066 (INP16) — PHP Remote File Inclusion

- **Target:** Gemini API Gateway
- **Details:** In this pattern the adversary is able to load and execute arbitrary code remotely available from the application. This is usually accomplished through an insecurely configured PHP runtime environment and an improperly sanitized include or require call, which the user can then control to point to any web-accessible file. This allows adversaries to hijack the targeted application and force it to execute their own instructions.
- **Mitigations:** Implementation: Perform input validation for all remote content, including remote and user-generated contentImplementation: Only allow known files to be included (whitelist)Implementation: Make use of indirect references passed in URL parameters instead of file namesConfiguration: Ensure that remote scripts cannot be include in the include or require PHP directives
- **References:** https://capec.mitre.org/data/definitions/193.html, http://cwe.mitre.org/data/definitions/98.html, http://cwe.mitre.org/data/definitions/80.html, http://cwe.mitre.org/data/definitions/714.html

#### F178 (INP16) — PHP Remote File Inclusion

- **Target:** Gemini LLM
- **Details:** In this pattern the adversary is able to load and execute arbitrary code remotely available from the application. This is usually accomplished through an insecurely configured PHP runtime environment and an improperly sanitized include or require call, which the user can then control to point to any web-accessible file. This allows adversaries to hijack the targeted application and force it to execute their own instructions.
- **Mitigations:** Implementation: Perform input validation for all remote content, including remote and user-generated contentImplementation: Only allow known files to be included (whitelist)Implementation: Make use of indirect references passed in URL parameters instead of file namesConfiguration: Ensure that remote scripts cannot be include in the include or require PHP directives
- **References:** https://capec.mitre.org/data/definitions/193.html, http://cwe.mitre.org/data/definitions/98.html, http://cwe.mitre.org/data/definitions/80.html, http://cwe.mitre.org/data/definitions/714.html

#### F022 (INP16) — PHP Remote File Inclusion

- **Target:** Gemini SDK / REST Client
- **Details:** In this pattern the adversary is able to load and execute arbitrary code remotely available from the application. This is usually accomplished through an insecurely configured PHP runtime environment and an improperly sanitized include or require call, which the user can then control to point to any web-accessible file. This allows adversaries to hijack the targeted application and force it to execute their own instructions.
- **Mitigations:** Implementation: Perform input validation for all remote content, including remote and user-generated contentImplementation: Only allow known files to be included (whitelist)Implementation: Make use of indirect references passed in URL parameters instead of file namesConfiguration: Ensure that remote scripts cannot be include in the include or require PHP directives
- **References:** https://capec.mitre.org/data/definitions/193.html, http://cwe.mitre.org/data/definitions/98.html, http://cwe.mitre.org/data/definitions/80.html, http://cwe.mitre.org/data/definitions/714.html

#### F125 (INP22) — XML Attribute Blowup

- **Target:** Auth & Billing Service
- **Details:** This attack exploits certain XML parsers which manage data in an inefficient manner. The attacker crafts an XML document with many attributes in the same XML node. In a vulnerable parser, this results in a denial of service condition owhere CPU resources are exhausted because of the parsing algorithm.
- **Mitigations:** This attack may be mitigated completely by using a parser that is not using a vulnerable container. Mitigation may also limit the number of attributes per XML element.
- **References:** https://capec.mitre.org/data/definitions/229.html, http://cwe.mitre.org/data/definitions/770.html

#### F081 (INP22) — XML Attribute Blowup

- **Target:** Gemini API Gateway
- **Details:** This attack exploits certain XML parsers which manage data in an inefficient manner. The attacker crafts an XML document with many attributes in the same XML node. In a vulnerable parser, this results in a denial of service condition owhere CPU resources are exhausted because of the parsing algorithm.
- **Mitigations:** This attack may be mitigated completely by using a parser that is not using a vulnerable container. Mitigation may also limit the number of attributes per XML element.
- **References:** https://capec.mitre.org/data/definitions/229.html, http://cwe.mitre.org/data/definitions/770.html

#### F193 (INP22) — XML Attribute Blowup

- **Target:** Gemini LLM
- **Details:** This attack exploits certain XML parsers which manage data in an inefficient manner. The attacker crafts an XML document with many attributes in the same XML node. In a vulnerable parser, this results in a denial of service condition owhere CPU resources are exhausted because of the parsing algorithm.
- **Mitigations:** This attack may be mitigated completely by using a parser that is not using a vulnerable container. Mitigation may also limit the number of attributes per XML element.
- **References:** https://capec.mitre.org/data/definitions/229.html, http://cwe.mitre.org/data/definitions/770.html

#### F037 (INP22) — XML Attribute Blowup

- **Target:** Gemini SDK / REST Client
- **Details:** This attack exploits certain XML parsers which manage data in an inefficient manner. The attacker crafts an XML document with many attributes in the same XML node. In a vulnerable parser, this results in a denial of service condition owhere CPU resources are exhausted because of the parsing algorithm.
- **Mitigations:** This attack may be mitigated completely by using a parser that is not using a vulnerable container. Mitigation may also limit the number of attributes per XML element.
- **References:** https://capec.mitre.org/data/definitions/229.html, http://cwe.mitre.org/data/definitions/770.html

#### F154 (INP24) — Filter Failure through Buffer Overflow

- **Target:** Context Injection Engine
- **Details:** In this attack, the idea is to cause an active filter to fail by causing an oversized transaction. An attacker may try to feed overly long input strings to the program in an attempt to overwhelm the filter (by causing a buffer overflow) and hoping that the filter does not fail securely (i.e. the user input is let into the system unfiltered).
- **Mitigations:** Make sure that ANY failure occurring in the filtering or input validation routine is properly handled and that offending input is NOT allowed to go through. Basically make sure that the vault is closed when failure occurs.Pre-design: Use a language or compiler that performs automatic bounds checking.Pre-design through Build: Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.Operational: Use OS-level preventative functionality. Not a complete solution.Design: Use an abstraction library to abstract away risky APIs. Not a complete solution.
- **References:** https://capec.mitre.org/data/definitions/24.html, http://cwe.mitre.org/data/definitions/120.html, http://cwe.mitre.org/data/definitions/680.html, http://cwe.mitre.org/data/definitions/20.html

#### F142 (INP24) — Filter Failure through Buffer Overflow

- **Target:** Embedding Service
- **Details:** In this attack, the idea is to cause an active filter to fail by causing an oversized transaction. An attacker may try to feed overly long input strings to the program in an attempt to overwhelm the filter (by causing a buffer overflow) and hoping that the filter does not fail securely (i.e. the user input is let into the system unfiltered).
- **Mitigations:** Make sure that ANY failure occurring in the filtering or input validation routine is properly handled and that offending input is NOT allowed to go through. Basically make sure that the vault is closed when failure occurs.Pre-design: Use a language or compiler that performs automatic bounds checking.Pre-design through Build: Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.Operational: Use OS-level preventative functionality. Not a complete solution.Design: Use an abstraction library to abstract away risky APIs. Not a complete solution.
- **References:** https://capec.mitre.org/data/definitions/24.html, http://cwe.mitre.org/data/definitions/120.html, http://cwe.mitre.org/data/definitions/680.html, http://cwe.mitre.org/data/definitions/20.html

#### F155 (INP25) — Resource Injection

- **Target:** Context Injection Engine
- **Details:** An adversary exploits weaknesses in input validation by manipulating resource identifiers enabling the unintended modification or specification of a resource.
- **Mitigations:** Ensure all input content that is delivered to client is sanitized against an acceptable content specification.Perform input validation for all content.Enforce regular patching of software.
- **References:** https://capec.mitre.org/data/definitions/240.html, https://capec.mitre.org/data/definitions/240.html

#### F143 (INP25) — Resource Injection

- **Target:** Embedding Service
- **Details:** An adversary exploits weaknesses in input validation by manipulating resource identifiers enabling the unintended modification or specification of a resource.
- **Mitigations:** Ensure all input content that is delivered to client is sanitized against an acceptable content specification.Perform input validation for all content.Enforce regular patching of software.
- **References:** https://capec.mitre.org/data/definitions/240.html, https://capec.mitre.org/data/definitions/240.html

#### F156 (INP26) — Code Injection

- **Target:** Context Injection Engine
- **Details:** An adversary exploits a weakness in input validation on the target to inject new code into that which is currently executing. This differs from code inclusion in that code inclusion involves the addition or replacement of a reference to a code file, which is subsequently loaded by the target and used as part of the code of some application.
- **Mitigations:** Utilize strict type, character, and encoding enforcementEnsure all input content that is delivered to client is sanitized against an acceptable content specification.Perform input validation for all content.Enforce regular patching of software.
- **References:** https://capec.mitre.org/data/definitions/242.html, http://cwe.mitre.org/data/definitions/94.html

#### F144 (INP26) — Code Injection

- **Target:** Embedding Service
- **Details:** An adversary exploits a weakness in input validation on the target to inject new code into that which is currently executing. This differs from code inclusion in that code inclusion involves the addition or replacement of a reference to a code file, which is subsequently loaded by the target and used as part of the code of some application.
- **Mitigations:** Utilize strict type, character, and encoding enforcementEnsure all input content that is delivered to client is sanitized against an acceptable content specification.Perform input validation for all content.Enforce regular patching of software.
- **References:** https://capec.mitre.org/data/definitions/242.html, http://cwe.mitre.org/data/definitions/94.html

#### F126 (INP28) — XSS Targeting URI Placeholders

- **Target:** Auth & Billing Service
- **Details:** An attack of this type exploits the ability of most browsers to interpret data, javascript or other URI schemes as client-side executable content placeholders. This attack consists of passing a malicious URI in an anchor tag HREF attribute or any other similar attributes in other HTML tags. Such malicious URI contains, for example, a base64 encoded HTML content with an embedded cross-site scripting payload. The attack is executed when the browser interprets the malicious content i.e., for example, when the victim clicks on the malicious link.
- **Mitigations:** Design: Use browser technologies that do not allow client side scripting.Design: Utilize strict type, character, and encoding enforcement.Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.Implementation: Ensure all content coming from the client is using the same encoding; if not, the server-side application must canonicalize the data before applying any filtering.Implementation: Perform input validation for all remote content, including remote and user-generated contentImplementation: Perform output validation for all remote content.Implementation: Disable scripting languages such as JavaScript in browserImplementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
- **References:** https://capec.mitre.org/data/definitions/244.html, http://cwe.mitre.org/data/definitions/83.html

#### F082 (INP28) — XSS Targeting URI Placeholders

- **Target:** Gemini API Gateway
- **Details:** An attack of this type exploits the ability of most browsers to interpret data, javascript or other URI schemes as client-side executable content placeholders. This attack consists of passing a malicious URI in an anchor tag HREF attribute or any other similar attributes in other HTML tags. Such malicious URI contains, for example, a base64 encoded HTML content with an embedded cross-site scripting payload. The attack is executed when the browser interprets the malicious content i.e., for example, when the victim clicks on the malicious link.
- **Mitigations:** Design: Use browser technologies that do not allow client side scripting.Design: Utilize strict type, character, and encoding enforcement.Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.Implementation: Ensure all content coming from the client is using the same encoding; if not, the server-side application must canonicalize the data before applying any filtering.Implementation: Perform input validation for all remote content, including remote and user-generated contentImplementation: Perform output validation for all remote content.Implementation: Disable scripting languages such as JavaScript in browserImplementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
- **References:** https://capec.mitre.org/data/definitions/244.html, http://cwe.mitre.org/data/definitions/83.html

#### F194 (INP28) — XSS Targeting URI Placeholders

- **Target:** Gemini LLM
- **Details:** An attack of this type exploits the ability of most browsers to interpret data, javascript or other URI schemes as client-side executable content placeholders. This attack consists of passing a malicious URI in an anchor tag HREF attribute or any other similar attributes in other HTML tags. Such malicious URI contains, for example, a base64 encoded HTML content with an embedded cross-site scripting payload. The attack is executed when the browser interprets the malicious content i.e., for example, when the victim clicks on the malicious link.
- **Mitigations:** Design: Use browser technologies that do not allow client side scripting.Design: Utilize strict type, character, and encoding enforcement.Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.Implementation: Ensure all content coming from the client is using the same encoding; if not, the server-side application must canonicalize the data before applying any filtering.Implementation: Perform input validation for all remote content, including remote and user-generated contentImplementation: Perform output validation for all remote content.Implementation: Disable scripting languages such as JavaScript in browserImplementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
- **References:** https://capec.mitre.org/data/definitions/244.html, http://cwe.mitre.org/data/definitions/83.html

#### F038 (INP28) — XSS Targeting URI Placeholders

- **Target:** Gemini SDK / REST Client
- **Details:** An attack of this type exploits the ability of most browsers to interpret data, javascript or other URI schemes as client-side executable content placeholders. This attack consists of passing a malicious URI in an anchor tag HREF attribute or any other similar attributes in other HTML tags. Such malicious URI contains, for example, a base64 encoded HTML content with an embedded cross-site scripting payload. The attack is executed when the browser interprets the malicious content i.e., for example, when the victim clicks on the malicious link.
- **Mitigations:** Design: Use browser technologies that do not allow client side scripting.Design: Utilize strict type, character, and encoding enforcement.Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.Implementation: Ensure all content coming from the client is using the same encoding; if not, the server-side application must canonicalize the data before applying any filtering.Implementation: Perform input validation for all remote content, including remote and user-generated contentImplementation: Perform output validation for all remote content.Implementation: Disable scripting languages such as JavaScript in browserImplementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
- **References:** https://capec.mitre.org/data/definitions/244.html, http://cwe.mitre.org/data/definitions/83.html

#### F128 (INP34) — SOAP Array Overflow

- **Target:** Auth & Billing Service
- **Details:** An attacker sends a SOAP request with an array whose actual length exceeds the length indicated in the request. When a data structure including a SOAP array is instantiated, the sender transmits the size of the array as an explicit parameter along with the data. If the server processing the transmission naively trusts the specified size, then an attacker can intentionally understate the size of the array, possibly resulting in a buffer overflow if the server attempts to read the entire data set into the memory it allocated for a smaller array. This, in turn, can lead to a server crash or even the execution of arbitrary code.
- **Mitigations:** If the server either verifies the correctness of the stated array size or if the server stops processing an array once the stated number of elements have been read, regardless of the actual array size, then this attack will fail. The former detects the malformed SOAP message while the latter ensures that the server does not attempt to load more data than was allocated for.
- **References:** https://capec.mitre.org/data/definitions/256.html

#### F084 (INP34) — SOAP Array Overflow

- **Target:** Gemini API Gateway
- **Details:** An attacker sends a SOAP request with an array whose actual length exceeds the length indicated in the request. When a data structure including a SOAP array is instantiated, the sender transmits the size of the array as an explicit parameter along with the data. If the server processing the transmission naively trusts the specified size, then an attacker can intentionally understate the size of the array, possibly resulting in a buffer overflow if the server attempts to read the entire data set into the memory it allocated for a smaller array. This, in turn, can lead to a server crash or even the execution of arbitrary code.
- **Mitigations:** If the server either verifies the correctness of the stated array size or if the server stops processing an array once the stated number of elements have been read, regardless of the actual array size, then this attack will fail. The former detects the malformed SOAP message while the latter ensures that the server does not attempt to load more data than was allocated for.
- **References:** https://capec.mitre.org/data/definitions/256.html

#### F196 (INP34) — SOAP Array Overflow

- **Target:** Gemini LLM
- **Details:** An attacker sends a SOAP request with an array whose actual length exceeds the length indicated in the request. When a data structure including a SOAP array is instantiated, the sender transmits the size of the array as an explicit parameter along with the data. If the server processing the transmission naively trusts the specified size, then an attacker can intentionally understate the size of the array, possibly resulting in a buffer overflow if the server attempts to read the entire data set into the memory it allocated for a smaller array. This, in turn, can lead to a server crash or even the execution of arbitrary code.
- **Mitigations:** If the server either verifies the correctness of the stated array size or if the server stops processing an array once the stated number of elements have been read, regardless of the actual array size, then this attack will fail. The former detects the malformed SOAP message while the latter ensures that the server does not attempt to load more data than was allocated for.
- **References:** https://capec.mitre.org/data/definitions/256.html

#### F040 (INP34) — SOAP Array Overflow

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker sends a SOAP request with an array whose actual length exceeds the length indicated in the request. When a data structure including a SOAP array is instantiated, the sender transmits the size of the array as an explicit parameter along with the data. If the server processing the transmission naively trusts the specified size, then an attacker can intentionally understate the size of the array, possibly resulting in a buffer overflow if the server attempts to read the entire data set into the memory it allocated for a smaller array. This, in turn, can lead to a server crash or even the execution of arbitrary code.
- **Mitigations:** If the server either verifies the correctness of the stated array size or if the server stops processing an array once the stated number of elements have been read, regardless of the actual array size, then this attack will fail. The former detects the malformed SOAP message while the latter ensures that the server does not attempt to load more data than was allocated for.
- **References:** https://capec.mitre.org/data/definitions/256.html

#### F130 (INP37) — HTTP Request Smuggling

- **Target:** Auth & Billing Service
- **Details:** HTTP Request Smuggling results from the discrepancies in parsing HTTP requests between HTTP entities such as web caching proxies or application firewalls. Entities such as web servers, web caching proxies, application firewalls or simple proxies often parse HTTP requests in slightly different ways. Under specific situations where there are two or more such entities in the path of the HTTP request, a specially crafted request is seen by two attacked entities as two different sets of requests. This allows certain requests to be smuggled through to a second entity without the first one realizing it.
- **Mitigations:** HTTP Request Smuggling is usually targeted at web servers. Therefore, in such cases, careful analysis of the entities must occur during system design prior to deployment. If there are known differences in the way the entities parse HTTP requests, the choice of entities needs consideration.Employing an application firewall can help. However, there are instances of the firewalls being susceptible to HTTP Request Smuggling as well.
- **References:** https://capec.mitre.org/data/definitions/33.html

#### F086 (INP37) — HTTP Request Smuggling

- **Target:** Gemini API Gateway
- **Details:** HTTP Request Smuggling results from the discrepancies in parsing HTTP requests between HTTP entities such as web caching proxies or application firewalls. Entities such as web servers, web caching proxies, application firewalls or simple proxies often parse HTTP requests in slightly different ways. Under specific situations where there are two or more such entities in the path of the HTTP request, a specially crafted request is seen by two attacked entities as two different sets of requests. This allows certain requests to be smuggled through to a second entity without the first one realizing it.
- **Mitigations:** HTTP Request Smuggling is usually targeted at web servers. Therefore, in such cases, careful analysis of the entities must occur during system design prior to deployment. If there are known differences in the way the entities parse HTTP requests, the choice of entities needs consideration.Employing an application firewall can help. However, there are instances of the firewalls being susceptible to HTTP Request Smuggling as well.
- **References:** https://capec.mitre.org/data/definitions/33.html

#### F198 (INP37) — HTTP Request Smuggling

- **Target:** Gemini LLM
- **Details:** HTTP Request Smuggling results from the discrepancies in parsing HTTP requests between HTTP entities such as web caching proxies or application firewalls. Entities such as web servers, web caching proxies, application firewalls or simple proxies often parse HTTP requests in slightly different ways. Under specific situations where there are two or more such entities in the path of the HTTP request, a specially crafted request is seen by two attacked entities as two different sets of requests. This allows certain requests to be smuggled through to a second entity without the first one realizing it.
- **Mitigations:** HTTP Request Smuggling is usually targeted at web servers. Therefore, in such cases, careful analysis of the entities must occur during system design prior to deployment. If there are known differences in the way the entities parse HTTP requests, the choice of entities needs consideration.Employing an application firewall can help. However, there are instances of the firewalls being susceptible to HTTP Request Smuggling as well.
- **References:** https://capec.mitre.org/data/definitions/33.html

#### F042 (INP37) — HTTP Request Smuggling

- **Target:** Gemini SDK / REST Client
- **Details:** HTTP Request Smuggling results from the discrepancies in parsing HTTP requests between HTTP entities such as web caching proxies or application firewalls. Entities such as web servers, web caching proxies, application firewalls or simple proxies often parse HTTP requests in slightly different ways. Under specific situations where there are two or more such entities in the path of the HTTP request, a specially crafted request is seen by two attacked entities as two different sets of requests. This allows certain requests to be smuggled through to a second entity without the first one realizing it.
- **Mitigations:** HTTP Request Smuggling is usually targeted at web servers. Therefore, in such cases, careful analysis of the entities must occur during system design prior to deployment. If there are known differences in the way the entities parse HTTP requests, the choice of entities needs consideration.Employing an application firewall can help. However, there are instances of the firewalls being susceptible to HTTP Request Smuggling as well.
- **References:** https://capec.mitre.org/data/definitions/33.html

#### F109 (SC03) — Embedding Scripts within Scripts

- **Target:** Auth & Billing Service
- **Details:** An attack of this type exploits a programs' vulnerabilities that are brought on by allowing remote hosts to execute scripts. The adversary leverages this capability to execute his/her own script by embedding it within other scripts that the target software is likely to execute. The adversary must have the ability to inject their script into a script that is likely to be executed. If this is done, then the adversary can potentially launch a variety of probes and attacks against the web server's local environment, in many cases the so-called DMZ, back end resources the web server can communicate with, and other hosts. With the proliferation of intermediaries, such as Web App Firewalls, network devices, and even printers having JVMs and Web servers, there are many locales where an attacker can inject malicious scripts. Since this attack pattern defines scripts within scripts, there are likely privileges to execute said attack on the host. These attacks are not solely limited to the server side, client side scripts like Ajax and client side JavaScript can contain malicious scripts as well.
- **Mitigations:** Use browser technologies that do not allow client side scripting.Utilize strict type, character, and encoding enforcement.Server side developers should not proxy content via XHR or other means. If a HTTP proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.Ensure all content that is delivered to client is sanitized against an acceptable content specification.Perform input validation for all remote content.Perform output validation for all remote content.Disable scripting languages such as JavaScript in browserSession tokens for specific hostPatching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.Privileges are constrained, if a script is loaded, ensure system runs in chroot jail or other limited authority mode
- **References:** https://capec.mitre.org/data/definitions/19.html, http://cwe.mitre.org/data/definitions/284.html

#### F065 (SC03) — Embedding Scripts within Scripts

- **Target:** Gemini API Gateway
- **Details:** An attack of this type exploits a programs' vulnerabilities that are brought on by allowing remote hosts to execute scripts. The adversary leverages this capability to execute his/her own script by embedding it within other scripts that the target software is likely to execute. The adversary must have the ability to inject their script into a script that is likely to be executed. If this is done, then the adversary can potentially launch a variety of probes and attacks against the web server's local environment, in many cases the so-called DMZ, back end resources the web server can communicate with, and other hosts. With the proliferation of intermediaries, such as Web App Firewalls, network devices, and even printers having JVMs and Web servers, there are many locales where an attacker can inject malicious scripts. Since this attack pattern defines scripts within scripts, there are likely privileges to execute said attack on the host. These attacks are not solely limited to the server side, client side scripts like Ajax and client side JavaScript can contain malicious scripts as well.
- **Mitigations:** Use browser technologies that do not allow client side scripting.Utilize strict type, character, and encoding enforcement.Server side developers should not proxy content via XHR or other means. If a HTTP proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.Ensure all content that is delivered to client is sanitized against an acceptable content specification.Perform input validation for all remote content.Perform output validation for all remote content.Disable scripting languages such as JavaScript in browserSession tokens for specific hostPatching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.Privileges are constrained, if a script is loaded, ensure system runs in chroot jail or other limited authority mode
- **References:** https://capec.mitre.org/data/definitions/19.html, http://cwe.mitre.org/data/definitions/284.html

#### F177 (SC03) — Embedding Scripts within Scripts

- **Target:** Gemini LLM
- **Details:** An attack of this type exploits a programs' vulnerabilities that are brought on by allowing remote hosts to execute scripts. The adversary leverages this capability to execute his/her own script by embedding it within other scripts that the target software is likely to execute. The adversary must have the ability to inject their script into a script that is likely to be executed. If this is done, then the adversary can potentially launch a variety of probes and attacks against the web server's local environment, in many cases the so-called DMZ, back end resources the web server can communicate with, and other hosts. With the proliferation of intermediaries, such as Web App Firewalls, network devices, and even printers having JVMs and Web servers, there are many locales where an attacker can inject malicious scripts. Since this attack pattern defines scripts within scripts, there are likely privileges to execute said attack on the host. These attacks are not solely limited to the server side, client side scripts like Ajax and client side JavaScript can contain malicious scripts as well.
- **Mitigations:** Use browser technologies that do not allow client side scripting.Utilize strict type, character, and encoding enforcement.Server side developers should not proxy content via XHR or other means. If a HTTP proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.Ensure all content that is delivered to client is sanitized against an acceptable content specification.Perform input validation for all remote content.Perform output validation for all remote content.Disable scripting languages such as JavaScript in browserSession tokens for specific hostPatching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.Privileges are constrained, if a script is loaded, ensure system runs in chroot jail or other limited authority mode
- **References:** https://capec.mitre.org/data/definitions/19.html, http://cwe.mitre.org/data/definitions/284.html

#### F021 (SC03) — Embedding Scripts within Scripts

- **Target:** Gemini SDK / REST Client
- **Details:** An attack of this type exploits a programs' vulnerabilities that are brought on by allowing remote hosts to execute scripts. The adversary leverages this capability to execute his/her own script by embedding it within other scripts that the target software is likely to execute. The adversary must have the ability to inject their script into a script that is likely to be executed. If this is done, then the adversary can potentially launch a variety of probes and attacks against the web server's local environment, in many cases the so-called DMZ, back end resources the web server can communicate with, and other hosts. With the proliferation of intermediaries, such as Web App Firewalls, network devices, and even printers having JVMs and Web servers, there are many locales where an attacker can inject malicious scripts. Since this attack pattern defines scripts within scripts, there are likely privileges to execute said attack on the host. These attacks are not solely limited to the server side, client side scripts like Ajax and client side JavaScript can contain malicious scripts as well.
- **Mitigations:** Use browser technologies that do not allow client side scripting.Utilize strict type, character, and encoding enforcement.Server side developers should not proxy content via XHR or other means. If a HTTP proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.Ensure all content that is delivered to client is sanitized against an acceptable content specification.Perform input validation for all remote content.Perform output validation for all remote content.Disable scripting languages such as JavaScript in browserSession tokens for specific hostPatching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.Privileges are constrained, if a script is loaded, ensure system runs in chroot jail or other limited authority mode
- **References:** https://capec.mitre.org/data/definitions/19.html, http://cwe.mitre.org/data/definitions/284.html

#### F113 (SC04) — XSS Using Alternate Syntax

- **Target:** Auth & Billing Service
- **Details:** An adversary uses alternate forms of keywords or commands that result in the same action as the primary form but which may not be caught by filters. For example, many keywords are processed in a case insensitive manner. If the site's web filtering algorithm does not convert all tags into a consistent case before the comparison with forbidden keywords it is possible to bypass filters (e.g., incomplete black lists) by using an alternate case structure. For example, the script tag using the alternate forms of Script or ScRiPt may bypass filters where script is the only form tested. Other variants using different syntax representations are also possible as well as using pollution meta-characters or entities that are eventually ignored by the rendering engine. The attack can result in the execution of otherwise prohibited functionality.
- **Mitigations:** Design: Use browser technologies that do not allow client side scripting.Design: Utilize strict type, character, and encoding enforcementImplementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.Implementation: Ensure all content coming from the client is using the same encoding; if not, the server-side application must canonicalize the data before applying any filtering.Implementation: Perform input validation for all remote content, including remote and user-generated contentImplementation: Perform output validation for all remote content.Implementation: Disable scripting languages such as JavaScript in browserImplementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
- **References:** https://capec.mitre.org/data/definitions/199.html, http://cwe.mitre.org/data/definitions/87.html

#### F069 (SC04) — XSS Using Alternate Syntax

- **Target:** Gemini API Gateway
- **Details:** An adversary uses alternate forms of keywords or commands that result in the same action as the primary form but which may not be caught by filters. For example, many keywords are processed in a case insensitive manner. If the site's web filtering algorithm does not convert all tags into a consistent case before the comparison with forbidden keywords it is possible to bypass filters (e.g., incomplete black lists) by using an alternate case structure. For example, the script tag using the alternate forms of Script or ScRiPt may bypass filters where script is the only form tested. Other variants using different syntax representations are also possible as well as using pollution meta-characters or entities that are eventually ignored by the rendering engine. The attack can result in the execution of otherwise prohibited functionality.
- **Mitigations:** Design: Use browser technologies that do not allow client side scripting.Design: Utilize strict type, character, and encoding enforcementImplementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.Implementation: Ensure all content coming from the client is using the same encoding; if not, the server-side application must canonicalize the data before applying any filtering.Implementation: Perform input validation for all remote content, including remote and user-generated contentImplementation: Perform output validation for all remote content.Implementation: Disable scripting languages such as JavaScript in browserImplementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
- **References:** https://capec.mitre.org/data/definitions/199.html, http://cwe.mitre.org/data/definitions/87.html

#### F181 (SC04) — XSS Using Alternate Syntax

- **Target:** Gemini LLM
- **Details:** An adversary uses alternate forms of keywords or commands that result in the same action as the primary form but which may not be caught by filters. For example, many keywords are processed in a case insensitive manner. If the site's web filtering algorithm does not convert all tags into a consistent case before the comparison with forbidden keywords it is possible to bypass filters (e.g., incomplete black lists) by using an alternate case structure. For example, the script tag using the alternate forms of Script or ScRiPt may bypass filters where script is the only form tested. Other variants using different syntax representations are also possible as well as using pollution meta-characters or entities that are eventually ignored by the rendering engine. The attack can result in the execution of otherwise prohibited functionality.
- **Mitigations:** Design: Use browser technologies that do not allow client side scripting.Design: Utilize strict type, character, and encoding enforcementImplementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.Implementation: Ensure all content coming from the client is using the same encoding; if not, the server-side application must canonicalize the data before applying any filtering.Implementation: Perform input validation for all remote content, including remote and user-generated contentImplementation: Perform output validation for all remote content.Implementation: Disable scripting languages such as JavaScript in browserImplementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
- **References:** https://capec.mitre.org/data/definitions/199.html, http://cwe.mitre.org/data/definitions/87.html

#### F025 (SC04) — XSS Using Alternate Syntax

- **Target:** Gemini SDK / REST Client
- **Details:** An adversary uses alternate forms of keywords or commands that result in the same action as the primary form but which may not be caught by filters. For example, many keywords are processed in a case insensitive manner. If the site's web filtering algorithm does not convert all tags into a consistent case before the comparison with forbidden keywords it is possible to bypass filters (e.g., incomplete black lists) by using an alternate case structure. For example, the script tag using the alternate forms of Script or ScRiPt may bypass filters where script is the only form tested. Other variants using different syntax representations are also possible as well as using pollution meta-characters or entities that are eventually ignored by the rendering engine. The attack can result in the execution of otherwise prohibited functionality.
- **Mitigations:** Design: Use browser technologies that do not allow client side scripting.Design: Utilize strict type, character, and encoding enforcementImplementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.Implementation: Ensure all content coming from the client is using the same encoding; if not, the server-side application must canonicalize the data before applying any filtering.Implementation: Perform input validation for all remote content, including remote and user-generated contentImplementation: Perform output validation for all remote content.Implementation: Disable scripting languages such as JavaScript in browserImplementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
- **References:** https://capec.mitre.org/data/definitions/199.html, http://cwe.mitre.org/data/definitions/87.html

#### F116 (SC05) — Removing Important Client Functionality

- **Target:** Auth & Billing Service
- **Details:** An attacker removes or disables functionality on the client that the server assumes to be present and trustworthy. Attackers can, in some cases, get around logic put in place to 'guard' sensitive functionality or data. Client applications may include functionality that a server relies on for correct and secure operation. This functionality can include, but is not limited to, filters to prevent the sending of dangerous content to the server, logical functionality such as price calculations, and authentication logic to ensure that only authorized users are utilizing the client. If an attacker can disable this functionality on the client, they can perform actions that the server believes are prohibited. This can result in client behavior that violates assumptions by the server leading to a variety of possible attacks. In the above examples, this could include the sending of dangerous content (such as scripts) to the server, incorrect price calculations, or unauthorized access to server resources.
- **Mitigations:** Design: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side.Design: Ship client-side application with integrity checks (code signing) when possible.Design: Use obfuscation and other techniques to prevent reverse engineering the client code.
- **References:** http://cwe.mitre.org/data/definitions/602.html

#### F072 (SC05) — Removing Important Client Functionality

- **Target:** Gemini API Gateway
- **Details:** An attacker removes or disables functionality on the client that the server assumes to be present and trustworthy. Attackers can, in some cases, get around logic put in place to 'guard' sensitive functionality or data. Client applications may include functionality that a server relies on for correct and secure operation. This functionality can include, but is not limited to, filters to prevent the sending of dangerous content to the server, logical functionality such as price calculations, and authentication logic to ensure that only authorized users are utilizing the client. If an attacker can disable this functionality on the client, they can perform actions that the server believes are prohibited. This can result in client behavior that violates assumptions by the server leading to a variety of possible attacks. In the above examples, this could include the sending of dangerous content (such as scripts) to the server, incorrect price calculations, or unauthorized access to server resources.
- **Mitigations:** Design: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side.Design: Ship client-side application with integrity checks (code signing) when possible.Design: Use obfuscation and other techniques to prevent reverse engineering the client code.
- **References:** http://cwe.mitre.org/data/definitions/602.html

#### F184 (SC05) — Removing Important Client Functionality

- **Target:** Gemini LLM
- **Details:** An attacker removes or disables functionality on the client that the server assumes to be present and trustworthy. Attackers can, in some cases, get around logic put in place to 'guard' sensitive functionality or data. Client applications may include functionality that a server relies on for correct and secure operation. This functionality can include, but is not limited to, filters to prevent the sending of dangerous content to the server, logical functionality such as price calculations, and authentication logic to ensure that only authorized users are utilizing the client. If an attacker can disable this functionality on the client, they can perform actions that the server believes are prohibited. This can result in client behavior that violates assumptions by the server leading to a variety of possible attacks. In the above examples, this could include the sending of dangerous content (such as scripts) to the server, incorrect price calculations, or unauthorized access to server resources.
- **Mitigations:** Design: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side.Design: Ship client-side application with integrity checks (code signing) when possible.Design: Use obfuscation and other techniques to prevent reverse engineering the client code.
- **References:** http://cwe.mitre.org/data/definitions/602.html

#### F028 (SC05) — Removing Important Client Functionality

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker removes or disables functionality on the client that the server assumes to be present and trustworthy. Attackers can, in some cases, get around logic put in place to 'guard' sensitive functionality or data. Client applications may include functionality that a server relies on for correct and secure operation. This functionality can include, but is not limited to, filters to prevent the sending of dangerous content to the server, logical functionality such as price calculations, and authentication logic to ensure that only authorized users are utilizing the client. If an attacker can disable this functionality on the client, they can perform actions that the server believes are prohibited. This can result in client behavior that violates assumptions by the server leading to a variety of possible attacks. In the above examples, this could include the sending of dangerous content (such as scripts) to the server, incorrect price calculations, or unauthorized access to server resources.
- **Mitigations:** Design: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side.Design: Ship client-side application with integrity checks (code signing) when possible.Design: Use obfuscation and other techniques to prevent reverse engineering the client code.
- **References:** http://cwe.mitre.org/data/definitions/602.html

### Severity: Medium

#### F091 (AA01) — Authentication Abuse/ByPass

- **Target:** Auth & Billing Service
- **Details:** An attacker obtains unauthorized access to an application, service or device either through knowledge of the inherent weaknesses of an authentication mechanism, or by exploiting a flaw in the authentication scheme's implementation. In such an attack an authentication mechanism is functioning but a carefully controlled sequence of events causes the mechanism to grant access to the attacker. This attack may exploit assumptions made by the target's authentication procedures, such as assumptions regarding trust relationships or assumptions regarding the generation of secret values. This attack differs from Authentication Bypass attacks in that Authentication Abuse allows the attacker to be certified as a valid user through illegitimate means, while Authentication Bypass allows the user to access protected material without ever being certified as an authenticated user. This attack does not rely on prior sessions established by successfully authenticating users, as relied upon for the Exploitation of Session Variables, Resource IDs and other Trusted Credentials attack patterns.
- **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
- **References:** https://capec.mitre.org/data/definitions/114.html, http://cwe.mitre.org/data/definitions/287.html

#### F047 (AA01) — Authentication Abuse/ByPass

- **Target:** Gemini API Gateway
- **Details:** An attacker obtains unauthorized access to an application, service or device either through knowledge of the inherent weaknesses of an authentication mechanism, or by exploiting a flaw in the authentication scheme's implementation. In such an attack an authentication mechanism is functioning but a carefully controlled sequence of events causes the mechanism to grant access to the attacker. This attack may exploit assumptions made by the target's authentication procedures, such as assumptions regarding trust relationships or assumptions regarding the generation of secret values. This attack differs from Authentication Bypass attacks in that Authentication Abuse allows the attacker to be certified as a valid user through illegitimate means, while Authentication Bypass allows the user to access protected material without ever being certified as an authenticated user. This attack does not rely on prior sessions established by successfully authenticating users, as relied upon for the Exploitation of Session Variables, Resource IDs and other Trusted Credentials attack patterns.
- **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
- **References:** https://capec.mitre.org/data/definitions/114.html, http://cwe.mitre.org/data/definitions/287.html

#### F159 (AA01) — Authentication Abuse/ByPass

- **Target:** Gemini LLM
- **Details:** An attacker obtains unauthorized access to an application, service or device either through knowledge of the inherent weaknesses of an authentication mechanism, or by exploiting a flaw in the authentication scheme's implementation. In such an attack an authentication mechanism is functioning but a carefully controlled sequence of events causes the mechanism to grant access to the attacker. This attack may exploit assumptions made by the target's authentication procedures, such as assumptions regarding trust relationships or assumptions regarding the generation of secret values. This attack differs from Authentication Bypass attacks in that Authentication Abuse allows the attacker to be certified as a valid user through illegitimate means, while Authentication Bypass allows the user to access protected material without ever being certified as an authenticated user. This attack does not rely on prior sessions established by successfully authenticating users, as relied upon for the Exploitation of Session Variables, Resource IDs and other Trusted Credentials attack patterns.
- **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
- **References:** https://capec.mitre.org/data/definitions/114.html, http://cwe.mitre.org/data/definitions/287.html

#### F003 (AA01) — Authentication Abuse/ByPass

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker obtains unauthorized access to an application, service or device either through knowledge of the inherent weaknesses of an authentication mechanism, or by exploiting a flaw in the authentication scheme's implementation. In such an attack an authentication mechanism is functioning but a carefully controlled sequence of events causes the mechanism to grant access to the attacker. This attack may exploit assumptions made by the target's authentication procedures, such as assumptions regarding trust relationships or assumptions regarding the generation of secret values. This attack differs from Authentication Bypass attacks in that Authentication Abuse allows the attacker to be certified as a valid user through illegitimate means, while Authentication Bypass allows the user to access protected material without ever being certified as an authenticated user. This attack does not rely on prior sessions established by successfully authenticating users, as relied upon for the Exploitation of Session Variables, Resource IDs and other Trusted Credentials attack patterns.
- **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
- **References:** https://capec.mitre.org/data/definitions/114.html, http://cwe.mitre.org/data/definitions/287.html

#### F111 (AA02) — Principal Spoof

- **Target:** Auth & Billing Service
- **Details:** A Principal Spoof is a form of Identity Spoofing where an adversary pretends to be some other person in an interaction. This is often accomplished by crafting a message (either written, verbal, or visual) that appears to come from a person other than the adversary. Phishing and Pharming attacks often attempt to do this so that their attempts to gather sensitive information appear to come from a legitimate source. A Principal Spoof does not use stolen or spoofed authentication credentials, instead relying on the appearance and content of the message to reflect identity. The possible outcomes of a Principal Spoof mirror those of Identity Spoofing. (e.g., escalation of privilege and false attribution of data or activities) Likewise, most techniques for Identity Spoofing (crafting messages or intercepting and replaying or modifying messages) can be used for a Principal Spoof attack. However, because a Principal Spoof is used to impersonate a person, social engineering can be both an attack technique (using social techniques to generate evidence in support of a false identity) as well as a possible outcome (manipulating people's perceptions by making statements or performing actions under a target's name).
- **Mitigations:** Employ robust authentication processes (e.g., multi-factor authentication).
- **References:** https://capec.mitre.org/data/definitions/195.html

#### F067 (AA02) — Principal Spoof

- **Target:** Gemini API Gateway
- **Details:** A Principal Spoof is a form of Identity Spoofing where an adversary pretends to be some other person in an interaction. This is often accomplished by crafting a message (either written, verbal, or visual) that appears to come from a person other than the adversary. Phishing and Pharming attacks often attempt to do this so that their attempts to gather sensitive information appear to come from a legitimate source. A Principal Spoof does not use stolen or spoofed authentication credentials, instead relying on the appearance and content of the message to reflect identity. The possible outcomes of a Principal Spoof mirror those of Identity Spoofing. (e.g., escalation of privilege and false attribution of data or activities) Likewise, most techniques for Identity Spoofing (crafting messages or intercepting and replaying or modifying messages) can be used for a Principal Spoof attack. However, because a Principal Spoof is used to impersonate a person, social engineering can be both an attack technique (using social techniques to generate evidence in support of a false identity) as well as a possible outcome (manipulating people's perceptions by making statements or performing actions under a target's name).
- **Mitigations:** Employ robust authentication processes (e.g., multi-factor authentication).
- **References:** https://capec.mitre.org/data/definitions/195.html

#### F179 (AA02) — Principal Spoof

- **Target:** Gemini LLM
- **Details:** A Principal Spoof is a form of Identity Spoofing where an adversary pretends to be some other person in an interaction. This is often accomplished by crafting a message (either written, verbal, or visual) that appears to come from a person other than the adversary. Phishing and Pharming attacks often attempt to do this so that their attempts to gather sensitive information appear to come from a legitimate source. A Principal Spoof does not use stolen or spoofed authentication credentials, instead relying on the appearance and content of the message to reflect identity. The possible outcomes of a Principal Spoof mirror those of Identity Spoofing. (e.g., escalation of privilege and false attribution of data or activities) Likewise, most techniques for Identity Spoofing (crafting messages or intercepting and replaying or modifying messages) can be used for a Principal Spoof attack. However, because a Principal Spoof is used to impersonate a person, social engineering can be both an attack technique (using social techniques to generate evidence in support of a false identity) as well as a possible outcome (manipulating people's perceptions by making statements or performing actions under a target's name).
- **Mitigations:** Employ robust authentication processes (e.g., multi-factor authentication).
- **References:** https://capec.mitre.org/data/definitions/195.html

#### F023 (AA02) — Principal Spoof

- **Target:** Gemini SDK / REST Client
- **Details:** A Principal Spoof is a form of Identity Spoofing where an adversary pretends to be some other person in an interaction. This is often accomplished by crafting a message (either written, verbal, or visual) that appears to come from a person other than the adversary. Phishing and Pharming attacks often attempt to do this so that their attempts to gather sensitive information appear to come from a legitimate source. A Principal Spoof does not use stolen or spoofed authentication credentials, instead relying on the appearance and content of the message to reflect identity. The possible outcomes of a Principal Spoof mirror those of Identity Spoofing. (e.g., escalation of privilege and false attribution of data or activities) Likewise, most techniques for Identity Spoofing (crafting messages or intercepting and replaying or modifying messages) can be used for a Principal Spoof attack. However, because a Principal Spoof is used to impersonate a person, social engineering can be both an attack technique (using social techniques to generate evidence in support of a false identity) as well as a possible outcome (manipulating people's perceptions by making statements or performing actions under a target's name).
- **Mitigations:** Employ robust authentication processes (e.g., multi-factor authentication).
- **References:** https://capec.mitre.org/data/definitions/195.html

#### F094 (AC01) — Privilege Abuse

- **Target:** Auth & Billing Service
- **Details:** An adversary is able to exploit features of the target that should be reserved for privileged users or administrators but are exposed to use by lower or non-privileged accounts. Access to sensitive information and functionality must be controlled to ensure that only authorized users are able to access these resources. If access control mechanisms are absent or misconfigured, a user may be able to access resources that are intended only for higher level users. An adversary may be able to exploit this to utilize a less trusted account to gain information and perform activities reserved for more trusted accounts. This attack differs from privilege escalation and other privilege stealing attacks in that the adversary never actually escalates their privileges but instead is able to use a lesser degree of privilege to access resources that should be (but are not) reserved for higher privilege accounts. Likewise, the adversary does not exploit trust or subvert systems - all control functionality is working as configured but the configuration does not adequately protect sensitive resources at an appropriate level.
- **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
- **References:** https://capec.mitre.org/data/definitions/122.html, http://cwe.mitre.org/data/definitions/732.html, http://cwe.mitre.org/data/definitions/269.html

#### F050 (AC01) — Privilege Abuse

- **Target:** Gemini API Gateway
- **Details:** An adversary is able to exploit features of the target that should be reserved for privileged users or administrators but are exposed to use by lower or non-privileged accounts. Access to sensitive information and functionality must be controlled to ensure that only authorized users are able to access these resources. If access control mechanisms are absent or misconfigured, a user may be able to access resources that are intended only for higher level users. An adversary may be able to exploit this to utilize a less trusted account to gain information and perform activities reserved for more trusted accounts. This attack differs from privilege escalation and other privilege stealing attacks in that the adversary never actually escalates their privileges but instead is able to use a lesser degree of privilege to access resources that should be (but are not) reserved for higher privilege accounts. Likewise, the adversary does not exploit trust or subvert systems - all control functionality is working as configured but the configuration does not adequately protect sensitive resources at an appropriate level.
- **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
- **References:** https://capec.mitre.org/data/definitions/122.html, http://cwe.mitre.org/data/definitions/732.html, http://cwe.mitre.org/data/definitions/269.html

#### F162 (AC01) — Privilege Abuse

- **Target:** Gemini LLM
- **Details:** An adversary is able to exploit features of the target that should be reserved for privileged users or administrators but are exposed to use by lower or non-privileged accounts. Access to sensitive information and functionality must be controlled to ensure that only authorized users are able to access these resources. If access control mechanisms are absent or misconfigured, a user may be able to access resources that are intended only for higher level users. An adversary may be able to exploit this to utilize a less trusted account to gain information and perform activities reserved for more trusted accounts. This attack differs from privilege escalation and other privilege stealing attacks in that the adversary never actually escalates their privileges but instead is able to use a lesser degree of privilege to access resources that should be (but are not) reserved for higher privilege accounts. Likewise, the adversary does not exploit trust or subvert systems - all control functionality is working as configured but the configuration does not adequately protect sensitive resources at an appropriate level.
- **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
- **References:** https://capec.mitre.org/data/definitions/122.html, http://cwe.mitre.org/data/definitions/732.html, http://cwe.mitre.org/data/definitions/269.html

#### F006 (AC01) — Privilege Abuse

- **Target:** Gemini SDK / REST Client
- **Details:** An adversary is able to exploit features of the target that should be reserved for privileged users or administrators but are exposed to use by lower or non-privileged accounts. Access to sensitive information and functionality must be controlled to ensure that only authorized users are able to access these resources. If access control mechanisms are absent or misconfigured, a user may be able to access resources that are intended only for higher level users. An adversary may be able to exploit this to utilize a less trusted account to gain information and perform activities reserved for more trusted accounts. This attack differs from privilege escalation and other privilege stealing attacks in that the adversary never actually escalates their privileges but instead is able to use a lesser degree of privilege to access resources that should be (but are not) reserved for higher privilege accounts. Likewise, the adversary does not exploit trust or subvert systems - all control functionality is working as configured but the configuration does not adequately protect sensitive resources at an appropriate level.
- **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
- **References:** https://capec.mitre.org/data/definitions/122.html, http://cwe.mitre.org/data/definitions/732.html, http://cwe.mitre.org/data/definitions/269.html

#### F133 (AC01) — Privilege Abuse

- **Target:** User File Store
- **Details:** An adversary is able to exploit features of the target that should be reserved for privileged users or administrators but are exposed to use by lower or non-privileged accounts. Access to sensitive information and functionality must be controlled to ensure that only authorized users are able to access these resources. If access control mechanisms are absent or misconfigured, a user may be able to access resources that are intended only for higher level users. An adversary may be able to exploit this to utilize a less trusted account to gain information and perform activities reserved for more trusted accounts. This attack differs from privilege escalation and other privilege stealing attacks in that the adversary never actually escalates their privileges but instead is able to use a lesser degree of privilege to access resources that should be (but are not) reserved for higher privilege accounts. Likewise, the adversary does not exploit trust or subvert systems - all control functionality is working as configured but the configuration does not adequately protect sensitive resources at an appropriate level.
- **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
- **References:** https://capec.mitre.org/data/definitions/122.html, http://cwe.mitre.org/data/definitions/732.html, http://cwe.mitre.org/data/definitions/269.html

#### F145 (AC01) — Privilege Abuse

- **Target:** Vector Store
- **Details:** An adversary is able to exploit features of the target that should be reserved for privileged users or administrators but are exposed to use by lower or non-privileged accounts. Access to sensitive information and functionality must be controlled to ensure that only authorized users are able to access these resources. If access control mechanisms are absent or misconfigured, a user may be able to access resources that are intended only for higher level users. An adversary may be able to exploit this to utilize a less trusted account to gain information and perform activities reserved for more trusted accounts. This attack differs from privilege escalation and other privilege stealing attacks in that the adversary never actually escalates their privileges but instead is able to use a lesser degree of privilege to access resources that should be (but are not) reserved for higher privilege accounts. Likewise, the adversary does not exploit trust or subvert systems - all control functionality is working as configured but the configuration does not adequately protect sensitive resources at an appropriate level.
- **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
- **References:** https://capec.mitre.org/data/definitions/122.html, http://cwe.mitre.org/data/definitions/732.html, http://cwe.mitre.org/data/definitions/269.html

#### F202 (AC05) — Content Spoofing

- **Target:** API key/token
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F267 (AC05) — Content Spoofing

- **Target:** API response
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F257 (AC05) — Content Spoofing

- **Target:** Context + prompt
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F272 (AC05) — Content Spoofing

- **Target:** Display response
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F217 (AC05) — Content Spoofing

- **Target:** File to API
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F212 (AC05) — Content Spoofing

- **Target:** File upload
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F262 (AC05) — Content Spoofing

- **Target:** LLM response
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F242 (AC05) — Content Spoofing

- **Target:** Prompt to API
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F247 (AC05) — Content Spoofing

- **Target:** Query vectors
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F252 (AC05) — Content Spoofing

- **Target:** Relevant chunks
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F222 (AC05) — Content Spoofing

- **Target:** Store file
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F232 (AC05) — Content Spoofing

- **Target:** Store vectors
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F207 (AC05) — Content Spoofing

- **Target:** Token validation
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F227 (AC05) — Content Spoofing

- **Target:** Trigger embedding
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F237 (AC05) — Content Spoofing

- **Target:** User prompt
- **Details:** An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
- **References:** https://capec.mitre.org/data/definitions/148.html, http://cwe.mitre.org/data/definitions/345.html, https://cwe.mitre.org/data/definitions/299.html

#### F108 (AC07) — Exploiting Incorrectly Configured Access Control Security Levels

- **Target:** Auth & Billing Service
- **Details:** An attacker exploits a weakness in the configuration of access controls and is able to bypass the intended protection that these measures guard against and thereby obtain unauthorized access to the system or network. Sensitive functionality should always be protected with access controls. However configuring all but the most trivial access control systems can be very complicated and there are many opportunities for mistakes. If an attacker can learn of incorrectly configured access security settings, they may be able to exploit this in an attack. Most commonly, attackers would take advantage of controls that provided too little protection for sensitive activities in order to perform actions that should be denied to them. In some circumstances, an attacker may be able to take advantage of overly restrictive access control policies, initiating denial of services (if an application locks because it unexpectedly failed to be granted access) or causing other legitimate actions to fail due to security. The latter class of attacks, however, is usually less severe and easier to detect than attacks based on inadequate security restrictions. This attack pattern differs from CAPEC 1, Accessing Functionality Not Properly Constrained by ACLs in that the latter describes attacks where sensitive functionality lacks access controls, where, in this pattern, the access control is present, but incorrectly configured.
- **Mitigations:** Design: Configure the access control correctly.
- **References:** https://capec.mitre.org/data/definitions/180.html, http://cwe.mitre.org/data/definitions/732.html

#### F064 (AC07) — Exploiting Incorrectly Configured Access Control Security Levels

- **Target:** Gemini API Gateway
- **Details:** An attacker exploits a weakness in the configuration of access controls and is able to bypass the intended protection that these measures guard against and thereby obtain unauthorized access to the system or network. Sensitive functionality should always be protected with access controls. However configuring all but the most trivial access control systems can be very complicated and there are many opportunities for mistakes. If an attacker can learn of incorrectly configured access security settings, they may be able to exploit this in an attack. Most commonly, attackers would take advantage of controls that provided too little protection for sensitive activities in order to perform actions that should be denied to them. In some circumstances, an attacker may be able to take advantage of overly restrictive access control policies, initiating denial of services (if an application locks because it unexpectedly failed to be granted access) or causing other legitimate actions to fail due to security. The latter class of attacks, however, is usually less severe and easier to detect than attacks based on inadequate security restrictions. This attack pattern differs from CAPEC 1, Accessing Functionality Not Properly Constrained by ACLs in that the latter describes attacks where sensitive functionality lacks access controls, where, in this pattern, the access control is present, but incorrectly configured.
- **Mitigations:** Design: Configure the access control correctly.
- **References:** https://capec.mitre.org/data/definitions/180.html, http://cwe.mitre.org/data/definitions/732.html

#### F176 (AC07) — Exploiting Incorrectly Configured Access Control Security Levels

- **Target:** Gemini LLM
- **Details:** An attacker exploits a weakness in the configuration of access controls and is able to bypass the intended protection that these measures guard against and thereby obtain unauthorized access to the system or network. Sensitive functionality should always be protected with access controls. However configuring all but the most trivial access control systems can be very complicated and there are many opportunities for mistakes. If an attacker can learn of incorrectly configured access security settings, they may be able to exploit this in an attack. Most commonly, attackers would take advantage of controls that provided too little protection for sensitive activities in order to perform actions that should be denied to them. In some circumstances, an attacker may be able to take advantage of overly restrictive access control policies, initiating denial of services (if an application locks because it unexpectedly failed to be granted access) or causing other legitimate actions to fail due to security. The latter class of attacks, however, is usually less severe and easier to detect than attacks based on inadequate security restrictions. This attack pattern differs from CAPEC 1, Accessing Functionality Not Properly Constrained by ACLs in that the latter describes attacks where sensitive functionality lacks access controls, where, in this pattern, the access control is present, but incorrectly configured.
- **Mitigations:** Design: Configure the access control correctly.
- **References:** https://capec.mitre.org/data/definitions/180.html, http://cwe.mitre.org/data/definitions/732.html

#### F020 (AC07) — Exploiting Incorrectly Configured Access Control Security Levels

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker exploits a weakness in the configuration of access controls and is able to bypass the intended protection that these measures guard against and thereby obtain unauthorized access to the system or network. Sensitive functionality should always be protected with access controls. However configuring all but the most trivial access control systems can be very complicated and there are many opportunities for mistakes. If an attacker can learn of incorrectly configured access security settings, they may be able to exploit this in an attack. Most commonly, attackers would take advantage of controls that provided too little protection for sensitive activities in order to perform actions that should be denied to them. In some circumstances, an attacker may be able to take advantage of overly restrictive access control policies, initiating denial of services (if an application locks because it unexpectedly failed to be granted access) or causing other legitimate actions to fail due to security. The latter class of attacks, however, is usually less severe and easier to detect than attacks based on inadequate security restrictions. This attack pattern differs from CAPEC 1, Accessing Functionality Not Properly Constrained by ACLs in that the latter describes attacks where sensitive functionality lacks access controls, where, in this pattern, the access control is present, but incorrectly configured.
- **Mitigations:** Design: Configure the access control correctly.
- **References:** https://capec.mitre.org/data/definitions/180.html, http://cwe.mitre.org/data/definitions/732.html

#### F115 (AC08) — Manipulate Registry Information

- **Target:** Auth & Billing Service
- **Details:** An adversary exploits a weakness in authorization in order to modify content within a registry (e.g., Windows Registry, Mac plist, application registry). Editing registry information can permit the adversary to hide configuration information or remove indicators of compromise to cover up activity. Many applications utilize registries to store configuration and service information. As such, modification of registry information can affect individual services (affecting billing, authorization, or even allowing for identity spoofing) or the overall configuration of a targeted application. For example, both Java RMI and SOAP use registries to track available services. Changing registry values is sometimes a preliminary step towards completing another attack pattern, but given the long term usage of many registry values, manipulation of registry information could be its own end.
- **Mitigations:** Ensure proper permissions are set for Registry hives to prevent users from modifying keys.Employ a robust and layered defensive posture in order to prevent unauthorized users on your system.Employ robust identification and audit/blocking via whitelisting of applications on your system. Unnecessary applications, utilities, and configurations will have a presence in the system registry that can be leveraged by an adversary through this attack pattern.
- **References:** https://capec.mitre.org/data/definitions/203.html, http://cwe.mitre.org/data/definitions/15.html

#### F071 (AC08) — Manipulate Registry Information

- **Target:** Gemini API Gateway
- **Details:** An adversary exploits a weakness in authorization in order to modify content within a registry (e.g., Windows Registry, Mac plist, application registry). Editing registry information can permit the adversary to hide configuration information or remove indicators of compromise to cover up activity. Many applications utilize registries to store configuration and service information. As such, modification of registry information can affect individual services (affecting billing, authorization, or even allowing for identity spoofing) or the overall configuration of a targeted application. For example, both Java RMI and SOAP use registries to track available services. Changing registry values is sometimes a preliminary step towards completing another attack pattern, but given the long term usage of many registry values, manipulation of registry information could be its own end.
- **Mitigations:** Ensure proper permissions are set for Registry hives to prevent users from modifying keys.Employ a robust and layered defensive posture in order to prevent unauthorized users on your system.Employ robust identification and audit/blocking via whitelisting of applications on your system. Unnecessary applications, utilities, and configurations will have a presence in the system registry that can be leveraged by an adversary through this attack pattern.
- **References:** https://capec.mitre.org/data/definitions/203.html, http://cwe.mitre.org/data/definitions/15.html

#### F183 (AC08) — Manipulate Registry Information

- **Target:** Gemini LLM
- **Details:** An adversary exploits a weakness in authorization in order to modify content within a registry (e.g., Windows Registry, Mac plist, application registry). Editing registry information can permit the adversary to hide configuration information or remove indicators of compromise to cover up activity. Many applications utilize registries to store configuration and service information. As such, modification of registry information can affect individual services (affecting billing, authorization, or even allowing for identity spoofing) or the overall configuration of a targeted application. For example, both Java RMI and SOAP use registries to track available services. Changing registry values is sometimes a preliminary step towards completing another attack pattern, but given the long term usage of many registry values, manipulation of registry information could be its own end.
- **Mitigations:** Ensure proper permissions are set for Registry hives to prevent users from modifying keys.Employ a robust and layered defensive posture in order to prevent unauthorized users on your system.Employ robust identification and audit/blocking via whitelisting of applications on your system. Unnecessary applications, utilities, and configurations will have a presence in the system registry that can be leveraged by an adversary through this attack pattern.
- **References:** https://capec.mitre.org/data/definitions/203.html, http://cwe.mitre.org/data/definitions/15.html

#### F027 (AC08) — Manipulate Registry Information

- **Target:** Gemini SDK / REST Client
- **Details:** An adversary exploits a weakness in authorization in order to modify content within a registry (e.g., Windows Registry, Mac plist, application registry). Editing registry information can permit the adversary to hide configuration information or remove indicators of compromise to cover up activity. Many applications utilize registries to store configuration and service information. As such, modification of registry information can affect individual services (affecting billing, authorization, or even allowing for identity spoofing) or the overall configuration of a targeted application. For example, both Java RMI and SOAP use registries to track available services. Changing registry values is sometimes a preliminary step towards completing another attack pattern, but given the long term usage of many registry values, manipulation of registry information could be its own end.
- **Mitigations:** Ensure proper permissions are set for Registry hives to prevent users from modifying keys.Employ a robust and layered defensive posture in order to prevent unauthorized users on your system.Employ robust identification and audit/blocking via whitelisting of applications on your system. Unnecessary applications, utilities, and configurations will have a presence in the system registry that can be leveraged by an adversary through this attack pattern.
- **References:** https://capec.mitre.org/data/definitions/203.html, http://cwe.mitre.org/data/definitions/15.html

#### F119 (AC09) — Functionality Misuse

- **Target:** Auth & Billing Service
- **Details:** An adversary leverages a legitimate capability of an application in such a way as to achieve a negative technical impact. The system functionality is not altered or modified but used in a way that was not intended. This is often accomplished through the overuse of a specific functionality or by leveraging functionality with design flaws that enables the adversary to gain access to unauthorized, sensitive data.
- **Mitigations:** Perform comprehensive threat modeling, a process of identifying, evaluating, and mitigating potential threats to the application. This effort can help reveal potentially obscure application functionality that can be manipulated for malicious purposes.When implementing security features, consider how they can be misused and compromised.
- **References:** https://capec.mitre.org/data/definitions/212.html

#### F075 (AC09) — Functionality Misuse

- **Target:** Gemini API Gateway
- **Details:** An adversary leverages a legitimate capability of an application in such a way as to achieve a negative technical impact. The system functionality is not altered or modified but used in a way that was not intended. This is often accomplished through the overuse of a specific functionality or by leveraging functionality with design flaws that enables the adversary to gain access to unauthorized, sensitive data.
- **Mitigations:** Perform comprehensive threat modeling, a process of identifying, evaluating, and mitigating potential threats to the application. This effort can help reveal potentially obscure application functionality that can be manipulated for malicious purposes.When implementing security features, consider how they can be misused and compromised.
- **References:** https://capec.mitre.org/data/definitions/212.html

#### F187 (AC09) — Functionality Misuse

- **Target:** Gemini LLM
- **Details:** An adversary leverages a legitimate capability of an application in such a way as to achieve a negative technical impact. The system functionality is not altered or modified but used in a way that was not intended. This is often accomplished through the overuse of a specific functionality or by leveraging functionality with design flaws that enables the adversary to gain access to unauthorized, sensitive data.
- **Mitigations:** Perform comprehensive threat modeling, a process of identifying, evaluating, and mitigating potential threats to the application. This effort can help reveal potentially obscure application functionality that can be manipulated for malicious purposes.When implementing security features, consider how they can be misused and compromised.
- **References:** https://capec.mitre.org/data/definitions/212.html

#### F031 (AC09) — Functionality Misuse

- **Target:** Gemini SDK / REST Client
- **Details:** An adversary leverages a legitimate capability of an application in such a way as to achieve a negative technical impact. The system functionality is not altered or modified but used in a way that was not intended. This is often accomplished through the overuse of a specific functionality or by leveraging functionality with design flaws that enables the adversary to gain access to unauthorized, sensitive data.
- **Mitigations:** Perform comprehensive threat modeling, a process of identifying, evaluating, and mitigating potential threats to the application. This effort can help reveal potentially obscure application functionality that can be manipulated for malicious purposes.When implementing security features, consider how they can be misused and compromised.
- **References:** https://capec.mitre.org/data/definitions/212.html

#### F123 (AC11) — Session Credential Falsification through Manipulation

- **Target:** Auth & Billing Service
- **Details:** An attacker manipulates an existing credential in order to gain access to a target application. Session credentials allow users to identify themselves to a service after an initial authentication without needing to resend the authentication information (usually a username and password) with every message. An attacker may be able to manipulate a credential sniffed from an existing connection in order to gain access to a target server. For example, a credential in the form of a web cookie might have a field that indicates the access rights of a user. By manually tweaking this cookie, a user might be able to increase their access rights to the server. Alternately an attacker may be able to manipulate an existing credential to appear as a different user. This attack differs from falsification through prediction in that the user bases their modified credentials off existing credentials instead of using patterns detected in prior credentials to create a new credential that is accepted because it fits the pattern. As a result, an attacker may be able to impersonate other users or elevate their permissions to a targeted service.
- **Mitigations:** Implementation: Use session IDs that are difficult to guess or brute-force: One way for the attackers to obtain valid session IDs is by brute-forcing or guessing them. By choosing session identifiers that are sufficiently random, brute-forcing or guessing becomes very difficult. Implementation: Regenerate and destroy session identifiers when there is a change in the level of privilege: This ensures that even though a potential victim may have followed a link with a fixated identifier, a new one is issued when the level of privilege changes.
- **References:** https://capec.mitre.org/data/definitions/226.html, http://cwe.mitre.org/data/definitions/565.html, http://cwe.mitre.org/data/definitions/472.html

#### F079 (AC11) — Session Credential Falsification through Manipulation

- **Target:** Gemini API Gateway
- **Details:** An attacker manipulates an existing credential in order to gain access to a target application. Session credentials allow users to identify themselves to a service after an initial authentication without needing to resend the authentication information (usually a username and password) with every message. An attacker may be able to manipulate a credential sniffed from an existing connection in order to gain access to a target server. For example, a credential in the form of a web cookie might have a field that indicates the access rights of a user. By manually tweaking this cookie, a user might be able to increase their access rights to the server. Alternately an attacker may be able to manipulate an existing credential to appear as a different user. This attack differs from falsification through prediction in that the user bases their modified credentials off existing credentials instead of using patterns detected in prior credentials to create a new credential that is accepted because it fits the pattern. As a result, an attacker may be able to impersonate other users or elevate their permissions to a targeted service.
- **Mitigations:** Implementation: Use session IDs that are difficult to guess or brute-force: One way for the attackers to obtain valid session IDs is by brute-forcing or guessing them. By choosing session identifiers that are sufficiently random, brute-forcing or guessing becomes very difficult. Implementation: Regenerate and destroy session identifiers when there is a change in the level of privilege: This ensures that even though a potential victim may have followed a link with a fixated identifier, a new one is issued when the level of privilege changes.
- **References:** https://capec.mitre.org/data/definitions/226.html, http://cwe.mitre.org/data/definitions/565.html, http://cwe.mitre.org/data/definitions/472.html

#### F191 (AC11) — Session Credential Falsification through Manipulation

- **Target:** Gemini LLM
- **Details:** An attacker manipulates an existing credential in order to gain access to a target application. Session credentials allow users to identify themselves to a service after an initial authentication without needing to resend the authentication information (usually a username and password) with every message. An attacker may be able to manipulate a credential sniffed from an existing connection in order to gain access to a target server. For example, a credential in the form of a web cookie might have a field that indicates the access rights of a user. By manually tweaking this cookie, a user might be able to increase their access rights to the server. Alternately an attacker may be able to manipulate an existing credential to appear as a different user. This attack differs from falsification through prediction in that the user bases their modified credentials off existing credentials instead of using patterns detected in prior credentials to create a new credential that is accepted because it fits the pattern. As a result, an attacker may be able to impersonate other users or elevate their permissions to a targeted service.
- **Mitigations:** Implementation: Use session IDs that are difficult to guess or brute-force: One way for the attackers to obtain valid session IDs is by brute-forcing or guessing them. By choosing session identifiers that are sufficiently random, brute-forcing or guessing becomes very difficult. Implementation: Regenerate and destroy session identifiers when there is a change in the level of privilege: This ensures that even though a potential victim may have followed a link with a fixated identifier, a new one is issued when the level of privilege changes.
- **References:** https://capec.mitre.org/data/definitions/226.html, http://cwe.mitre.org/data/definitions/565.html, http://cwe.mitre.org/data/definitions/472.html

#### F035 (AC11) — Session Credential Falsification through Manipulation

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker manipulates an existing credential in order to gain access to a target application. Session credentials allow users to identify themselves to a service after an initial authentication without needing to resend the authentication information (usually a username and password) with every message. An attacker may be able to manipulate a credential sniffed from an existing connection in order to gain access to a target server. For example, a credential in the form of a web cookie might have a field that indicates the access rights of a user. By manually tweaking this cookie, a user might be able to increase their access rights to the server. Alternately an attacker may be able to manipulate an existing credential to appear as a different user. This attack differs from falsification through prediction in that the user bases their modified credentials off existing credentials instead of using patterns detected in prior credentials to create a new credential that is accepted because it fits the pattern. As a result, an attacker may be able to impersonate other users or elevate their permissions to a targeted service.
- **Mitigations:** Implementation: Use session IDs that are difficult to guess or brute-force: One way for the attackers to obtain valid session IDs is by brute-forcing or guessing them. By choosing session identifiers that are sufficiently random, brute-forcing or guessing becomes very difficult. Implementation: Regenerate and destroy session identifiers when there is a change in the level of privilege: This ensures that even though a potential victim may have followed a link with a fixated identifier, a new one is issued when the level of privilege changes.
- **References:** https://capec.mitre.org/data/definitions/226.html, http://cwe.mitre.org/data/definitions/565.html, http://cwe.mitre.org/data/definitions/472.html

#### F205 (CR08) — Client-Server Protocol Manipulation

- **Target:** API key/token
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F270 (CR08) — Client-Server Protocol Manipulation

- **Target:** API response
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F260 (CR08) — Client-Server Protocol Manipulation

- **Target:** Context + prompt
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F275 (CR08) — Client-Server Protocol Manipulation

- **Target:** Display response
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F220 (CR08) — Client-Server Protocol Manipulation

- **Target:** File to API
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F215 (CR08) — Client-Server Protocol Manipulation

- **Target:** File upload
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F265 (CR08) — Client-Server Protocol Manipulation

- **Target:** LLM response
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F245 (CR08) — Client-Server Protocol Manipulation

- **Target:** Prompt to API
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F250 (CR08) — Client-Server Protocol Manipulation

- **Target:** Query vectors
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F255 (CR08) — Client-Server Protocol Manipulation

- **Target:** Relevant chunks
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F225 (CR08) — Client-Server Protocol Manipulation

- **Target:** Store file
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F235 (CR08) — Client-Server Protocol Manipulation

- **Target:** Store vectors
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F210 (CR08) — Client-Server Protocol Manipulation

- **Target:** Token validation
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F230 (CR08) — Client-Server Protocol Manipulation

- **Target:** Trigger embedding
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F240 (CR08) — Client-Server Protocol Manipulation

- **Target:** User prompt
- **Details:** An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions. For example, an authentication protocol might be used to establish the identities of the server and client while a separate messaging protocol might be used to exchange data. If there is a weakness in a protocol used by the client and server, an attacker might take advantage of this to perform various types of attacks. For example, if the attacker is able to manipulate an authentication protocol, the attacker may be able spoof other clients or servers. If the attacker is able to manipulate a messaging protocol, the may be able to read sensitive information or modify message contents. This attack is often made easier by the fact that many clients and servers support multiple protocols to perform similar roles. For example, a server might support several different authentication protocols in order to support a wide range of clients, including legacy clients. Some of the older protocols may have vulnerabilities that allow an attacker to manipulate client-server interactions.
- **Mitigations:** Use strong authentication protocols.
- **References:** https://capec.mitre.org/data/definitions/220.html, http://cwe.mitre.org/data/definitions/757.html

#### F201 (DE01) — Interception

- **Target:** API key/token
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F266 (DE01) — Interception

- **Target:** API response
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F256 (DE01) — Interception

- **Target:** Context + prompt
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F271 (DE01) — Interception

- **Target:** Display response
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F216 (DE01) — Interception

- **Target:** File to API
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F211 (DE01) — Interception

- **Target:** File upload
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F261 (DE01) — Interception

- **Target:** LLM response
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F241 (DE01) — Interception

- **Target:** Prompt to API
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F246 (DE01) — Interception

- **Target:** Query vectors
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F251 (DE01) — Interception

- **Target:** Relevant chunks
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F221 (DE01) — Interception

- **Target:** Store file
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F231 (DE01) — Interception

- **Target:** Store vectors
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F206 (DE01) — Interception

- **Target:** Token validation
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F226 (DE01) — Interception

- **Target:** Trigger embedding
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F236 (DE01) — Interception

- **Target:** User prompt
- **Details:** An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream, influence the nature of the data transmitted, or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position himself so as to observe explicit data channels (e.g. network traffic) and read the content.
- **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
- **References:** https://capec.mitre.org/data/definitions/117.html, http://cwe.mitre.org/data/definitions/319.html, https://cwe.mitre.org/data/definitions/299.html

#### F093 (DE02) — Double Encoding

- **Target:** Auth & Billing Service
- **Details:** The adversary utilizes a repeating of the encoding process for a set of characters (that is, character encoding a character encoding of a character) to obfuscate the payload of a particular request. This may allow the adversary to bypass filters that attempt to detect illegal characters or strings, such as those that might be used in traversal or injection attacks. Filters may be able to catch illegal encoded strings, but may not catch doubly encoded strings. For example, a dot (.), often used in path traversal attacks and therefore often blocked by filters, could be URL encoded as %2E. However, many filters recognize this encoding and would still block the request. In a double encoding, the % in the above URL encoding would be encoded again as %25, resulting in %252E which some filters might not catch, but which could still be interpreted as a dot (.) by interpreters on the target.
- **Mitigations:** Assume all input is malicious. Create a white list that defines all valid input to the software system based on the requirements specifications. Input that does not match against the white list should not be permitted to enter into the system. Test your decoding process against malicious input. Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding. When client input is required from web-based forms, avoid using the GET method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the POST method whenever possible. Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.Refer to the RFCs to safely decode URL. Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive. There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).
- **References:** https://capec.mitre.org/data/definitions/120.html, http://cwe.mitre.org/data/definitions/173.html, http://cwe.mitre.org/data/definitions/177.html

#### F049 (DE02) — Double Encoding

- **Target:** Gemini API Gateway
- **Details:** The adversary utilizes a repeating of the encoding process for a set of characters (that is, character encoding a character encoding of a character) to obfuscate the payload of a particular request. This may allow the adversary to bypass filters that attempt to detect illegal characters or strings, such as those that might be used in traversal or injection attacks. Filters may be able to catch illegal encoded strings, but may not catch doubly encoded strings. For example, a dot (.), often used in path traversal attacks and therefore often blocked by filters, could be URL encoded as %2E. However, many filters recognize this encoding and would still block the request. In a double encoding, the % in the above URL encoding would be encoded again as %25, resulting in %252E which some filters might not catch, but which could still be interpreted as a dot (.) by interpreters on the target.
- **Mitigations:** Assume all input is malicious. Create a white list that defines all valid input to the software system based on the requirements specifications. Input that does not match against the white list should not be permitted to enter into the system. Test your decoding process against malicious input. Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding. When client input is required from web-based forms, avoid using the GET method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the POST method whenever possible. Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.Refer to the RFCs to safely decode URL. Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive. There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).
- **References:** https://capec.mitre.org/data/definitions/120.html, http://cwe.mitre.org/data/definitions/173.html, http://cwe.mitre.org/data/definitions/177.html

#### F161 (DE02) — Double Encoding

- **Target:** Gemini LLM
- **Details:** The adversary utilizes a repeating of the encoding process for a set of characters (that is, character encoding a character encoding of a character) to obfuscate the payload of a particular request. This may allow the adversary to bypass filters that attempt to detect illegal characters or strings, such as those that might be used in traversal or injection attacks. Filters may be able to catch illegal encoded strings, but may not catch doubly encoded strings. For example, a dot (.), often used in path traversal attacks and therefore often blocked by filters, could be URL encoded as %2E. However, many filters recognize this encoding and would still block the request. In a double encoding, the % in the above URL encoding would be encoded again as %25, resulting in %252E which some filters might not catch, but which could still be interpreted as a dot (.) by interpreters on the target.
- **Mitigations:** Assume all input is malicious. Create a white list that defines all valid input to the software system based on the requirements specifications. Input that does not match against the white list should not be permitted to enter into the system. Test your decoding process against malicious input. Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding. When client input is required from web-based forms, avoid using the GET method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the POST method whenever possible. Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.Refer to the RFCs to safely decode URL. Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive. There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).
- **References:** https://capec.mitre.org/data/definitions/120.html, http://cwe.mitre.org/data/definitions/173.html, http://cwe.mitre.org/data/definitions/177.html

#### F005 (DE02) — Double Encoding

- **Target:** Gemini SDK / REST Client
- **Details:** The adversary utilizes a repeating of the encoding process for a set of characters (that is, character encoding a character encoding of a character) to obfuscate the payload of a particular request. This may allow the adversary to bypass filters that attempt to detect illegal characters or strings, such as those that might be used in traversal or injection attacks. Filters may be able to catch illegal encoded strings, but may not catch doubly encoded strings. For example, a dot (.), often used in path traversal attacks and therefore often blocked by filters, could be URL encoded as %2E. However, many filters recognize this encoding and would still block the request. In a double encoding, the % in the above URL encoding would be encoded again as %25, resulting in %252E which some filters might not catch, but which could still be interpreted as a dot (.) by interpreters on the target.
- **Mitigations:** Assume all input is malicious. Create a white list that defines all valid input to the software system based on the requirements specifications. Input that does not match against the white list should not be permitted to enter into the system. Test your decoding process against malicious input. Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding. When client input is required from web-based forms, avoid using the GET method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the POST method whenever possible. Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.Refer to the RFCs to safely decode URL. Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive. There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).
- **References:** https://capec.mitre.org/data/definitions/120.html, http://cwe.mitre.org/data/definitions/173.html, http://cwe.mitre.org/data/definitions/177.html

#### F203 (DE03) — Sniffing Attacks

- **Target:** API key/token
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F268 (DE03) — Sniffing Attacks

- **Target:** API response
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F258 (DE03) — Sniffing Attacks

- **Target:** Context + prompt
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F273 (DE03) — Sniffing Attacks

- **Target:** Display response
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F218 (DE03) — Sniffing Attacks

- **Target:** File to API
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F213 (DE03) — Sniffing Attacks

- **Target:** File upload
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F263 (DE03) — Sniffing Attacks

- **Target:** LLM response
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F243 (DE03) — Sniffing Attacks

- **Target:** Prompt to API
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F248 (DE03) — Sniffing Attacks

- **Target:** Query vectors
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F253 (DE03) — Sniffing Attacks

- **Target:** Relevant chunks
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F223 (DE03) — Sniffing Attacks

- **Target:** Store file
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F233 (DE03) — Sniffing Attacks

- **Target:** Store vectors
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F208 (DE03) — Sniffing Attacks

- **Target:** Token validation
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F228 (DE03) — Sniffing Attacks

- **Target:** Trigger embedding
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F238 (DE03) — Sniffing Attacks

- **Target:** User prompt
- **Details:** In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the information. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient.
- **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
- **References:** https://capec.mitre.org/data/definitions/157.html, http://cwe.mitre.org/data/definitions/311.html

#### F095 (DO01) — Flooding

- **Target:** Auth & Billing Service
- **Details:** An adversary consumes the resources of a target by rapidly engaging in a large number of interactions with the target. This type of attack generally exposes a weakness in rate limiting or flow. When successful this attack prevents legitimate users from accessing the service and can cause the target to crash. This attack differs from resource depletion through leaks or allocations in that the latter attacks do not rely on the volume of requests made to the target but instead focus on manipulation of the target's operations. The key factor in a flooding attack is the number of requests the adversary can make in a given period of time. The greater this number, the more likely an attack is to succeed against a given target.
- **Mitigations:** Ensure that protocols have specific limits of scale configured. Specify expectations for capabilities and dictate which behaviors are acceptable when resource allocation reaches limits. Uniformly throttle all requests in order to make it more difficult to consume resources more quickly than they can again be freed.
- **References:** https://capec.mitre.org/data/definitions/125.html, http://cwe.mitre.org/data/definitions/404.html, http://cwe.mitre.org/data/definitions/770.html

#### F051 (DO01) — Flooding

- **Target:** Gemini API Gateway
- **Details:** An adversary consumes the resources of a target by rapidly engaging in a large number of interactions with the target. This type of attack generally exposes a weakness in rate limiting or flow. When successful this attack prevents legitimate users from accessing the service and can cause the target to crash. This attack differs from resource depletion through leaks or allocations in that the latter attacks do not rely on the volume of requests made to the target but instead focus on manipulation of the target's operations. The key factor in a flooding attack is the number of requests the adversary can make in a given period of time. The greater this number, the more likely an attack is to succeed against a given target.
- **Mitigations:** Ensure that protocols have specific limits of scale configured. Specify expectations for capabilities and dictate which behaviors are acceptable when resource allocation reaches limits. Uniformly throttle all requests in order to make it more difficult to consume resources more quickly than they can again be freed.
- **References:** https://capec.mitre.org/data/definitions/125.html, http://cwe.mitre.org/data/definitions/404.html, http://cwe.mitre.org/data/definitions/770.html

#### F163 (DO01) — Flooding

- **Target:** Gemini LLM
- **Details:** An adversary consumes the resources of a target by rapidly engaging in a large number of interactions with the target. This type of attack generally exposes a weakness in rate limiting or flow. When successful this attack prevents legitimate users from accessing the service and can cause the target to crash. This attack differs from resource depletion through leaks or allocations in that the latter attacks do not rely on the volume of requests made to the target but instead focus on manipulation of the target's operations. The key factor in a flooding attack is the number of requests the adversary can make in a given period of time. The greater this number, the more likely an attack is to succeed against a given target.
- **Mitigations:** Ensure that protocols have specific limits of scale configured. Specify expectations for capabilities and dictate which behaviors are acceptable when resource allocation reaches limits. Uniformly throttle all requests in order to make it more difficult to consume resources more quickly than they can again be freed.
- **References:** https://capec.mitre.org/data/definitions/125.html, http://cwe.mitre.org/data/definitions/404.html, http://cwe.mitre.org/data/definitions/770.html

#### F007 (DO01) — Flooding

- **Target:** Gemini SDK / REST Client
- **Details:** An adversary consumes the resources of a target by rapidly engaging in a large number of interactions with the target. This type of attack generally exposes a weakness in rate limiting or flow. When successful this attack prevents legitimate users from accessing the service and can cause the target to crash. This attack differs from resource depletion through leaks or allocations in that the latter attacks do not rely on the volume of requests made to the target but instead focus on manipulation of the target's operations. The key factor in a flooding attack is the number of requests the adversary can make in a given period of time. The greater this number, the more likely an attack is to succeed against a given target.
- **Mitigations:** Ensure that protocols have specific limits of scale configured. Specify expectations for capabilities and dictate which behaviors are acceptable when resource allocation reaches limits. Uniformly throttle all requests in order to make it more difficult to consume resources more quickly than they can again be freed.
- **References:** https://capec.mitre.org/data/definitions/125.html, http://cwe.mitre.org/data/definitions/404.html, http://cwe.mitre.org/data/definitions/770.html

#### F097 (DO02) — Excessive Allocation

- **Target:** Auth & Billing Service
- **Details:** An adversary causes the target to allocate excessive resources to servicing the attackers' request, thereby reducing the resources available for legitimate services and degrading or denying services. Usually, this attack focuses on memory allocation, but any finite resource on the target could be the attacked, including bandwidth, processing cycles, or other resources. This attack does not attempt to force this allocation through a large number of requests (that would be Resource Depletion through Flooding) but instead uses one or a small number of requests that are carefully formatted to force the target to allocate excessive resources to service this request(s). Often this attack takes advantage of a bug in the target to cause the target to allocate resources vastly beyond what would be needed for a normal request.
- **Mitigations:** Limit the amount of resources that are accessible to unprivileged users. Assume all input is malicious. Consider all potentially relevant properties when validating input. Consider uniformly throttling all requests in order to make it more difficult to consume resources more quickly than they can again be freed. Use resource-limiting settings, if possible.
- **References:** https://capec.mitre.org/data/definitions/130.html, http://cwe.mitre.org/data/definitions/770.html, http://cwe.mitre.org/data/definitions/404.html

#### F149 (DO02) — Excessive Allocation

- **Target:** Context Injection Engine
- **Details:** An adversary causes the target to allocate excessive resources to servicing the attackers' request, thereby reducing the resources available for legitimate services and degrading or denying services. Usually, this attack focuses on memory allocation, but any finite resource on the target could be the attacked, including bandwidth, processing cycles, or other resources. This attack does not attempt to force this allocation through a large number of requests (that would be Resource Depletion through Flooding) but instead uses one or a small number of requests that are carefully formatted to force the target to allocate excessive resources to service this request(s). Often this attack takes advantage of a bug in the target to cause the target to allocate resources vastly beyond what would be needed for a normal request.
- **Mitigations:** Limit the amount of resources that are accessible to unprivileged users. Assume all input is malicious. Consider all potentially relevant properties when validating input. Consider uniformly throttling all requests in order to make it more difficult to consume resources more quickly than they can again be freed. Use resource-limiting settings, if possible.
- **References:** https://capec.mitre.org/data/definitions/130.html, http://cwe.mitre.org/data/definitions/770.html, http://cwe.mitre.org/data/definitions/404.html

#### F137 (DO02) — Excessive Allocation

- **Target:** Embedding Service
- **Details:** An adversary causes the target to allocate excessive resources to servicing the attackers' request, thereby reducing the resources available for legitimate services and degrading or denying services. Usually, this attack focuses on memory allocation, but any finite resource on the target could be the attacked, including bandwidth, processing cycles, or other resources. This attack does not attempt to force this allocation through a large number of requests (that would be Resource Depletion through Flooding) but instead uses one or a small number of requests that are carefully formatted to force the target to allocate excessive resources to service this request(s). Often this attack takes advantage of a bug in the target to cause the target to allocate resources vastly beyond what would be needed for a normal request.
- **Mitigations:** Limit the amount of resources that are accessible to unprivileged users. Assume all input is malicious. Consider all potentially relevant properties when validating input. Consider uniformly throttling all requests in order to make it more difficult to consume resources more quickly than they can again be freed. Use resource-limiting settings, if possible.
- **References:** https://capec.mitre.org/data/definitions/130.html, http://cwe.mitre.org/data/definitions/770.html, http://cwe.mitre.org/data/definitions/404.html

#### F053 (DO02) — Excessive Allocation

- **Target:** Gemini API Gateway
- **Details:** An adversary causes the target to allocate excessive resources to servicing the attackers' request, thereby reducing the resources available for legitimate services and degrading or denying services. Usually, this attack focuses on memory allocation, but any finite resource on the target could be the attacked, including bandwidth, processing cycles, or other resources. This attack does not attempt to force this allocation through a large number of requests (that would be Resource Depletion through Flooding) but instead uses one or a small number of requests that are carefully formatted to force the target to allocate excessive resources to service this request(s). Often this attack takes advantage of a bug in the target to cause the target to allocate resources vastly beyond what would be needed for a normal request.
- **Mitigations:** Limit the amount of resources that are accessible to unprivileged users. Assume all input is malicious. Consider all potentially relevant properties when validating input. Consider uniformly throttling all requests in order to make it more difficult to consume resources more quickly than they can again be freed. Use resource-limiting settings, if possible.
- **References:** https://capec.mitre.org/data/definitions/130.html, http://cwe.mitre.org/data/definitions/770.html, http://cwe.mitre.org/data/definitions/404.html

#### F165 (DO02) — Excessive Allocation

- **Target:** Gemini LLM
- **Details:** An adversary causes the target to allocate excessive resources to servicing the attackers' request, thereby reducing the resources available for legitimate services and degrading or denying services. Usually, this attack focuses on memory allocation, but any finite resource on the target could be the attacked, including bandwidth, processing cycles, or other resources. This attack does not attempt to force this allocation through a large number of requests (that would be Resource Depletion through Flooding) but instead uses one or a small number of requests that are carefully formatted to force the target to allocate excessive resources to service this request(s). Often this attack takes advantage of a bug in the target to cause the target to allocate resources vastly beyond what would be needed for a normal request.
- **Mitigations:** Limit the amount of resources that are accessible to unprivileged users. Assume all input is malicious. Consider all potentially relevant properties when validating input. Consider uniformly throttling all requests in order to make it more difficult to consume resources more quickly than they can again be freed. Use resource-limiting settings, if possible.
- **References:** https://capec.mitre.org/data/definitions/130.html, http://cwe.mitre.org/data/definitions/770.html, http://cwe.mitre.org/data/definitions/404.html

#### F009 (DO02) — Excessive Allocation

- **Target:** Gemini SDK / REST Client
- **Details:** An adversary causes the target to allocate excessive resources to servicing the attackers' request, thereby reducing the resources available for legitimate services and degrading or denying services. Usually, this attack focuses on memory allocation, but any finite resource on the target could be the attacked, including bandwidth, processing cycles, or other resources. This attack does not attempt to force this allocation through a large number of requests (that would be Resource Depletion through Flooding) but instead uses one or a small number of requests that are carefully formatted to force the target to allocate excessive resources to service this request(s). Often this attack takes advantage of a bug in the target to cause the target to allocate resources vastly beyond what would be needed for a normal request.
- **Mitigations:** Limit the amount of resources that are accessible to unprivileged users. Assume all input is malicious. Consider all potentially relevant properties when validating input. Consider uniformly throttling all requests in order to make it more difficult to consume resources more quickly than they can again be freed. Use resource-limiting settings, if possible.
- **References:** https://capec.mitre.org/data/definitions/130.html, http://cwe.mitre.org/data/definitions/770.html, http://cwe.mitre.org/data/definitions/404.html

#### F134 (DO02) — Excessive Allocation

- **Target:** User File Store
- **Details:** An adversary causes the target to allocate excessive resources to servicing the attackers' request, thereby reducing the resources available for legitimate services and degrading or denying services. Usually, this attack focuses on memory allocation, but any finite resource on the target could be the attacked, including bandwidth, processing cycles, or other resources. This attack does not attempt to force this allocation through a large number of requests (that would be Resource Depletion through Flooding) but instead uses one or a small number of requests that are carefully formatted to force the target to allocate excessive resources to service this request(s). Often this attack takes advantage of a bug in the target to cause the target to allocate resources vastly beyond what would be needed for a normal request.
- **Mitigations:** Limit the amount of resources that are accessible to unprivileged users. Assume all input is malicious. Consider all potentially relevant properties when validating input. Consider uniformly throttling all requests in order to make it more difficult to consume resources more quickly than they can again be freed. Use resource-limiting settings, if possible.
- **References:** https://capec.mitre.org/data/definitions/130.html, http://cwe.mitre.org/data/definitions/770.html, http://cwe.mitre.org/data/definitions/404.html

#### F146 (DO02) — Excessive Allocation

- **Target:** Vector Store
- **Details:** An adversary causes the target to allocate excessive resources to servicing the attackers' request, thereby reducing the resources available for legitimate services and degrading or denying services. Usually, this attack focuses on memory allocation, but any finite resource on the target could be the attacked, including bandwidth, processing cycles, or other resources. This attack does not attempt to force this allocation through a large number of requests (that would be Resource Depletion through Flooding) but instead uses one or a small number of requests that are carefully formatted to force the target to allocate excessive resources to service this request(s). Often this attack takes advantage of a bug in the target to cause the target to allocate resources vastly beyond what would be needed for a normal request.
- **Mitigations:** Limit the amount of resources that are accessible to unprivileged users. Assume all input is malicious. Consider all potentially relevant properties when validating input. Consider uniformly throttling all requests in order to make it more difficult to consume resources more quickly than they can again be freed. Use resource-limiting settings, if possible.
- **References:** https://capec.mitre.org/data/definitions/130.html, http://cwe.mitre.org/data/definitions/770.html, http://cwe.mitre.org/data/definitions/404.html

#### F092 (DS01) — Excavation

- **Target:** Auth & Billing Service
- **Details:** An adversary actively probes the target in a manner that is designed to solicit information that could be leveraged for malicious purposes. This is achieved by exploring the target via ordinary interactions for the purpose of gathering intelligence about the target, or by sending data that is syntactically invalid or non-standard in an attempt to produce a response that contains the desired data. As a result of these interactions, the adversary is able to obtain information from the target that aids the attacker in making inferences about its security, configuration, or potential vulnerabilities. Examplar exchanges with the target may trigger unhandled exceptions or verbose error messages that reveal information like stack traces, configuration information, path information, or database design. This type of attack also includes the manipulation of query strings in a URI to produce invalid SQL queries, or by trying alternative path values in the hope that the server will return useful information.
- **Mitigations:** Minimize error/response output to only what is necessary for functional use or corrective language. Remove potentially sensitive information that is not necessary for the application's functionality.
- **References:** https://capec.mitre.org/data/definitions/116.html, http://cwe.mitre.org/data/definitions/200.html

#### F048 (DS01) — Excavation

- **Target:** Gemini API Gateway
- **Details:** An adversary actively probes the target in a manner that is designed to solicit information that could be leveraged for malicious purposes. This is achieved by exploring the target via ordinary interactions for the purpose of gathering intelligence about the target, or by sending data that is syntactically invalid or non-standard in an attempt to produce a response that contains the desired data. As a result of these interactions, the adversary is able to obtain information from the target that aids the attacker in making inferences about its security, configuration, or potential vulnerabilities. Examplar exchanges with the target may trigger unhandled exceptions or verbose error messages that reveal information like stack traces, configuration information, path information, or database design. This type of attack also includes the manipulation of query strings in a URI to produce invalid SQL queries, or by trying alternative path values in the hope that the server will return useful information.
- **Mitigations:** Minimize error/response output to only what is necessary for functional use or corrective language. Remove potentially sensitive information that is not necessary for the application's functionality.
- **References:** https://capec.mitre.org/data/definitions/116.html, http://cwe.mitre.org/data/definitions/200.html

#### F160 (DS01) — Excavation

- **Target:** Gemini LLM
- **Details:** An adversary actively probes the target in a manner that is designed to solicit information that could be leveraged for malicious purposes. This is achieved by exploring the target via ordinary interactions for the purpose of gathering intelligence about the target, or by sending data that is syntactically invalid or non-standard in an attempt to produce a response that contains the desired data. As a result of these interactions, the adversary is able to obtain information from the target that aids the attacker in making inferences about its security, configuration, or potential vulnerabilities. Examplar exchanges with the target may trigger unhandled exceptions or verbose error messages that reveal information like stack traces, configuration information, path information, or database design. This type of attack also includes the manipulation of query strings in a URI to produce invalid SQL queries, or by trying alternative path values in the hope that the server will return useful information.
- **Mitigations:** Minimize error/response output to only what is necessary for functional use or corrective language. Remove potentially sensitive information that is not necessary for the application's functionality.
- **References:** https://capec.mitre.org/data/definitions/116.html, http://cwe.mitre.org/data/definitions/200.html

#### F004 (DS01) — Excavation

- **Target:** Gemini SDK / REST Client
- **Details:** An adversary actively probes the target in a manner that is designed to solicit information that could be leveraged for malicious purposes. This is achieved by exploring the target via ordinary interactions for the purpose of gathering intelligence about the target, or by sending data that is syntactically invalid or non-standard in an attempt to produce a response that contains the desired data. As a result of these interactions, the adversary is able to obtain information from the target that aids the attacker in making inferences about its security, configuration, or potential vulnerabilities. Examplar exchanges with the target may trigger unhandled exceptions or verbose error messages that reveal information like stack traces, configuration information, path information, or database design. This type of attack also includes the manipulation of query strings in a URI to produce invalid SQL queries, or by trying alternative path values in the hope that the server will return useful information.
- **Mitigations:** Minimize error/response output to only what is necessary for functional use or corrective language. Remove potentially sensitive information that is not necessary for the application's functionality.
- **References:** https://capec.mitre.org/data/definitions/116.html, http://cwe.mitre.org/data/definitions/200.html

#### F112 (DS04) — XSS Targeting Error Pages

- **Target:** Auth & Billing Service
- **Details:** An adversary distributes a link (or possibly some other query structure) with a request to a third party web server that is malformed and also contains a block of exploit code in order to have the exploit become live code in the resulting error page. When the third party web server receives the crafted request and notes the error it then creates an error message that echoes the malformed message, including the exploit. Doing this converts the exploit portion of the message into to valid language elements that are executed by the viewing browser. When a victim executes the query provided by the attacker the infected error message error message is returned including the exploit code which then runs in the victim's browser. XSS can result in execution of code as well as data leakage (e.g. session cookies can be sent to the attacker). This type of attack is especially dangerous since the exploit appears to come from the third party web server, who the victim may trust and hence be more vulnerable to deception.
- **Mitigations:** Design: Use libraries and templates that minimize unfiltered input.Implementation: Normalize, filter and white list any input that will be used in error messages.Implementation: The victim should configure the browser to minimize active content from untrusted sources.
- **References:** https://capec.mitre.org/data/definitions/198.html, http://cwe.mitre.org/data/definitions/81.html

#### F068 (DS04) — XSS Targeting Error Pages

- **Target:** Gemini API Gateway
- **Details:** An adversary distributes a link (or possibly some other query structure) with a request to a third party web server that is malformed and also contains a block of exploit code in order to have the exploit become live code in the resulting error page. When the third party web server receives the crafted request and notes the error it then creates an error message that echoes the malformed message, including the exploit. Doing this converts the exploit portion of the message into to valid language elements that are executed by the viewing browser. When a victim executes the query provided by the attacker the infected error message error message is returned including the exploit code which then runs in the victim's browser. XSS can result in execution of code as well as data leakage (e.g. session cookies can be sent to the attacker). This type of attack is especially dangerous since the exploit appears to come from the third party web server, who the victim may trust and hence be more vulnerable to deception.
- **Mitigations:** Design: Use libraries and templates that minimize unfiltered input.Implementation: Normalize, filter and white list any input that will be used in error messages.Implementation: The victim should configure the browser to minimize active content from untrusted sources.
- **References:** https://capec.mitre.org/data/definitions/198.html, http://cwe.mitre.org/data/definitions/81.html

#### F180 (DS04) — XSS Targeting Error Pages

- **Target:** Gemini LLM
- **Details:** An adversary distributes a link (or possibly some other query structure) with a request to a third party web server that is malformed and also contains a block of exploit code in order to have the exploit become live code in the resulting error page. When the third party web server receives the crafted request and notes the error it then creates an error message that echoes the malformed message, including the exploit. Doing this converts the exploit portion of the message into to valid language elements that are executed by the viewing browser. When a victim executes the query provided by the attacker the infected error message error message is returned including the exploit code which then runs in the victim's browser. XSS can result in execution of code as well as data leakage (e.g. session cookies can be sent to the attacker). This type of attack is especially dangerous since the exploit appears to come from the third party web server, who the victim may trust and hence be more vulnerable to deception.
- **Mitigations:** Design: Use libraries and templates that minimize unfiltered input.Implementation: Normalize, filter and white list any input that will be used in error messages.Implementation: The victim should configure the browser to minimize active content from untrusted sources.
- **References:** https://capec.mitre.org/data/definitions/198.html, http://cwe.mitre.org/data/definitions/81.html

#### F024 (DS04) — XSS Targeting Error Pages

- **Target:** Gemini SDK / REST Client
- **Details:** An adversary distributes a link (or possibly some other query structure) with a request to a third party web server that is malformed and also contains a block of exploit code in order to have the exploit become live code in the resulting error page. When the third party web server receives the crafted request and notes the error it then creates an error message that echoes the malformed message, including the exploit. Doing this converts the exploit portion of the message into to valid language elements that are executed by the viewing browser. When a victim executes the query provided by the attacker the infected error message error message is returned including the exploit code which then runs in the victim's browser. XSS can result in execution of code as well as data leakage (e.g. session cookies can be sent to the attacker). This type of attack is especially dangerous since the exploit appears to come from the third party web server, who the victim may trust and hence be more vulnerable to deception.
- **Mitigations:** Design: Use libraries and templates that minimize unfiltered input.Implementation: Normalize, filter and white list any input that will be used in error messages.Implementation: The victim should configure the browser to minimize active content from untrusted sources.
- **References:** https://capec.mitre.org/data/definitions/198.html, http://cwe.mitre.org/data/definitions/81.html

#### F100 (INP10) — Parameter Injection

- **Target:** Auth & Billing Service
- **Details:** An adversary manipulates the content of request parameters for the purpose of undermining the security of the target. Some parameter encodings use text characters as separators. For example, parameters in a HTTP GET message are encoded as name-value pairs separated by an ampersand (&). If an attacker can supply text strings that are used to fill in these parameters, then they can inject special characters used in the encoding scheme to add or modify parameters. For example, if user input is fed directly into an HTTP GET request and the user provides the value myInput&new_param=myValue, then the input parameter is set to myInput, but a new parameter (new_param) is also added with a value of myValue. This can significantly change the meaning of the query that is processed by the server. Any encoding scheme where parameters are identified and separated by text characters is potentially vulnerable to this attack - the HTTP GET encoding used above is just one example.
- **Mitigations:** Implement an audit log written to a separate host. In the event of a compromise, the audit log may be able to provide evidence and details of the compromise. Treat all user input as untrusted data that must be validated before use.
- **References:** https://capec.mitre.org/data/definitions/137.html, http://cwe.mitre.org/data/definitions/88.html

#### F056 (INP10) — Parameter Injection

- **Target:** Gemini API Gateway
- **Details:** An adversary manipulates the content of request parameters for the purpose of undermining the security of the target. Some parameter encodings use text characters as separators. For example, parameters in a HTTP GET message are encoded as name-value pairs separated by an ampersand (&). If an attacker can supply text strings that are used to fill in these parameters, then they can inject special characters used in the encoding scheme to add or modify parameters. For example, if user input is fed directly into an HTTP GET request and the user provides the value myInput&new_param=myValue, then the input parameter is set to myInput, but a new parameter (new_param) is also added with a value of myValue. This can significantly change the meaning of the query that is processed by the server. Any encoding scheme where parameters are identified and separated by text characters is potentially vulnerable to this attack - the HTTP GET encoding used above is just one example.
- **Mitigations:** Implement an audit log written to a separate host. In the event of a compromise, the audit log may be able to provide evidence and details of the compromise. Treat all user input as untrusted data that must be validated before use.
- **References:** https://capec.mitre.org/data/definitions/137.html, http://cwe.mitre.org/data/definitions/88.html

#### F168 (INP10) — Parameter Injection

- **Target:** Gemini LLM
- **Details:** An adversary manipulates the content of request parameters for the purpose of undermining the security of the target. Some parameter encodings use text characters as separators. For example, parameters in a HTTP GET message are encoded as name-value pairs separated by an ampersand (&). If an attacker can supply text strings that are used to fill in these parameters, then they can inject special characters used in the encoding scheme to add or modify parameters. For example, if user input is fed directly into an HTTP GET request and the user provides the value myInput&new_param=myValue, then the input parameter is set to myInput, but a new parameter (new_param) is also added with a value of myValue. This can significantly change the meaning of the query that is processed by the server. Any encoding scheme where parameters are identified and separated by text characters is potentially vulnerable to this attack - the HTTP GET encoding used above is just one example.
- **Mitigations:** Implement an audit log written to a separate host. In the event of a compromise, the audit log may be able to provide evidence and details of the compromise. Treat all user input as untrusted data that must be validated before use.
- **References:** https://capec.mitre.org/data/definitions/137.html, http://cwe.mitre.org/data/definitions/88.html

#### F012 (INP10) — Parameter Injection

- **Target:** Gemini SDK / REST Client
- **Details:** An adversary manipulates the content of request parameters for the purpose of undermining the security of the target. Some parameter encodings use text characters as separators. For example, parameters in a HTTP GET message are encoded as name-value pairs separated by an ampersand (&). If an attacker can supply text strings that are used to fill in these parameters, then they can inject special characters used in the encoding scheme to add or modify parameters. For example, if user input is fed directly into an HTTP GET request and the user provides the value myInput&new_param=myValue, then the input parameter is set to myInput, but a new parameter (new_param) is also added with a value of myValue. This can significantly change the meaning of the query that is processed by the server. Any encoding scheme where parameters are identified and separated by text characters is potentially vulnerable to this attack - the HTTP GET encoding used above is just one example.
- **Mitigations:** Implement an audit log written to a separate host. In the event of a compromise, the audit log may be able to provide evidence and details of the compromise. Treat all user input as untrusted data that must be validated before use.
- **References:** https://capec.mitre.org/data/definitions/137.html, http://cwe.mitre.org/data/definitions/88.html

#### F102 (INP14) — Input Data Manipulation

- **Target:** Auth & Billing Service
- **Details:** An attacker exploits a weakness in input validation by controlling the format, structure, and composition of data to an input-processing interface. By supplying input of a non-standard or unexpected form an attacker can adversely impact the security of the target. For example, using a different character encoding might cause dangerous text to be treated as safe text. Alternatively, the attacker may use certain flags, such as file extensions, to make a target application believe that provided data should be handled using a certain interpreter when the data is not actually of the appropriate type. This can lead to bypassing protection mechanisms, forcing the target to use specific components for input processing, or otherwise causing the user's data to be handled differently than might otherwise be expected. This attack differs from Variable Manipulation in that Variable Manipulation attempts to subvert the target's processing through the value of the input while Input Data Manipulation seeks to control how the input is processed.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc.
- **References:** https://capec.mitre.org/data/definitions/153.html, http://cwe.mitre.org/data/definitions/20.html

#### F153 (INP14) — Input Data Manipulation

- **Target:** Context Injection Engine
- **Details:** An attacker exploits a weakness in input validation by controlling the format, structure, and composition of data to an input-processing interface. By supplying input of a non-standard or unexpected form an attacker can adversely impact the security of the target. For example, using a different character encoding might cause dangerous text to be treated as safe text. Alternatively, the attacker may use certain flags, such as file extensions, to make a target application believe that provided data should be handled using a certain interpreter when the data is not actually of the appropriate type. This can lead to bypassing protection mechanisms, forcing the target to use specific components for input processing, or otherwise causing the user's data to be handled differently than might otherwise be expected. This attack differs from Variable Manipulation in that Variable Manipulation attempts to subvert the target's processing through the value of the input while Input Data Manipulation seeks to control how the input is processed.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc.
- **References:** https://capec.mitre.org/data/definitions/153.html, http://cwe.mitre.org/data/definitions/20.html

#### F141 (INP14) — Input Data Manipulation

- **Target:** Embedding Service
- **Details:** An attacker exploits a weakness in input validation by controlling the format, structure, and composition of data to an input-processing interface. By supplying input of a non-standard or unexpected form an attacker can adversely impact the security of the target. For example, using a different character encoding might cause dangerous text to be treated as safe text. Alternatively, the attacker may use certain flags, such as file extensions, to make a target application believe that provided data should be handled using a certain interpreter when the data is not actually of the appropriate type. This can lead to bypassing protection mechanisms, forcing the target to use specific components for input processing, or otherwise causing the user's data to be handled differently than might otherwise be expected. This attack differs from Variable Manipulation in that Variable Manipulation attempts to subvert the target's processing through the value of the input while Input Data Manipulation seeks to control how the input is processed.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc.
- **References:** https://capec.mitre.org/data/definitions/153.html, http://cwe.mitre.org/data/definitions/20.html

#### F058 (INP14) — Input Data Manipulation

- **Target:** Gemini API Gateway
- **Details:** An attacker exploits a weakness in input validation by controlling the format, structure, and composition of data to an input-processing interface. By supplying input of a non-standard or unexpected form an attacker can adversely impact the security of the target. For example, using a different character encoding might cause dangerous text to be treated as safe text. Alternatively, the attacker may use certain flags, such as file extensions, to make a target application believe that provided data should be handled using a certain interpreter when the data is not actually of the appropriate type. This can lead to bypassing protection mechanisms, forcing the target to use specific components for input processing, or otherwise causing the user's data to be handled differently than might otherwise be expected. This attack differs from Variable Manipulation in that Variable Manipulation attempts to subvert the target's processing through the value of the input while Input Data Manipulation seeks to control how the input is processed.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc.
- **References:** https://capec.mitre.org/data/definitions/153.html, http://cwe.mitre.org/data/definitions/20.html

#### F170 (INP14) — Input Data Manipulation

- **Target:** Gemini LLM
- **Details:** An attacker exploits a weakness in input validation by controlling the format, structure, and composition of data to an input-processing interface. By supplying input of a non-standard or unexpected form an attacker can adversely impact the security of the target. For example, using a different character encoding might cause dangerous text to be treated as safe text. Alternatively, the attacker may use certain flags, such as file extensions, to make a target application believe that provided data should be handled using a certain interpreter when the data is not actually of the appropriate type. This can lead to bypassing protection mechanisms, forcing the target to use specific components for input processing, or otherwise causing the user's data to be handled differently than might otherwise be expected. This attack differs from Variable Manipulation in that Variable Manipulation attempts to subvert the target's processing through the value of the input while Input Data Manipulation seeks to control how the input is processed.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc.
- **References:** https://capec.mitre.org/data/definitions/153.html, http://cwe.mitre.org/data/definitions/20.html

#### F014 (INP14) — Input Data Manipulation

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker exploits a weakness in input validation by controlling the format, structure, and composition of data to an input-processing interface. By supplying input of a non-standard or unexpected form an attacker can adversely impact the security of the target. For example, using a different character encoding might cause dangerous text to be treated as safe text. Alternatively, the attacker may use certain flags, such as file extensions, to make a target application believe that provided data should be handled using a certain interpreter when the data is not actually of the appropriate type. This can lead to bypassing protection mechanisms, forcing the target to use specific components for input processing, or otherwise causing the user's data to be handled differently than might otherwise be expected. This attack differs from Variable Manipulation in that Variable Manipulation attempts to subvert the target's processing through the value of the input while Input Data Manipulation seeks to control how the input is processed.
- **Mitigations:** Validation of user input for type, length, data-range, format, etc.
- **References:** https://capec.mitre.org/data/definitions/153.html, http://cwe.mitre.org/data/definitions/20.html

#### F117 (INP17) — XSS Using MIME Type Mismatch

- **Target:** Auth & Billing Service
- **Details:** An adversary creates a file with scripting content but where the specified MIME type of the file is such that scripting is not expected. The adversary tricks the victim into accessing a URL that responds with the script file. Some browsers will detect that the specified MIME type of the file does not match the actual type of its content and will automatically switch to using an interpreter for the real content type. If the browser does not invoke script filters before doing this, the adversary's script may run on the target unsanitized, possibly revealing the victim's cookies or executing arbitrary script in their browser.
- **Mitigations:** Design: Browsers must invoke script filters to detect that the specified MIME type of the file matches the actual type of its content before deciding which script interpreter to use.
- **References:** http://cwe.mitre.org/data/definitions/79.html, http://cwe.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/646.html

#### F073 (INP17) — XSS Using MIME Type Mismatch

- **Target:** Gemini API Gateway
- **Details:** An adversary creates a file with scripting content but where the specified MIME type of the file is such that scripting is not expected. The adversary tricks the victim into accessing a URL that responds with the script file. Some browsers will detect that the specified MIME type of the file does not match the actual type of its content and will automatically switch to using an interpreter for the real content type. If the browser does not invoke script filters before doing this, the adversary's script may run on the target unsanitized, possibly revealing the victim's cookies or executing arbitrary script in their browser.
- **Mitigations:** Design: Browsers must invoke script filters to detect that the specified MIME type of the file matches the actual type of its content before deciding which script interpreter to use.
- **References:** http://cwe.mitre.org/data/definitions/79.html, http://cwe.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/646.html

#### F185 (INP17) — XSS Using MIME Type Mismatch

- **Target:** Gemini LLM
- **Details:** An adversary creates a file with scripting content but where the specified MIME type of the file is such that scripting is not expected. The adversary tricks the victim into accessing a URL that responds with the script file. Some browsers will detect that the specified MIME type of the file does not match the actual type of its content and will automatically switch to using an interpreter for the real content type. If the browser does not invoke script filters before doing this, the adversary's script may run on the target unsanitized, possibly revealing the victim's cookies or executing arbitrary script in their browser.
- **Mitigations:** Design: Browsers must invoke script filters to detect that the specified MIME type of the file matches the actual type of its content before deciding which script interpreter to use.
- **References:** http://cwe.mitre.org/data/definitions/79.html, http://cwe.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/646.html

#### F029 (INP17) — XSS Using MIME Type Mismatch

- **Target:** Gemini SDK / REST Client
- **Details:** An adversary creates a file with scripting content but where the specified MIME type of the file is such that scripting is not expected. The adversary tricks the victim into accessing a URL that responds with the script file. Some browsers will detect that the specified MIME type of the file does not match the actual type of its content and will automatically switch to using an interpreter for the real content type. If the browser does not invoke script filters before doing this, the adversary's script may run on the target unsanitized, possibly revealing the victim's cookies or executing arbitrary script in their browser.
- **Mitigations:** Design: Browsers must invoke script filters to detect that the specified MIME type of the file matches the actual type of its content before deciding which script interpreter to use.
- **References:** http://cwe.mitre.org/data/definitions/79.html, http://cwe.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/646.html

#### F122 (INP19) — XML External Entities Blowup

- **Target:** Auth & Billing Service
- **Details:** This attack takes advantage of the entity replacement property of XML where the value of the replacement is a URI. A well-crafted XML document could have the entity refer to a URI that consumes a large amount of resources to create a denial of service condition. This can cause the system to either freeze, crash, or execute arbitrary code depending on the URI.
- **Mitigations:** This attack may be mitigated by tweaking the XML parser to not resolve external entities. If external entities are needed, then implement a custom XmlResolver that has a request timeout, data retrieval limit, and restrict resources it can retrieve locally.
- **References:** https://capec.mitre.org/data/definitions/221.html, http://cwe.mitre.org/data/definitions/611.html

#### F078 (INP19) — XML External Entities Blowup

- **Target:** Gemini API Gateway
- **Details:** This attack takes advantage of the entity replacement property of XML where the value of the replacement is a URI. A well-crafted XML document could have the entity refer to a URI that consumes a large amount of resources to create a denial of service condition. This can cause the system to either freeze, crash, or execute arbitrary code depending on the URI.
- **Mitigations:** This attack may be mitigated by tweaking the XML parser to not resolve external entities. If external entities are needed, then implement a custom XmlResolver that has a request timeout, data retrieval limit, and restrict resources it can retrieve locally.
- **References:** https://capec.mitre.org/data/definitions/221.html, http://cwe.mitre.org/data/definitions/611.html

#### F190 (INP19) — XML External Entities Blowup

- **Target:** Gemini LLM
- **Details:** This attack takes advantage of the entity replacement property of XML where the value of the replacement is a URI. A well-crafted XML document could have the entity refer to a URI that consumes a large amount of resources to create a denial of service condition. This can cause the system to either freeze, crash, or execute arbitrary code depending on the URI.
- **Mitigations:** This attack may be mitigated by tweaking the XML parser to not resolve external entities. If external entities are needed, then implement a custom XmlResolver that has a request timeout, data retrieval limit, and restrict resources it can retrieve locally.
- **References:** https://capec.mitre.org/data/definitions/221.html, http://cwe.mitre.org/data/definitions/611.html

#### F034 (INP19) — XML External Entities Blowup

- **Target:** Gemini SDK / REST Client
- **Details:** This attack takes advantage of the entity replacement property of XML where the value of the replacement is a URI. A well-crafted XML document could have the entity refer to a URI that consumes a large amount of resources to create a denial of service condition. This can cause the system to either freeze, crash, or execute arbitrary code depending on the URI.
- **Mitigations:** This attack may be mitigated by tweaking the XML parser to not resolve external entities. If external entities are needed, then implement a custom XmlResolver that has a request timeout, data retrieval limit, and restrict resources it can retrieve locally.
- **References:** https://capec.mitre.org/data/definitions/221.html, http://cwe.mitre.org/data/definitions/611.html

#### F124 (INP21) — DTD Injection

- **Target:** Auth & Billing Service
- **Details:** An attacker injects malicious content into an application's DTD in an attempt to produce a negative technical impact. DTDs are used to describe how XML documents are processed. Certain malformed DTDs (for example, those with excessive entity expansion as described in CAPEC 197) can cause the XML parsers that process the DTDs to consume excessive resources resulting in resource depletion.
- **Mitigations:** Design: Sanitize incoming DTDs to prevent excessive expansion or other actions that could result in impacts like resource depletion.Implementation: Disallow the inclusion of DTDs as part of incoming messages.Implementation: Use XML parsing tools that protect against DTD attacks.
- **References:** https://capec.mitre.org/data/definitions/228.html, http://cwe.mitre.org/data/definitions/829.html

#### F080 (INP21) — DTD Injection

- **Target:** Gemini API Gateway
- **Details:** An attacker injects malicious content into an application's DTD in an attempt to produce a negative technical impact. DTDs are used to describe how XML documents are processed. Certain malformed DTDs (for example, those with excessive entity expansion as described in CAPEC 197) can cause the XML parsers that process the DTDs to consume excessive resources resulting in resource depletion.
- **Mitigations:** Design: Sanitize incoming DTDs to prevent excessive expansion or other actions that could result in impacts like resource depletion.Implementation: Disallow the inclusion of DTDs as part of incoming messages.Implementation: Use XML parsing tools that protect against DTD attacks.
- **References:** https://capec.mitre.org/data/definitions/228.html, http://cwe.mitre.org/data/definitions/829.html

#### F192 (INP21) — DTD Injection

- **Target:** Gemini LLM
- **Details:** An attacker injects malicious content into an application's DTD in an attempt to produce a negative technical impact. DTDs are used to describe how XML documents are processed. Certain malformed DTDs (for example, those with excessive entity expansion as described in CAPEC 197) can cause the XML parsers that process the DTDs to consume excessive resources resulting in resource depletion.
- **Mitigations:** Design: Sanitize incoming DTDs to prevent excessive expansion or other actions that could result in impacts like resource depletion.Implementation: Disallow the inclusion of DTDs as part of incoming messages.Implementation: Use XML parsing tools that protect against DTD attacks.
- **References:** https://capec.mitre.org/data/definitions/228.html, http://cwe.mitre.org/data/definitions/829.html

#### F036 (INP21) — DTD Injection

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker injects malicious content into an application's DTD in an attempt to produce a negative technical impact. DTDs are used to describe how XML documents are processed. Certain malformed DTDs (for example, those with excessive entity expansion as described in CAPEC 197) can cause the XML parsers that process the DTDs to consume excessive resources resulting in resource depletion.
- **Mitigations:** Design: Sanitize incoming DTDs to prevent excessive expansion or other actions that could result in impacts like resource depletion.Implementation: Disallow the inclusion of DTDs as part of incoming messages.Implementation: Use XML parsing tools that protect against DTD attacks.
- **References:** https://capec.mitre.org/data/definitions/228.html, http://cwe.mitre.org/data/definitions/829.html

#### F127 (INP29) — XSS Using Doubled Characters

- **Target:** Auth & Billing Service
- **Details:** The attacker bypasses input validation by using doubled characters in order to perform a cross-site scripting attack. Some filters fail to recognize dangerous sequences if they are preceded by repeated characters. For example, by doubling the < before a script command, (<<script or %3C%3script using URI encoding) the filters of some web applications may fail to recognize the presence of a script tag. If the targeted server is vulnerable to this type of bypass, the attacker can create a crafted URL or other trap to cause a victim to view a page on the targeted server where the malicious content is executed, as per a normal XSS attack.
- **Mitigations:** Design: Use libraries and templates that minimize unfiltered input.Implementation: Normalize, filter and sanitize all user supplied fields.Implementation: The victim should configure the browser to minimize active content from untrusted sources.
- **References:** https://capec.mitre.org/data/definitions/245.html

#### F083 (INP29) — XSS Using Doubled Characters

- **Target:** Gemini API Gateway
- **Details:** The attacker bypasses input validation by using doubled characters in order to perform a cross-site scripting attack. Some filters fail to recognize dangerous sequences if they are preceded by repeated characters. For example, by doubling the < before a script command, (<<script or %3C%3script using URI encoding) the filters of some web applications may fail to recognize the presence of a script tag. If the targeted server is vulnerable to this type of bypass, the attacker can create a crafted URL or other trap to cause a victim to view a page on the targeted server where the malicious content is executed, as per a normal XSS attack.
- **Mitigations:** Design: Use libraries and templates that minimize unfiltered input.Implementation: Normalize, filter and sanitize all user supplied fields.Implementation: The victim should configure the browser to minimize active content from untrusted sources.
- **References:** https://capec.mitre.org/data/definitions/245.html

#### F195 (INP29) — XSS Using Doubled Characters

- **Target:** Gemini LLM
- **Details:** The attacker bypasses input validation by using doubled characters in order to perform a cross-site scripting attack. Some filters fail to recognize dangerous sequences if they are preceded by repeated characters. For example, by doubling the < before a script command, (<<script or %3C%3script using URI encoding) the filters of some web applications may fail to recognize the presence of a script tag. If the targeted server is vulnerable to this type of bypass, the attacker can create a crafted URL or other trap to cause a victim to view a page on the targeted server where the malicious content is executed, as per a normal XSS attack.
- **Mitigations:** Design: Use libraries and templates that minimize unfiltered input.Implementation: Normalize, filter and sanitize all user supplied fields.Implementation: The victim should configure the browser to minimize active content from untrusted sources.
- **References:** https://capec.mitre.org/data/definitions/245.html

#### F039 (INP29) — XSS Using Doubled Characters

- **Target:** Gemini SDK / REST Client
- **Details:** The attacker bypasses input validation by using doubled characters in order to perform a cross-site scripting attack. Some filters fail to recognize dangerous sequences if they are preceded by repeated characters. For example, by doubling the < before a script command, (<<script or %3C%3script using URI encoding) the filters of some web applications may fail to recognize the presence of a script tag. If the targeted server is vulnerable to this type of bypass, the attacker can create a crafted URL or other trap to cause a victim to view a page on the targeted server where the malicious content is executed, as per a normal XSS attack.
- **Mitigations:** Design: Use libraries and templates that minimize unfiltered input.Implementation: Normalize, filter and sanitize all user supplied fields.Implementation: The victim should configure the browser to minimize active content from untrusted sources.
- **References:** https://capec.mitre.org/data/definitions/245.html

#### F129 (INP36) — HTTP Response Smuggling

- **Target:** Auth & Billing Service
- **Details:** An attacker injects content into a server response that is interpreted differently by intermediaries than it is by the target browser. To do this, it takes advantage of inconsistent or incorrect interpretations of the HTTP protocol by various applications. For example, it might use different block terminating characters (CR or LF alone), adding duplicate header fields that browsers interpret as belonging to separate responses, or other techniques. Consequences of this attack can include response-splitting, cross-site scripting, apparent defacement of targeted sites, cache poisoning, or similar actions.
- **Mitigations:** Design: Employ strict adherence to interpretations of HTTP messages wherever possible.Implementation: Encode header information provided by user input so that user-supplied content is not interpreted by intermediaries.
- **References:** https://capec.mitre.org/data/definitions/273.html

#### F085 (INP36) — HTTP Response Smuggling

- **Target:** Gemini API Gateway
- **Details:** An attacker injects content into a server response that is interpreted differently by intermediaries than it is by the target browser. To do this, it takes advantage of inconsistent or incorrect interpretations of the HTTP protocol by various applications. For example, it might use different block terminating characters (CR or LF alone), adding duplicate header fields that browsers interpret as belonging to separate responses, or other techniques. Consequences of this attack can include response-splitting, cross-site scripting, apparent defacement of targeted sites, cache poisoning, or similar actions.
- **Mitigations:** Design: Employ strict adherence to interpretations of HTTP messages wherever possible.Implementation: Encode header information provided by user input so that user-supplied content is not interpreted by intermediaries.
- **References:** https://capec.mitre.org/data/definitions/273.html

#### F197 (INP36) — HTTP Response Smuggling

- **Target:** Gemini LLM
- **Details:** An attacker injects content into a server response that is interpreted differently by intermediaries than it is by the target browser. To do this, it takes advantage of inconsistent or incorrect interpretations of the HTTP protocol by various applications. For example, it might use different block terminating characters (CR or LF alone), adding duplicate header fields that browsers interpret as belonging to separate responses, or other techniques. Consequences of this attack can include response-splitting, cross-site scripting, apparent defacement of targeted sites, cache poisoning, or similar actions.
- **Mitigations:** Design: Employ strict adherence to interpretations of HTTP messages wherever possible.Implementation: Encode header information provided by user input so that user-supplied content is not interpreted by intermediaries.
- **References:** https://capec.mitre.org/data/definitions/273.html

#### F041 (INP36) — HTTP Response Smuggling

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker injects content into a server response that is interpreted differently by intermediaries than it is by the target browser. To do this, it takes advantage of inconsistent or incorrect interpretations of the HTTP protocol by various applications. For example, it might use different block terminating characters (CR or LF alone), adding duplicate header fields that browsers interpret as belonging to separate responses, or other techniques. Consequences of this attack can include response-splitting, cross-site scripting, apparent defacement of targeted sites, cache poisoning, or similar actions.
- **Mitigations:** Design: Employ strict adherence to interpretations of HTTP messages wherever possible.Implementation: Encode header information provided by user input so that user-supplied content is not interpreted by intermediaries.
- **References:** https://capec.mitre.org/data/definitions/273.html

### Severity: Low

#### F114 (CR05) — Encryption Brute Forcing

- **Target:** Auth & Billing Service
- **Details:** An attacker, armed with the cipher text and the encryption algorithm used, performs an exhaustive (brute force) search on the key space to determine the key that decrypts the cipher text to obtain the plaintext.
- **Mitigations:** Use commonly accepted algorithms and recommended key sizes. The key size used will depend on how important it is to keep the data confidential and for how long.In theory a brute force attack performing an exhaustive key space search will always succeed, so the goal is to have computational security. Moore's law needs to be taken into account that suggests that computing resources double every eighteen months.
- **References:** https://capec.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/326.html, http://cwe.mitre.org/data/definitions/327.html, http://cwe.mitre.org/data/definitions/693.html, http://cwe.mitre.org/data/definitions/719.html

#### F070 (CR05) — Encryption Brute Forcing

- **Target:** Gemini API Gateway
- **Details:** An attacker, armed with the cipher text and the encryption algorithm used, performs an exhaustive (brute force) search on the key space to determine the key that decrypts the cipher text to obtain the plaintext.
- **Mitigations:** Use commonly accepted algorithms and recommended key sizes. The key size used will depend on how important it is to keep the data confidential and for how long.In theory a brute force attack performing an exhaustive key space search will always succeed, so the goal is to have computational security. Moore's law needs to be taken into account that suggests that computing resources double every eighteen months.
- **References:** https://capec.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/326.html, http://cwe.mitre.org/data/definitions/327.html, http://cwe.mitre.org/data/definitions/693.html, http://cwe.mitre.org/data/definitions/719.html

#### F182 (CR05) — Encryption Brute Forcing

- **Target:** Gemini LLM
- **Details:** An attacker, armed with the cipher text and the encryption algorithm used, performs an exhaustive (brute force) search on the key space to determine the key that decrypts the cipher text to obtain the plaintext.
- **Mitigations:** Use commonly accepted algorithms and recommended key sizes. The key size used will depend on how important it is to keep the data confidential and for how long.In theory a brute force attack performing an exhaustive key space search will always succeed, so the goal is to have computational security. Moore's law needs to be taken into account that suggests that computing resources double every eighteen months.
- **References:** https://capec.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/326.html, http://cwe.mitre.org/data/definitions/327.html, http://cwe.mitre.org/data/definitions/693.html, http://cwe.mitre.org/data/definitions/719.html

#### F026 (CR05) — Encryption Brute Forcing

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker, armed with the cipher text and the encryption algorithm used, performs an exhaustive (brute force) search on the key space to determine the key that decrypts the cipher text to obtain the plaintext.
- **Mitigations:** Use commonly accepted algorithms and recommended key sizes. The key size used will depend on how important it is to keep the data confidential and for how long.In theory a brute force attack performing an exhaustive key space search will always succeed, so the goal is to have computational security. Moore's law needs to be taken into account that suggests that computing resources double every eighteen months.
- **References:** https://capec.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/326.html, http://cwe.mitre.org/data/definitions/327.html, http://cwe.mitre.org/data/definitions/693.html, http://cwe.mitre.org/data/definitions/719.html

#### F135 (CR05) — Encryption Brute Forcing

- **Target:** User File Store
- **Details:** An attacker, armed with the cipher text and the encryption algorithm used, performs an exhaustive (brute force) search on the key space to determine the key that decrypts the cipher text to obtain the plaintext.
- **Mitigations:** Use commonly accepted algorithms and recommended key sizes. The key size used will depend on how important it is to keep the data confidential and for how long.In theory a brute force attack performing an exhaustive key space search will always succeed, so the goal is to have computational security. Moore's law needs to be taken into account that suggests that computing resources double every eighteen months.
- **References:** https://capec.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/326.html, http://cwe.mitre.org/data/definitions/327.html, http://cwe.mitre.org/data/definitions/693.html, http://cwe.mitre.org/data/definitions/719.html

#### F147 (CR05) — Encryption Brute Forcing

- **Target:** Vector Store
- **Details:** An attacker, armed with the cipher text and the encryption algorithm used, performs an exhaustive (brute force) search on the key space to determine the key that decrypts the cipher text to obtain the plaintext.
- **Mitigations:** Use commonly accepted algorithms and recommended key sizes. The key size used will depend on how important it is to keep the data confidential and for how long.In theory a brute force attack performing an exhaustive key space search will always succeed, so the goal is to have computational security. Moore's law needs to be taken into account that suggests that computing resources double every eighteen months.
- **References:** https://capec.mitre.org/data/definitions/20.html, http://cwe.mitre.org/data/definitions/326.html, http://cwe.mitre.org/data/definitions/327.html, http://cwe.mitre.org/data/definitions/693.html, http://cwe.mitre.org/data/definitions/719.html

#### F106 (HA03) — Web Application Fingerprinting

- **Target:** Auth & Billing Service
- **Details:** An attacker sends a series of probes to a web application in order to elicit version-dependent and type-dependent behavior that assists in identifying the target. An attacker could learn information such as software versions, error pages, and response headers, variations in implementations of the HTTP protocol, directory structures, and other similar information about the targeted service. This information can then be used by an attacker to formulate a targeted attack plan. While web application fingerprinting is not intended to be damaging (although certain activities, such as network scans, can sometimes cause disruptions to vulnerable applications inadvertently) it may often pave the way for more damaging attacks.
- **Mitigations:** Implementation: Obfuscate server fields of HTTP response.Implementation: Hide inner ordering of HTTP response header.Implementation: Customizing HTTP error codes such as 404 or 500.Implementation: Hide URL file extension.Implementation: Hide HTTP response header software information filed.Implementation: Hide cookie's software information filed.Implementation: Appropriately deal with error messages.Implementation: Obfuscate database type in Database API's error message.
- **References:** https://capec.mitre.org/data/definitions/170.html, http://cwe.mitre.org/data/definitions/497.html

#### F062 (HA03) — Web Application Fingerprinting

- **Target:** Gemini API Gateway
- **Details:** An attacker sends a series of probes to a web application in order to elicit version-dependent and type-dependent behavior that assists in identifying the target. An attacker could learn information such as software versions, error pages, and response headers, variations in implementations of the HTTP protocol, directory structures, and other similar information about the targeted service. This information can then be used by an attacker to formulate a targeted attack plan. While web application fingerprinting is not intended to be damaging (although certain activities, such as network scans, can sometimes cause disruptions to vulnerable applications inadvertently) it may often pave the way for more damaging attacks.
- **Mitigations:** Implementation: Obfuscate server fields of HTTP response.Implementation: Hide inner ordering of HTTP response header.Implementation: Customizing HTTP error codes such as 404 or 500.Implementation: Hide URL file extension.Implementation: Hide HTTP response header software information filed.Implementation: Hide cookie's software information filed.Implementation: Appropriately deal with error messages.Implementation: Obfuscate database type in Database API's error message.
- **References:** https://capec.mitre.org/data/definitions/170.html, http://cwe.mitre.org/data/definitions/497.html

#### F174 (HA03) — Web Application Fingerprinting

- **Target:** Gemini LLM
- **Details:** An attacker sends a series of probes to a web application in order to elicit version-dependent and type-dependent behavior that assists in identifying the target. An attacker could learn information such as software versions, error pages, and response headers, variations in implementations of the HTTP protocol, directory structures, and other similar information about the targeted service. This information can then be used by an attacker to formulate a targeted attack plan. While web application fingerprinting is not intended to be damaging (although certain activities, such as network scans, can sometimes cause disruptions to vulnerable applications inadvertently) it may often pave the way for more damaging attacks.
- **Mitigations:** Implementation: Obfuscate server fields of HTTP response.Implementation: Hide inner ordering of HTTP response header.Implementation: Customizing HTTP error codes such as 404 or 500.Implementation: Hide URL file extension.Implementation: Hide HTTP response header software information filed.Implementation: Hide cookie's software information filed.Implementation: Appropriately deal with error messages.Implementation: Obfuscate database type in Database API's error message.
- **References:** https://capec.mitre.org/data/definitions/170.html, http://cwe.mitre.org/data/definitions/497.html

#### F018 (HA03) — Web Application Fingerprinting

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker sends a series of probes to a web application in order to elicit version-dependent and type-dependent behavior that assists in identifying the target. An attacker could learn information such as software versions, error pages, and response headers, variations in implementations of the HTTP protocol, directory structures, and other similar information about the targeted service. This information can then be used by an attacker to formulate a targeted attack plan. While web application fingerprinting is not intended to be damaging (although certain activities, such as network scans, can sometimes cause disruptions to vulnerable applications inadvertently) it may often pave the way for more damaging attacks.
- **Mitigations:** Implementation: Obfuscate server fields of HTTP response.Implementation: Hide inner ordering of HTTP response header.Implementation: Customizing HTTP error codes such as 404 or 500.Implementation: Hide URL file extension.Implementation: Hide HTTP response header software information filed.Implementation: Hide cookie's software information filed.Implementation: Appropriately deal with error messages.Implementation: Obfuscate database type in Database API's error message.
- **References:** https://capec.mitre.org/data/definitions/170.html, http://cwe.mitre.org/data/definitions/497.html

#### F120 (INP18) — Fuzzing and observing application log data/errors for application mapping

- **Target:** Auth & Billing Service
- **Details:** An attacker sends random, malformed, or otherwise unexpected messages to a target application and observes the application's log or error messages returned. Fuzzing techniques involve sending random or malformed messages to a target and monitoring the target's response. The attacker does not initially know how a target will respond to individual messages but by attempting a large number of message variants they may find a variant that trigger's desired behavior. In this attack, the purpose of the fuzzing is to observe the application's log and error messages, although fuzzing a target can also sometimes cause the target to enter an unstable state, causing a crash. By observing logs and error messages, the attacker can learn details about the configuration of the target application and might be able to cause the target to disclose sensitive information.
- **Mitigations:** Design: Construct a 'code book' for error messages. When using a code book, application error messages aren't generated in string or stack trace form, but are catalogued and replaced with a unique (often integer-based) value 'coding' for the error. Such a technique will require helpdesk and hosting personnel to use a 'code book' or similar mapping to decode application errors/logs in order to respond to them normally.Design: wrap application functionality (preferably through the underlying framework) in an output encoding scheme that obscures or cleanses error messages to prevent such attacks. Such a technique is often used in conjunction with the above 'code book' suggestion.Implementation: Obfuscate server fields of HTTP response.Implementation: Hide inner ordering of HTTP response header.Implementation: Customizing HTTP error codes such as 404 or 500.Implementation: Hide HTTP response header software information filed.Implementation: Hide cookie's software information filed.Implementation: Obfuscate database type in Database API's error message.
- **References:** https://capec.mitre.org/data/definitions/215.html, http://cwe.mitre.org/data/definitions/209.html, http://cwe.mitre.org/data/definitions/532.html

#### F076 (INP18) — Fuzzing and observing application log data/errors for application mapping

- **Target:** Gemini API Gateway
- **Details:** An attacker sends random, malformed, or otherwise unexpected messages to a target application and observes the application's log or error messages returned. Fuzzing techniques involve sending random or malformed messages to a target and monitoring the target's response. The attacker does not initially know how a target will respond to individual messages but by attempting a large number of message variants they may find a variant that trigger's desired behavior. In this attack, the purpose of the fuzzing is to observe the application's log and error messages, although fuzzing a target can also sometimes cause the target to enter an unstable state, causing a crash. By observing logs and error messages, the attacker can learn details about the configuration of the target application and might be able to cause the target to disclose sensitive information.
- **Mitigations:** Design: Construct a 'code book' for error messages. When using a code book, application error messages aren't generated in string or stack trace form, but are catalogued and replaced with a unique (often integer-based) value 'coding' for the error. Such a technique will require helpdesk and hosting personnel to use a 'code book' or similar mapping to decode application errors/logs in order to respond to them normally.Design: wrap application functionality (preferably through the underlying framework) in an output encoding scheme that obscures or cleanses error messages to prevent such attacks. Such a technique is often used in conjunction with the above 'code book' suggestion.Implementation: Obfuscate server fields of HTTP response.Implementation: Hide inner ordering of HTTP response header.Implementation: Customizing HTTP error codes such as 404 or 500.Implementation: Hide HTTP response header software information filed.Implementation: Hide cookie's software information filed.Implementation: Obfuscate database type in Database API's error message.
- **References:** https://capec.mitre.org/data/definitions/215.html, http://cwe.mitre.org/data/definitions/209.html, http://cwe.mitre.org/data/definitions/532.html

#### F188 (INP18) — Fuzzing and observing application log data/errors for application mapping

- **Target:** Gemini LLM
- **Details:** An attacker sends random, malformed, or otherwise unexpected messages to a target application and observes the application's log or error messages returned. Fuzzing techniques involve sending random or malformed messages to a target and monitoring the target's response. The attacker does not initially know how a target will respond to individual messages but by attempting a large number of message variants they may find a variant that trigger's desired behavior. In this attack, the purpose of the fuzzing is to observe the application's log and error messages, although fuzzing a target can also sometimes cause the target to enter an unstable state, causing a crash. By observing logs and error messages, the attacker can learn details about the configuration of the target application and might be able to cause the target to disclose sensitive information.
- **Mitigations:** Design: Construct a 'code book' for error messages. When using a code book, application error messages aren't generated in string or stack trace form, but are catalogued and replaced with a unique (often integer-based) value 'coding' for the error. Such a technique will require helpdesk and hosting personnel to use a 'code book' or similar mapping to decode application errors/logs in order to respond to them normally.Design: wrap application functionality (preferably through the underlying framework) in an output encoding scheme that obscures or cleanses error messages to prevent such attacks. Such a technique is often used in conjunction with the above 'code book' suggestion.Implementation: Obfuscate server fields of HTTP response.Implementation: Hide inner ordering of HTTP response header.Implementation: Customizing HTTP error codes such as 404 or 500.Implementation: Hide HTTP response header software information filed.Implementation: Hide cookie's software information filed.Implementation: Obfuscate database type in Database API's error message.
- **References:** https://capec.mitre.org/data/definitions/215.html, http://cwe.mitre.org/data/definitions/209.html, http://cwe.mitre.org/data/definitions/532.html

#### F032 (INP18) — Fuzzing and observing application log data/errors for application mapping

- **Target:** Gemini SDK / REST Client
- **Details:** An attacker sends random, malformed, or otherwise unexpected messages to a target application and observes the application's log or error messages returned. Fuzzing techniques involve sending random or malformed messages to a target and monitoring the target's response. The attacker does not initially know how a target will respond to individual messages but by attempting a large number of message variants they may find a variant that trigger's desired behavior. In this attack, the purpose of the fuzzing is to observe the application's log and error messages, although fuzzing a target can also sometimes cause the target to enter an unstable state, causing a crash. By observing logs and error messages, the attacker can learn details about the configuration of the target application and might be able to cause the target to disclose sensitive information.
- **Mitigations:** Design: Construct a 'code book' for error messages. When using a code book, application error messages aren't generated in string or stack trace form, but are catalogued and replaced with a unique (often integer-based) value 'coding' for the error. Such a technique will require helpdesk and hosting personnel to use a 'code book' or similar mapping to decode application errors/logs in order to respond to them normally.Design: wrap application functionality (preferably through the underlying framework) in an output encoding scheme that obscures or cleanses error messages to prevent such attacks. Such a technique is often used in conjunction with the above 'code book' suggestion.Implementation: Obfuscate server fields of HTTP response.Implementation: Hide inner ordering of HTTP response header.Implementation: Customizing HTTP error codes such as 404 or 500.Implementation: Hide HTTP response header software information filed.Implementation: Hide cookie's software information filed.Implementation: Obfuscate database type in Database API's error message.
- **References:** https://capec.mitre.org/data/definitions/215.html, http://cwe.mitre.org/data/definitions/209.html, http://cwe.mitre.org/data/definitions/532.html

### Severity: Very Low

#### F104 (DS03) — Footprinting

- **Target:** Auth & Billing Service
- **Details:** An adversary engages in probing and exploration activities to identify constituents and properties of the target. Footprinting is a general term to describe a variety of information gathering techniques, often used by attackers in preparation for some attack. It consists of using tools to learn as much as possible about the composition, configuration, and security mechanisms of the targeted application, system or network. Information that might be collected during a footprinting effort could include open ports, applications and their versions, network topology, and similar information. While footprinting is not intended to be damaging (although certain activities, such as network scans, can sometimes cause disruptions to vulnerable applications inadvertently) it may often pave the way for more damaging attacks.
- **Mitigations:** Keep patches up to date by installing weekly or daily if possible.Shut down unnecessary services/ports.Change default passwords by choosing strong passwords.Curtail unexpected input.Encrypt and password-protect sensitive data.Avoid including information that has the potential to identify and compromise your organization's security such as access to business plans, formulas, and proprietary documents.
- **References:** https://capec.mitre.org/data/definitions/169.html, http://cwe.mitre.org/data/definitions/200.html

#### F060 (DS03) — Footprinting

- **Target:** Gemini API Gateway
- **Details:** An adversary engages in probing and exploration activities to identify constituents and properties of the target. Footprinting is a general term to describe a variety of information gathering techniques, often used by attackers in preparation for some attack. It consists of using tools to learn as much as possible about the composition, configuration, and security mechanisms of the targeted application, system or network. Information that might be collected during a footprinting effort could include open ports, applications and their versions, network topology, and similar information. While footprinting is not intended to be damaging (although certain activities, such as network scans, can sometimes cause disruptions to vulnerable applications inadvertently) it may often pave the way for more damaging attacks.
- **Mitigations:** Keep patches up to date by installing weekly or daily if possible.Shut down unnecessary services/ports.Change default passwords by choosing strong passwords.Curtail unexpected input.Encrypt and password-protect sensitive data.Avoid including information that has the potential to identify and compromise your organization's security such as access to business plans, formulas, and proprietary documents.
- **References:** https://capec.mitre.org/data/definitions/169.html, http://cwe.mitre.org/data/definitions/200.html

#### F172 (DS03) — Footprinting

- **Target:** Gemini LLM
- **Details:** An adversary engages in probing and exploration activities to identify constituents and properties of the target. Footprinting is a general term to describe a variety of information gathering techniques, often used by attackers in preparation for some attack. It consists of using tools to learn as much as possible about the composition, configuration, and security mechanisms of the targeted application, system or network. Information that might be collected during a footprinting effort could include open ports, applications and their versions, network topology, and similar information. While footprinting is not intended to be damaging (although certain activities, such as network scans, can sometimes cause disruptions to vulnerable applications inadvertently) it may often pave the way for more damaging attacks.
- **Mitigations:** Keep patches up to date by installing weekly or daily if possible.Shut down unnecessary services/ports.Change default passwords by choosing strong passwords.Curtail unexpected input.Encrypt and password-protect sensitive data.Avoid including information that has the potential to identify and compromise your organization's security such as access to business plans, formulas, and proprietary documents.
- **References:** https://capec.mitre.org/data/definitions/169.html, http://cwe.mitre.org/data/definitions/200.html

#### F016 (DS03) — Footprinting

- **Target:** Gemini SDK / REST Client
- **Details:** An adversary engages in probing and exploration activities to identify constituents and properties of the target. Footprinting is a general term to describe a variety of information gathering techniques, often used by attackers in preparation for some attack. It consists of using tools to learn as much as possible about the composition, configuration, and security mechanisms of the targeted application, system or network. Information that might be collected during a footprinting effort could include open ports, applications and their versions, network topology, and similar information. While footprinting is not intended to be damaging (although certain activities, such as network scans, can sometimes cause disruptions to vulnerable applications inadvertently) it may often pave the way for more damaging attacks.
- **Mitigations:** Keep patches up to date by installing weekly or daily if possible.Shut down unnecessary services/ports.Change default passwords by choosing strong passwords.Curtail unexpected input.Encrypt and password-protect sensitive data.Avoid including information that has the potential to identify and compromise your organization's security such as access to business plans, formulas, and proprietary documents.
- **References:** https://capec.mitre.org/data/definitions/169.html, http://cwe.mitre.org/data/definitions/200.html
