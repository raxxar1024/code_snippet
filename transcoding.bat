:::::::批量修改文件名.bat:::::::
@echo off
title 批量修改文件名
setlocal EnableDelayedExpansion
:: 启用延迟变量扩充
 
:GetPath
set zpath=%CD%
set prefix=（已转码）
:GetExt

set answer=N
echo.
echo 您试图将 %zpath%\ 里的所有 .mp4 和 .wmv 类型的文件以 "(已转码)" 为前缀名进行批量转码，是否继续？
set /p answer=继续请输入 Y ，输入其它键放弃...
if "%answer%"=="Y" goto :ReadyToRename
if "%answer%"=="y" goto :ReadyToRename
 
echo 放弃文件改名，按任意键退出... & goto :PauseThenQuit
 
:ReadyToRename
 
set /a num=0
echo.
 
set ext=.mp4
for /f "delims=" %%a in ('dir /a /b *%ext%') do (  
if not exist "已转码" md "已转码"
if not exist "截图" md "截图"
::压缩
ffmpeg.exe -i "%%~a" -s 854*480 -vcodec h264  -b:v 360k -r 15 -keyint_min 25 -acodec aac -b:a 48k -ar 24000 -ac 2 "tmp_%%a"
::修改mp4头
qt-faststart "tmp_%%a" "（已转码）%%a"
::截图
ffmpeg -i "（已转码）%%a" -y -f image2 -ss 00:00:01 -frames:v 1 "(截图)%%~a.jpg"
::拷贝截图到 “截图” 文件夹
move "(截图)%%~a.jpg" "截图"
::拷贝转码后的文件到 “已转码” 文件夹
move "（已转码）%%a" "已转码"
::删除临时文件
del "tmp_%%a"
)  

set ext=.wmv
for /f "delims=" %%a in ('dir /a /b *%ext%') do (  
if not exist "已转码" md "已转码"
if not exist "截图" md "截图"
::压缩
ffmpeg.exe -i "%%~a" -s 854*480 -vcodec h264 -b:v 360k -r 15 -keyint_min 25 -acodec aac -b:a 48k -ar 24000 -ac 2 "tmp_%%~na.mp4"
::修改mp4头
qt-faststart "tmp_%%~na.mp4" "（已转码）%%~na.mp4"
::截图
ffmpeg -i "（已转码）%%~na.mp4" -y -f image2 -ss 00:00:01 -frames:v 1 "(截图)%%~a.jpg"
::拷贝截图到 “截图” 文件夹
move "(截图)%%~a.jpg" "截图"
::拷贝转码后的文件到 “已转码” 文件夹
move "（已转码）%%~na.mp4" "已转码"
::删除临时文件
del "tmp_%%~na.mp4"
)  

echo 完成，按任意键退出...
 
:PauseThenQuit
pause>nul
::::::::::::::::::::::::::::::::