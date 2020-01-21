global toggle
#MaxThreadsPerHotkey 2
*F12::	
	toggle := !toggle
	if (toggle)
		ToolTip, Hook`nStruggle, 100, 150
	while (toggle)
	{
		Send {Space}
		Sleep, 50
	}
	ToolTip
return
*F8:: 
	toggle := !toggle
	if (toggle)
		ToolTip, Carry`nStruggle, 100, 150
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
	Tooltip
return
#MaxThreadsPerHotkey 1
