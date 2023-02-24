import json
import os



def init():

    print("A existing project couldn't be found.")
    print("Init new project?: y/n")
    x = str(input())

    if(x!="y"):
        return 0

    print("The name of the website: ")
    name = str(input())

    print("The name of the author: ")
    user = str(input())

    print("Website's description: ")
    desc = str(input())

    f = open("config.conf", "w")
    f.close()
    f = open("config.conf", 'r+')
    f.write(f'{name}\n{user}\n{desc}')
    conf = f.readlines()

    data = {
        
        1:{
            "id": "hello-world",
            "title": "Hello, World!",
            "content": "This is a test post."
        }
    }

    with open("posts.json", "w") as write_file:
        json.dump(data, write_file)

    f = open("index.html", "w")

    f.write(f'<html><head><title>{name} </title>  <meta name="description"content="{desc}"></head> <body> <h1 style="text-align: center">{name}</h1> <p style="text-align: center">{desc} </p>\n ')

    try:
        os.mkdir("./posts")
    except:
        print("") 
    
    with open("posts.json", "r+") as write_file:
        posts = json.load(write_file)

        for i in posts.values():
            post = open(f'./posts/{i["id"]}.html', 'w')
            post = open(f'./posts/{i["id"]}.html', 'r+')
            post.write(f'<html><body>{i["content"]}</body></html>')

            f.write(f'\n<a href="./posts/{i["id"]}.html">{i["title"]}</a>')


    f.write(f'\n</body></html>')

def update():

    f = open("config.conf", 'r+')
    conf = f.readlines()

    name=conf[0]
    user=conf[1]
    desc=conf[2]

    f = open("index.html", "w")

    f.write(f'<html><head><title>{name} </title>  <meta name="description"content="{desc}"></head> <body> <h1 style="text-align: center">{name}</h1> <p style="text-align: center">{desc} </p>\n ')

    try:
        os.mkdir("./posts")
    except:
        print("") 
    
    with open("posts.json", "r+") as write_file:
        posts = json.load(write_file)

        for i in posts.values():
            post = open(f'./posts/{i["id"]}.html', 'w')
            post = open(f'./posts/{i["id"]}.html', 'r+')
            post.write(f'<html><body>{i["content"]}</body></html>')

            f.write(f'\n<a href="./posts/{i["id"]}.html">{i["title"]}</a>')


    f.write(f'\n</body></html>')

    print("Website updated succesfully")


#init a project
if not os.path.exists('./config.conf'):
    init()

else:
    update() #update the website
