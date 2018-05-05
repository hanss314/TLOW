xcopy C:\Users F:\ /E /-Y
REM copies files to an installed flashdrive as backup
sfc /scannow
REM scans for integrity violations
start notepad "C:\Windows\Logs\CBS\CBS.log"
REM opens the log for problematic files
exit