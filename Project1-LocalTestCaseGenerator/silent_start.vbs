Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "c:\AITesterBlueprint\Project1-LocalTestCaseGenerator\run_app.bat" & chr(34), 0
Set WshShell = Nothing
