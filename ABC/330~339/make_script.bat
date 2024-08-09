@echo off

rem バッチファイルの第1引数がディレクトリ名、第2引数がファイル名として扱われる
set dest_dir=%1
set file_name=%2

rem cp コマンドを使ってファイルをコピーする
copy python_input_template.py "%dest_dir%\%file_name%.py"