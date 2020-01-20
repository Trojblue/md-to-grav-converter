# test

asdasdasd
asdasd

@Gertt has done some excellent work in getting the first responsive image support into a CMS that I'm aware of that works through Grav's impressive image handling features: http://getgrav.org/blog/retina-responsive-images. 

By marking up an image in an `.md` file like this: `![Alt Text](image.jpg)` and providing an image file like: `image@2x.jpg` you get HTML like (simplified for illustration): ``` <img src="image.jpg" alt="Alt Text" srcset="image@1x.jpeg 300w, image@2x.jpeg 600w" sizes="100vw" data-src="image@1x.jpeg" data-srcsetfallback="true" style=""> ``` 
Cool! When the browser first parses this code, it wants to get started downloading the image file right away, even before it has composed the page layout and determined the actual width of the image on the page. All it knows at that point is the screen density and the viewport width. So, if it's running on a retina display with a viewport width of 1000px, it's going to download the image2x.jpeg file. Even if it later finds out that the image is in a narrow column and ends up being displayed at 100px wide. 
Grav defaults to using `sizes="100vw"` because it has nothing else to go on. Only the author working on that website knows how wide that image might be. Can we/should we want to extend Grav even more by providing Markdown syntax that Grav understands that could be used by the author to define the `sizes=` to be used? We have media actions. Could sizes be another?