@echo off
setlocal enabledelayedexpansion

rem 设置输入和输出文件夹
set input_folder=m4a
set output_folder=mp3

rem 创建输出文件夹（如果不存在）
if not exist "%output_folder%" mkdir "%output_folder%"

rem 遍历输入文件夹中的所有M4A文件
for %%f in ("%input_folder%\*.m4a") do (
    rem 获取文件名（不带扩展名）
    set filename=%%~nf
    rem 转换文件
    ffmpeg -i "%%f" -c:a libmp3lame -q:a 0 "%output_folder%\!filename!.mp3"
)

echo 转换完成！
pause
