from PIL import Image, PngImagePlugin
import os
_file="/home/yerin/code/marketing/00100.png"
image = Image.open(_file)
image=image.resize((1920, 1300))
image.save(_file)
#folder=f"/home/yerin/code/final/"
# filelist=os.listdir(folder)

# for i in filelist:
    
#     try:
#         image = Image.open(folder+i)
#         image=image.resize((1920, 1300))
#         image.save(f"{folder}{i}")
#     except:
#         pass
    
#     import os

# dir_path = "/home/js/tests"

# for (root1, directories1, files1) in os.walk(folder):
#     # for d in directories:
#     #     d_path = os.path.join(root, d)
#     #     print(d_path)
#     for d in directories1:
#         print(d)
#         d_path = os.path.join(root1, d)
#         for (root, directories, files) in os.walk(d_path):
#             for file in files:
                
#                 file_path = os.path.join(root, file)
#                 try:
#                     image = Image.open(file_path)
#                     image=image.resize((1920, 1300))
                    
#                     print(file_path)
#                     image.save(file_path)
#                 except: pass