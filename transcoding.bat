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
echo ����ͼ�� %zpath%\ ������� .mp4 �� .wmv ���͵��ļ��� "(��ת��)" Ϊǰ׺����������ת�룬�Ƿ������
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
if not exist "��ͼ" md "��ͼ"
::ѹ��
ffmpeg.exe -i "%%~a" -s 854*480 -vcodec h264  -b:v 360k -r 15 -keyint_min 25 -acodec aac -b:a 48k -ar 24000 -ac 2 "tmp_%%a"
::�޸�mp4ͷ
qt-faststart "tmp_%%a" "����ת�룩%%a"
::��ͼ
ffmpeg -i "����ת�룩%%a" -y -f image2 -ss 00:00:01 -frames:v 1 "(��ͼ)%%~a.jpg"
::������ͼ�� ����ͼ�� �ļ���
move "(��ͼ)%%~a.jpg" "��ͼ"
::����ת�����ļ��� ����ת�롱 �ļ���
move "����ת�룩%%a" "��ת��"
::ɾ����ʱ�ļ�
del "tmp_%%a"
)  

set ext=.wmv
for /f "delims=" %%a in ('dir /a /b *%ext%') do (  
if not exist "��ת��" md "��ת��"
if not exist "��ͼ" md "��ͼ"
::ѹ��
ffmpeg.exe -i "%%~a" -s 854*480 -vcodec h264 -b:v 360k -r 15 -keyint_min 25 -acodec aac -b:a 48k -ar 24000 -ac 2 "tmp_%%~na.mp4"
::�޸�mp4ͷ
qt-faststart "tmp_%%~na.mp4" "����ת�룩%%~na.mp4"
::��ͼ
ffmpeg -i "����ת�룩%%~na.mp4" -y -f image2 -ss 00:00:01 -frames:v 1 "(��ͼ)%%~a.jpg"
::������ͼ�� ����ͼ�� �ļ���
move "(��ͼ)%%~a.jpg" "��ͼ"
::����ת�����ļ��� ����ת�롱 �ļ���
move "����ת�룩%%~na.mp4" "��ת��"
::ɾ����ʱ�ļ�
del "tmp_%%~na.mp4"
)  

echo ��ɣ���������˳�...
 
:PauseThenQuit
pause>nul
::::::::::::::::::::::::::::::::