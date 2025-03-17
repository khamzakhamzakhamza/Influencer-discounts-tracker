mkdir package
pip install -r requirements.txt -t package/
Set-Location package
Compress-Archive -Path * -DestinationPath ../lambda_function.zip -Force
Set-Location ../
Compress-Archive -Path idt_scrapper -DestinationPath lambda_function.zip -Update
Compress-Archive -Path lambda_function.py -DestinationPath lambda_function.zip -Update
Remove-Item -Path package -Recurse -Force