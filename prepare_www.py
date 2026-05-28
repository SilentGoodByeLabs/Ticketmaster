import os
import shutil

# Create www folder if it doesn't exist
www_dir = os.path.join(os.getcwd(), "www")
if not os.path.exists(www_dir):
    os.makedirs(www_dir)

# Copy index.html
index_src = os.path.join(os.getcwd(), "index.html")
index_dst = os.path.join(www_dir, "index.html")
if os.path.exists(index_src):
    shutil.copy(index_src, index_dst)
    print(f"Copied index.html to www/")

# List of directories to copy
dirs_to_copy = [
    "uk.tmconst.com",
    "s1.ticketm.net",
    "prismic-images.tmol.io",
    "a.ad.gt",
    "af.monetate.net",
    "analytics.tiktok.com",
    "analytics.twitter.com",
    "bat.bing.com",
    "c.lytics.io",
    "cdn.cookielaw.org",
    "cm.g.doubleclick.net",
    "connect.facebook.net",
    "d.t-x.io",
    "d6tizftlrpuof.cloudfront.net",
    "ep1.adtrafficquality.google",
    "ep2.adtrafficquality.google",
    "f517a4ad5736252ee37ec1d79c57b9b0.safeframe.googlesyndication.com",
    "identity.ticketmaster.com",
    "pagead2.googlesyndication.com",
    "resources.xg4ken.com",
    "rules.quantcount.com",
    "s3.us-east-1.amazonaws.com",
    "sc-static.net",
    "se.monetate.net",
    "secure.quantserve.com",
    "securepubads.g.doubleclick.net",
    "static.ads-twitter.com",
    "t.co",
    "t.contentsquare.net",
    "tpc.googlesyndication.com",
    "tr.snapchat.com",
    "www.google.com",
    "www.googleadservices.com",
    "www.googletagmanager.com",
    "www.googletagservices.com",
    "www.gstatic.com",
    "www.redditstatic.com"
]

for dir_name in dirs_to_copy:
    src_dir = os.path.join(os.getcwd(), dir_name)
    dst_dir = os.path.join(www_dir, dir_name)
    if os.path.exists(src_dir) and os.path.isdir(src_dir):
        if os.path.exists(dst_dir):
            shutil.rmtree(dst_dir)
        shutil.copytree(src_dir, dst_dir)
        print(f"Copied {dir_name}/ to www/")

print("Done! www folder is ready.")
