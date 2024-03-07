git config --global --unset http.proxy
git config --global --unset https.proxy
git add .
git commit -m 'update'
git push -u origin master
pause
