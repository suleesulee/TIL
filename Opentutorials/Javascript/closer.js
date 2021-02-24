//1
function outter(){
    function inner(){
        var title = 'coding everybody';
        alert(title);
    }
    inner();
}
outter();


function outter(){
    var title = 'coding everybody';
    function inner(){
        alert(title);
    }
    inner();
}
outter();


//3
function factory_movie(title){
    return {
        get_title : function (){
            return title;
        },
        set_title : function(_title){
            title = _title
        }
    }
}
ghost = factory_movie('Ghost in the shell');
matrix = factory_movie('Matrix');

//4

var arr = []
for(var i =0; i<5;i++){
    arr[i] = function(id){
        return function(){
        console.log(id);
        }
    }(i);   //이해 잘 안감
}
for(var index in arr){
    console.log(arr[index]());
}