git config --global --unset http.proxy
git config --global --unset https.proxy
git add .
git commit -m "update"
git branch -M main
git remote add origin https://github.com/xjsongphy/2024spring-cs201.git
git push -u origin main
pause
