:::::::批量修改文件名.bat:::::::
@echo off
title 批量修改文件名
setlocal EnableDelayedExpansion
:: 启用延迟变量扩充
 
:GetPath
set zpath=%CD%
set prefix=（已转码）
:GetExt
set ext=.mp4
set answer=N
echo.
echo 您试图将 %zpath%\ 里的所有 %ext% 类型的文件以 %prefix% 为前缀名进行批量改名，是否继续？
set /p answer=继续请输入 Y ，输入其它键放弃...
if "%answer%"=="Y" goto :ReadyToRename
if "%answer%"=="y" goto :ReadyToRename
 
echo 放弃文件改名，按任意键退出... & goto :PauseThenQuit
 
:ReadyToRename
 
set /a num=0
echo.
 

for /f "delims=" %%a in ('dir /a /b *%ext%') do (  
if not exist "已转码" md "已转码"
ffmpeg.exe -i "%%~a" -s 1024*768 -vcodec h264  -b:v 1024k -r 15 -keyint_min 25 -acodec aac -b:a 48k -ar 24000 -ac 2 "tmp_%%a"
qt-faststart "tmp_%%a" "（已转码）%%a"
move "（已转码）%%a" "已转码"
del "tmp_%%a"
)  
 


echo 文件改名完成，按任意键退出...
 
:PauseThenQuit
pause>nul
::::::::::::::::::::::::::::::::