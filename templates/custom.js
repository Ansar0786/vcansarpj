myfunction=()=>{
    var x = document.getElementById("myFile");
    var txt = "";
    if('files' in x){
        if(x.files.length == 0){
            txt = "Select One File";

        }
        else{
            for(var i=0; i<x.files.length; i++){
                txt += "<br> <strong>" + (i+1) + ".File </strong> <br>";
                var file = x.files[i];
                if('name' in file){
                    txt += "Name:" + file.name + "<br>";

                }
                if('size' in file){
                    txt += "Size:" + file.size + "bytes <br>";

                }
            }
        }
    }
    else{
        if(x.value == ""){
            txt += "Select one or more than one file";
        }
        else{
            txt += "The file property is not supported in your browser";
            txt += "<br> the path of the file:" + x.value;
        }
    }
    document.getElementById("demo").innerHTML = txt;
}