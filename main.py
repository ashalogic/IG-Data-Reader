import os
import sys
import base64
import json
import pandas as pd

if(len(sys.argv) < 2):
    print("Please give file name as argv for ex : main datafolder")
    exit()
path = "./" + sys.argv[1] + "/"
DirList = (os.listdir(path))

# Func A
def ConvImagePost2CSV():
    with open("ImagePostExported2CSV.csv", mode='w') as w:
        w.write("image,[caption],follower,like,comment")
        for Dir in DirList:
            json_files = [pos_json for pos_json in os.listdir(
                path + Dir) if pos_json.endswith('.json')]
            if(len(json_files) > 0):
                with open(path + Dir + "/" + json_files[0], encoding="utf8", mode='r') as f:
                    Posts = json.load(f)
                    for p in Posts:
                        if(p["MediaType"] == 1):
                            w.write('\n')
                            w.write(path + Dir + "/Image/" + p["InstaIdentifier"] + ".jpg" + "," + str(base64.b64encode((p["Caption"]["Text"]).encode("utf-8"))) + "," + str(p["User"]["FollowersCount"]) + "," + str(p["LikesCount"]) + "," + str(p["CommentsCount"]))
    return

# Func B
def notd():
    return

# Test
ConvImagePost2CSV()
