

Restart Nginx
Search for the file, it is probably at: /usr/sbin/nginx . 
To be sure type:

ps aux | grep nginx

To kill process:

sudo killall nginx

And start again 

sudo /usr/sbin/nginx