
;DBD
global toggle
#MaxThreadsPerHotkey 2
*F12::	                           
	toggle := !toggle
	while (toggle)
	{
		Send {Space}
		Sleep, 50
	}                                              
return
*F8:: 
	toggle := !toggle
	while (toggle)
	{
		Send {a down} 
		Sleep, 50
		Send {a up}
		Sleep, 50
		Send {d down}
		Sleep, 50
		Send {d up}
		Sleep, 50
	}
return
#MaxThreadsPerHotkey 1
