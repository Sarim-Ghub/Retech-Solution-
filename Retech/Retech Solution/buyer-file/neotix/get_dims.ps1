Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile("C:\Users\pc\OneDrive\Desktop\Retech\Retech Solution\buyer-file\neotix\assets\img\home-3\hero-bg.jpg")
Write-Output "Width: $($img.Width), Height: $($img.Height)"
$img.Dispose()
