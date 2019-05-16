import os;
def ReName():
    dir()
    FolderLink=input()
    #print(os.getcwd())
    os.chdir(FolderLink)
    FileName=os.listdir()
    print(FileName)
    Endl=len(FolderLink)-1
    while FolderLink[Endl]=='/' or FolderLink[Endl]=='\\' or FolderLink[Endl]==':':
        Endl=Endl-1
    Startl=Endl
    while FolderLink[Startl]!='/' and FolderLink[Startl]!='\\' :
        Startl=Startl-1
    Folder=FolderLink[(Startl+1):(Endl+1)]
    print(Folder)
    for i in range(0,len(FileName)):
        if FileName[i][-4:]=='.jpg':
            os.renames(FileName[i], Folder + '_' + str(i+1));
    print(os.listdir())
    return 1
ReName()
#D:\