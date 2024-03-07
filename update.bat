git config --global --unset http.proxy
git config --global --unset https.proxy
git add .
git commit -m "update"
git branch -M master
git remote add origin https://github.com/xjsongphy/2023fall-cs101.git
git push -u origin master
pause
