:::::::�����޸��ļ���.bat:::::::
@echo off
title �����޸��ļ���
setlocal EnableDelayedExpansion
:: �����ӳٱ�������
 
:GetPath
set zpath=%CD%
set prefix=����ת�룩
:GetExt

set answer=N
echo.
echo ����ͼ�� %zpath%\ ������� %ext% ���͵��ļ��� %prefix% Ϊǰ׺�����������������Ƿ������
set /p answer=���������� Y ����������������...
if "%answer%"=="Y" goto :ReadyToRename
if "%answer%"=="y" goto :ReadyToRename
 
echo �����ļ���������������˳�... & goto :PauseThenQuit
 
:ReadyToRename
 
set /a num=0
echo.
 
set ext=.mp4
for /f "delims=" %%a in ('dir /a /b *%ext%') do (  
if not exist "��ת��" md "��ת��"
::ffmpeg -threads 4 -i "zp.mp4" -s 854*480 -vcodec h264  -b:v 360k -r 15 -keyint_min 25 -acodec aac -b:a 48k -ar 24000 -ac 2 "zp_480p_360k.mp4"
ffmpeg.exe -i "%%~a" -s 854*480 -vcodec h264  -b:v 360k -r 15 -keyint_min 25 -acodec aac -b:a 48k -ar 24000 -ac 2 "tmp_%%a"
qt-faststart "tmp_%%a" "����ת�룩%%a"
move "����ת�룩%%a" "��ת��"
del "tmp_%%a"
)  

set ext=.wmv
for /f "delims=" %%a in ('dir /a /b *%ext%') do (  
if not exist "��ת��" md "��ת��"
::ffmpeg -threads 4 -i "zp.mp4" -s 854*480 -vcodec h264  -b:v 360k -r 15 -keyint_min 25 -acodec aac -b:a 48k -ar 24000 -ac 2 "zp_480p_360k.mp4"
ffmpeg.exe -i "%%~a" -s 854*480 -vcodec h264 -b:v 360k -r 15 -keyint_min 25 -acodec aac -b:a 48k -ar 24000 -ac 2 "tmp_%%~na.mp4"
qt-faststart "tmp_%%~na.mp4" "����ת�룩%%~na.mp4"
move "����ת�룩%%~na.mp4" "��ת��"
del "tmp_%%~na.mp4"
)  

echo �ļ�������ɣ���������˳�...
 
:PauseThenQuit
pause>nul
::::::::::::::::::::::::::::::::