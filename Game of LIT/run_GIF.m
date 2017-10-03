genNum= 1:10;
GIF(50,50,0,1,genNum,0.25)
figure,
f = getframe;
[im,map] = rgb2ind(f.cdata,256);

for genNum=1:10,
GIF(50,50,0,1,genNum,0.25)
f=getframe;
im(:,:,1,genNum) = rgb2ind(f.cdata,map);
end

imwrite(im,map,'GIF.gif','DelayTime',0,'LoopCount',inf);