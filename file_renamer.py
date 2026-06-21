import os

folder_path=r"/storage/emulated/0/DCIM/Camera"

files=sorted(os.listdir(folder_path))
img_count=1
vid_count=1

for index,filename in enumerate(files,start=1):
    
    old_path=os.path.join(folder_path,filename)
    
    ext=os.path.splitext(filename)[1]
    
    if  ext in [".jpg",".png",".jpeg",".webp"]:
        new_name=f"img{img_count:03d}{ext}"
        img_count+=1
        

    elif ext==".mp4":
        new_name=f"vid{vid_count:03d}{ext}"   
        vid_count+=1
    
    new_path=os.path.join(folder_path,new_name)
    os.rename(old_path,new_path)
    
print("files renamed succesfully!")    
    
    
