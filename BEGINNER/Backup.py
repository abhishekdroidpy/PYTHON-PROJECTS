import os,time,datetime,shutil,schedule

source_dir="/storage/emulated/0/My poems"
dest_direct="/0/storage/emulated/0/Python scripts"

def copy_folder(source,dest):
    today=datetime.date.today()
    dest_dir=os.path.join(dest,str(today))
    
    try:
        shutil.copytree(source,dest_dir)
        print("folder copied to:{dest_dir}")
        
    except Exception as e:
        print(e)
        
        
copy_folder(source_dir,dest_direct)
