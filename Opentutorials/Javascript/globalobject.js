function func(){
    alert('Hello?');
}

func();
window.func();

var o = {'func':function(){
    alert('Hello?');
}}
o.func();
window.o.func();