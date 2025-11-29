screenX := A_ScreenWidth / 2 - 15
screenY := A_ScreenHeight / 2 - 15

MyGui := Gui()
MyGui.Opt("+AlwaysOnTop -Caption")
MyGui.BackColor := "000000"

; Vertical bar
MyGui.Add("Progress", "x14 y0 w2 h30 Background0000FF c0000FF", 100)
; Horizontal bar
MyGui.Add("Progress", "x0 y14 w30 h2 Background0000FF c0000FF", 100)

MyGui.Show("x" screenX " y" screenY " w30 h30 NA")

hwnd := MyGui.Hwnd
WinSetTransColor("000000", hwnd)

; Make window click-through
DllCall("SetWindowLong", "Ptr", hwnd, "Int", -20, "Int", DllCall("GetWindowLong", "Ptr", hwnd, "Int", -20) | 0x20)

HotKey "F5", ExitApp
