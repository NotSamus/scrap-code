import os
# Remember we have to pass a array or a tuple
def create_process(args):
        pid = os.fork()
        if pid > 0:
            os.waitpid(pid,0)
        elif pid == 0:
            os.execv(args[0],args)

def reader(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            create_process(["/opt/local/bin/steghide", " "])

def main():
    directory = "/Users/lopez/projects/scrap-code/useful_tools/steghide_create/resized_pictures"
    # os.chdir(directory)
    # create_process(["/bin/ls"])
    # reader(directory)
if __name__ == "__main__":
    main()