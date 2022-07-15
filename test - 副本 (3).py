ssh-keygen -t rsa -C "52725351@qq.com"
git config --global user.name "hackfreedom888"
git config --global user.email "52725351@qq.com"
git config --global --list
ssh -T git@github.com
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:Hackfreedom888/testapp.git
git push -u origin main
