package main

//
// 计算一个目录下所有文件的 hash (sha256) 值.
// 输出到控制台以及写入结果文件.
// 示例:
//   ./folderhash /root/
//   ./folderhash /root/ /tmp/r.txt
//

import (
    "os"
    "io"
    "fmt"
    "flag"
    "io/ioutil"
    "path/filepath"
    "crypto/sha256"
)

func SHA256File(filename string) (string, error) {
    file, err := os.Open(filename)
    defer file.Close() 
    if err != nil {
        return "",err 
    }

    h := sha256.New() 
    _, err = io.Copy(h,file)
    if err != nil {
        return "",err 
    }
    return fmt.Sprintf("%x",h.Sum(nil)), nil 
}


func SHA256String(str string) (string) {
    sum := sha256.Sum256([]byte(str))
    return fmt.Sprintf("%x",sum)
}

func checkPathIsFolder(path string) (bool, error){
    finfo, err := os.Stat(path)
    if err != nil {
        // no such file or dir
        fmt.Println("Stat {%v} failed :%v", path, err)
        return false,err
    }
    if finfo.IsDir() {
        // it's a file
        return true,nil
    } else {
        // it's a directory
        return false,nil
    }
     
}

func writeResult(fp * os.File, filename string) {
    
    fileDataHashHex, err :=SHA256File(filename)
    if err!=nil {
        fmt.Printf("SHA256File failed of %v !\n", filename)
    }

    filenameHashHex :=SHA256String(filename)

    rs :=fmt.Sprintf("%v    %v    %v\n", filenameHashHex, fileDataHashHex, filename)
    
    fmt.Printf(rs)

    if fp!=nil {
        fp.WriteString(rs)
    }
}

func openResultFile(resultfile string) (* os.File, error) {
    if len(resultfile)>0 {
        // 这行使用追加模式写入文件，如果文件不存在则创建
        f, err := os.OpenFile( resultfile, os.O_CREATE|os.O_APPEND|os.O_RDWR,0660 )
        if err != nil{
            fmt.Println("OpenFile {%v} failed :%v", resultfile, err)
            return nil, err
        }
        return f, nil
    }
    return nil, nil
}

func listAll(path string, fp * os.File) {

    isFolder, err :=checkPathIsFolder(path)
    if err!=nil {
        return
    }
    if isFolder==false {
        writeResult(fp, path)
        return
    }

    files, err := ioutil.ReadDir(path)
    if err!=nil {
        fmt.Printf("ReadDir {%v} failed :%v \n", path, err)
        return
    }
    for _, fi := range files {
        if fi.IsDir() {
            listAll(path + "/" + fi.Name(), fp)
        } else {
            filename :=path + "/" + fi.Name()
            writeResult(fp, filename)
        }
    }
}

func process(path string, resultfile string) {
    fp, err :=openResultFile(resultfile)
    if err!=nil {
        return
    }
    defer fp.Close()

    path =filepath.ToSlash(path)
    fmt.Printf("process, path:%v \n", path)


    listAll(path, fp)
}


func main() {
    if len(os.Args) < 2 {
        fmt.Println("Calculate folder's sha256, result format is 'file_name_sha256    file_data_sha256    file_name'. Have Fun!\n")
        fmt.Println("Usage:")
        fmt.Printf("    %v <input a folder or input a file>\n", filepath.Base(os.Args[0]))
        fmt.Println("Example:")
        fmt.Printf("    ./%v /tmp/ \n", filepath.Base(os.Args[0]))
        fmt.Printf("    ./%v /tmp/video.mp4 \n", filepath.Base(os.Args[0]))
        fmt.Printf("    ./%v /tmp/ > /tmp/folderhash.txt \n", filepath.Base(os.Args[0]))
        return
    }

    flag.Parse()
    root := flag.Arg(0) // 1st argument is the directory location

    resultfile :=""
    if len(os.Args) >= 2 {
        resultfile =flag.Arg(1)
    }

    process(root, resultfile)
}

