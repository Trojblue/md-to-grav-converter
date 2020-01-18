---
title: '解决Grav CMS迁移后的404问题'
date: '03:45 29-12-2019'
taxonomy:
    category:
        - blog
    tag:
        - Grav
        - Linux
        - 前端
        - VPS
summary:
    enabled: '1'
feed:
    limit: 10
aura:
    pagetype: website
---

解决grav迁移到新VPS以后的404问题

===

(环境: CentOS7.5, 宝塔LNMP)
直接复制黏贴grav到网站根目录`/wwwroot/`以后可能会404，网站首页能正常显示 但其他任何页面都会弹404

## 解决方法

到`/www/server/panel/vhost/nginx`目录, 修改`网站名.conf`: 
增加这段贴在开头
```php
    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }
```
这段贴在结尾
```php
    location ~ \.php$ {
        # Choose either a socket or TCP/IP address
        fastcgi_pass unix:/var/run/php/php7.3-fpm.sock;
        # fastcgi_pass unix:/var/run/php5-fpm.sock; #legacy
        # fastcgi_pass 127.0.0.1:9000;

        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME 	 				$document_root/$fastcgi_script_name;
    }
```
修改完毕后, 输入`sudo nginx -s reload` 重启nginx服务.