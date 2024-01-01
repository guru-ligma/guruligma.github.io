import os
from tqdm import tqdm


html_file = "gen.html"

count = 1
z_imgs = []

temp = []
for roots, _, files in os.walk("indexed"):
    for file in tqdm(files):
        temp.append(file)
        count += 1
        if count >= 5:
            z_imgs.append(temp)
            temp = []
            count = 1
with open(html_file, "w") as f:
    output = '''
        <div class="container-lg my-1">
            <div class="row justify-content-between">'''
    for imgs in z_imgs:
        for img in imgs:
            output = f"""{output}
                <div class="col-sm-1 col-lg-2 align-items-center">
                    <img class="img-fluid" src="static/img_catalogue/{img}" alt="{img}">
                    <br/>
                    <p class="text-center fw-light">
                        The ID is: {file.split('.')[0]}
                    </p>
                </div>"""
        output = f"""{output}
            </div>
            <div class="row justify-content-between">"""
    output = f"""{output}
        </div>"""
    f.write(output)

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            