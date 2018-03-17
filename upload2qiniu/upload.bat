for /f "tokens=1,2,3 delims=/- " %%a in ("%date%") do @set D=%%a%%b%%c
7z a -tzip "D:\Seeyon\A8\Backup\%D%_upload_file.zip" "D:\Seeyon\A8\base\upload"
python ./upload_qiniu.py